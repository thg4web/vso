#!/usr/bin/env python3
"""
Export a COMPLETE (not sampled) pull of T CrB observations for a recent
window -- every observation AAVSO has, fully paginated, not just a daily
average. This is the tool for "is this brightening a real trend or one
noisy observation" -- you need the full scatter for that, not one point a day.

This is a separate, deliberate, occasional action -- distinct from
fetch_tcrb.py's sparse daily-sample backfill. Run it when you actually want
a fresh detailed look, not on a schedule.

Usage:
  python3 scripts/export_tcrb_recent.py                      # last 24h, both formats
  python3 scripts/export_tcrb_recent.py --hours 48 --format csv
  python3 scripts/export_tcrb_recent.py --format json --out my_export.json

Requires AAVSO_API_TOKEN in a .env file at the project root (gitignored).
"""
import argparse
import csv as csv_module
import datetime
import json
import os
import sys
import time

from aavso_common import ROOT, BAND_NAMES, REQUEST_GAP_SECONDS, load_token, fetch_page, jd_to_iso

EXPORT_DIR = os.path.join(ROOT, "exports")


def fetch_all(token, start_date, end_date):
    """Paginate through every page for [start_date, end_date) -- half-open range."""
    results = []
    page = 1
    while True:
        payload = fetch_page(token, start_date, end_date, page)
        page_results = payload.get("results", [])
        results.extend(page_results)
        total = payload.get("count", len(results))
        print(f"  page {page}: +{len(page_results)} (have {len(results)}/{total})")
        if not payload.get("next"):
            break
        page += 1
        time.sleep(REQUEST_GAP_SECONDS)
    return results


def normalize(obs):
    band_code = str(obs.get("band"))
    return {
        "date_utc": jd_to_iso(obs["jd_dbl"]),
        "jd": obs["jd_dbl"],
        "magnitude": obs.get("magnitude"),
        "fainter_than": obs.get("fainterthan", False),
        "band_code": band_code,
        "band_name": BAND_NAMES.get(band_code, f"code {band_code}"),
        "uncertainty": obs.get("uncertainty"),
        "observer_code": obs.get("obscode"),
        "obstype": obs.get("obstype"),
    }


def write_json(rows, path):
    with open(path, "w") as f:
        json.dump({
            "star": "T CrB",
            "exported_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "count": len(rows),
            "observations": rows,
        }, f, indent=2)
        f.write("\n")


def write_csv(rows, path):
    fields = ["date_utc", "jd", "magnitude", "fainter_than", "band_code",
              "band_name", "uncertainty", "observer_code", "obstype"]
    with open(path, "w", newline="") as f:
        w = csv_module.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            w.writerow(row)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=24, help="how many hours back (day-granularity on the API, rounded up)")
    ap.add_argument("--format", choices=["json", "csv", "both"], default="both")
    ap.add_argument("--out", help="output path (without extension if --format both)")
    args = ap.parse_args()

    token = load_token()
    today = datetime.date.today()
    days_back = max(1, (args.hours + 23) // 24)
    start = today - datetime.timedelta(days=days_back)
    end = today + datetime.timedelta(days=1)  # half-open; include all of today

    print(f"Pulling ALL T CrB observations from {start.isoformat()} to {today.isoformat()} "
          f"(full pagination, ~{REQUEST_GAP_SECONDS}s/page)...")
    raw = fetch_all(token, start.isoformat(), end.isoformat())
    rows = [normalize(o) for o in raw]
    rows.sort(key=lambda r: r["jd"])

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    base = args.out or os.path.join(EXPORT_DIR, f"tcrb_last{args.hours}h_{stamp}")
    out_dir = os.path.dirname(base) or "."
    os.makedirs(out_dir, exist_ok=True)

    written = []
    if args.format in ("json", "both"):
        path = base if base.endswith(".json") else base + ".json"
        write_json(rows, path)
        written.append(path)
    if args.format in ("csv", "both"):
        path = base if base.endswith(".csv") else base + ".csv"
        write_csv(rows, path)
        written.append(path)

    print(f"\n{len(rows)} observations written:")
    for p in written:
        print(f"  {p}")


if __name__ == "__main__":
    main()
