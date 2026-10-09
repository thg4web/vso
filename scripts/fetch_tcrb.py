#!/usr/bin/env python3
"""
Pull real T CrB observations from the AAVSO API (apps.aavso.org), one day at
a time, and write data/tcrb_observations.json for the Blaze Star Watch page.

One request per calendar day (page=1, up to 10 raw observations returned by
that single request) -- NOT a full paginated pull. We average whatever that
one request returns per band, per day. This is a deliberate choice to stay
far under AAVSO's documented rate limit (<=1 req/10s) and this project's own
self-imposed budget (big backfills are rare/one-time; ongoing refreshes are
capped at a few requests/day) -- see project/docs/ or ask Aaron before
changing the cadence or the days count.

Usage:
  python3 scripts/fetch_tcrb.py --days 30
  python3 scripts/fetch_tcrb.py --days 1          # just today, for a daily refresh

Requires AAVSO_API_TOKEN in a .env file at the project root (gitignored).
"""
import argparse
import datetime
import json
import os
import sys
import time

from aavso_common import ROOT, BAND_MAP, REQUEST_GAP_SECONDS, load_token, fetch_page

DATA_PATH = os.path.join(ROOT, "data", "tcrb_observations.json")


def fetch_day(token, day):
    """day: a datetime.date. Pulls only page 1 (up to 10 raw observations) --
    this is the sparse daily-sample mode, not a full pull. See export_tcrb_recent.py
    for a complete pull of a short window."""
    next_day = day + datetime.timedelta(days=1)
    try:
        return fetch_page(token, day.isoformat(), next_day.isoformat(), 1)
    except Exception as e:
        print(f"  ! request failed for {day.isoformat()}: {e}", file=sys.stderr)
        return None


def summarize_day(day_str, payload):
    """Average magnitude per mapped band for one day's returned observations."""
    if not payload or not payload.get("results"):
        return []
    buckets = {}
    for obs in payload["results"]:
        if obs.get("fainterthan"):
            continue
        band = BAND_MAP.get(str(obs.get("band")))
        if band is None:
            continue
        try:
            mag = float(obs["magnitude"])
        except (TypeError, ValueError):
            continue
        buckets.setdefault(band, []).append(mag)
    points = []
    for band, mags in buckets.items():
        mean_mag = round(sum(mags) / len(mags), 3)
        points.append({"date": day_str, "mag": mean_mag, "band": band, "n": len(mags)})
    return points


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30, help="how many days back from today")
    args = ap.parse_args()

    token = load_token()
    today = datetime.date.today()
    all_points = []

    print(f"Fetching T CrB, {args.days} day(s), ~{REQUEST_GAP_SECONDS}s apart...")
    for i in range(args.days):
        day = today - datetime.timedelta(days=i)
        day_str = day.isoformat()
        print(f"[{i+1}/{args.days}] {day_str} ...", end=" ", flush=True)
        payload = fetch_day(token, day)
        day_points = summarize_day(day_str, payload)
        all_points.extend(day_points)
        if day_points:
            print(", ".join(f"{p['band']}={p['mag']} (n={p['n']})" for p in day_points))
        else:
            print("no usable observations")
        if i < args.days - 1:
            time.sleep(REQUEST_GAP_SECONDS)

    all_points.sort(key=lambda p: p["date"])

    # Preserve the two real historical eruption dates; drop any previously
    # fabricated filler points from earlier seed data.
    historical = [
        {"date": "1866-05-12", "mag": 2.0, "band": "visual"},
        {"date": "1946-02-09", "mag": 2.0, "band": "visual"},
    ]

    out = {
        "note": (
            f"Historical eruption dates (1866, 1946) are real record. Everything "
            f"else is real AAVSO data fetched {datetime.date.today().isoformat()} "
            f"via scripts/fetch_tcrb.py -- one request/day, averaged per band from "
            f"whatever that single request returned (not a full paginated pull). "
            f"Re-run that script to extend coverage or refresh."
        ),
        "fetched_through": today.isoformat(),
        "days_covered": args.days,
        "points": historical + all_points,
    }

    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(out, f, indent=2)
        f.write("\n")

    print(f"\nWrote {len(historical) + len(all_points)} points to {DATA_PATH}")


if __name__ == "__main__":
    main()
