"""Shared helpers for the AAVSO fetch/export scripts. Not a public module,
just split out so fetch_tcrb.py and export_tcrb_recent.py don't duplicate
the token loading and band-code mapping."""
import json
import os
import sys
import time
import urllib.request
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(ROOT, ".env")
API_BASE = "https://apps.aavso.org/v2/api/observations/photometry/"
REQUEST_GAP_SECONDS = 11  # politely over AAVSO's documented 10s minimum

# AAVSO band code -> our chart's band labels.
BAND_MAP = {
    "0": "visual",
    "2": "V",
    "3": "B",
    "8": "V",  # Unfiltered with V zeropoint -- calibrated to the V system
}

# Fuller label set for raw exports (not just the three chart buckets).
BAND_NAMES = {
    "0": "Visual", "1": "Unknown", "2": "Johnson V", "3": "Johnson B",
    "4": "Cousins R", "5": "Cousins I", "6": "Orange (Liller)",
    "7": "Johnson U", "8": "Unfiltered (V zeropoint)", "9": "Unfiltered (R zeropoint)",
    "10": "Johnson R", "11": "Johnson I", "13": "H-alpha", "14": "H-alpha-continuum",
}


def load_token():
    if not os.path.exists(ENV_PATH):
        sys.exit("No .env file found at project root with AAVSO_API_TOKEN=...")
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if line.startswith("AAVSO_API_TOKEN="):
                return line.split("=", 1)[1].strip()
    sys.exit("AAVSO_API_TOKEN not found in .env")


def fetch_page(token, start_date, end_date, page):
    """start_date/end_date: date strings, half-open range [start, end) --
    confirmed empirically that start==end returns count=0."""
    params = urllib.parse.urlencode({
        "target": "T CrB",
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
    })
    req = urllib.request.Request(
        f"{API_BASE}?{params}",
        headers={"Authorization": f"Token {token}"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def jd_to_iso(jd):
    """Julian Date -> ISO 8601 UTC string."""
    import datetime
    dt = datetime.datetime(1970, 1, 1) + datetime.timedelta(days=(jd - 2440587.5))
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
