#!/usr/bin/env python3
"""
Compute today's rise/transit/set times for T CrB from a fixed observer
location. Pure spherical astronomy, no ephemeris/network needed -- a star's
RA/Dec is effectively fixed on human timescales, unlike a planet or the Moon.

Meant to run once daily via cron, right after local midnight, so "today"
means the calendar day that's just started. Writes static/data/tcrb_rise_set.json
for the page to read.

Usage: python3 scripts/compute_rise_set.py
"""
import datetime
import json
import math
import os
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(ROOT, "static", "data", "tcrb_rise_set.json")

# T CrB (J2000): RA 15h 59m 30.16s, Dec +25 55' 12.6" -- from the AAVSO VSX
# lookup earlier in this project (auid 000-BBW-825).
RA_HOURS = 15 + 59 / 60 + 30.16 / 3600
DEC_DEG = 25 + 55 / 60 + 12.6 / 3600

# Observer: Fuquay-Varina, NC (approximate town center -- fine for rise/set,
# which doesn't need backyard-level precision).
LAT_DEG = 35.5846
LON_DEG = -78.7997
TZ_NAME = "America/New_York"

H0_DEG = -0.5667  # standard atmospheric refraction at the horizon for a star


def to_julian_date(dt_utc):
    a = (14 - dt_utc.month) // 12
    y = dt_utc.year + 4800 - a
    m = dt_utc.month + 12 * a - 3
    jdn = dt_utc.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    frac = (dt_utc.hour + dt_utc.minute / 60 + dt_utc.second / 3600) / 24.0
    return jdn + frac - 0.5


def gmst_hours(dt_utc):
    """Greenwich Mean Sidereal Time, in hours, for a UTC datetime."""
    jd = to_julian_date(dt_utc)
    t = (jd - 2451545.0) / 36525.0
    gmst = (280.46061837 + 360.98564736629 * (jd - 2451545.0)
            + 0.000387933 * t ** 2 - t ** 3 / 38710000.0)
    return (gmst % 360.0) / 15.0


def main():
    tz = ZoneInfo(TZ_NAME)
    now_local = datetime.datetime.now(tz)
    today = now_local.date()
    midnight_local = datetime.datetime(today.year, today.month, today.day, tzinfo=tz)
    midnight_utc = midnight_local.astimezone(datetime.timezone.utc)

    gmst0 = gmst_hours(midnight_utc)  # GMST at local midnight tonight

    lat_rad = math.radians(LAT_DEG)
    dec_rad = math.radians(DEC_DEG)
    h0_rad = math.radians(H0_DEG)

    cos_h0 = (math.sin(h0_rad) - math.sin(lat_rad) * math.sin(dec_rad)) / \
              (math.cos(lat_rad) * math.cos(dec_rad))

    def lst_to_elapsed_hours(lst_target_hours):
        """Hours after local midnight (clock time) that LST next equals the target."""
        lon_hours = LON_DEG / 15.0
        gmst_target = (lst_target_hours - lon_hours) % 24.0
        delta_sidereal = (gmst_target - gmst0) % 24.0
        return delta_sidereal * 0.9972695663  # sidereal hours -> solar (clock) hours

    transit_elapsed = lst_to_elapsed_hours(RA_HOURS)
    transit_local = midnight_local + datetime.timedelta(hours=transit_elapsed)

    def iso_utc(dt_local):
        return dt_local.astimezone(datetime.timezone.utc).isoformat().replace("+00:00", "Z")

    result = {
        # "date" anchors which local calendar day this was computed for (cron
        # fires at 12:01 AM local) -- the actual times below are absolute UTC
        # instants so any viewer's browser can render them in their own
        # timezone. These are rise/set as seen from the reference location
        # below, not from the viewer's own location.
        "date": today.isoformat(),
        "location": {"name": "Reference location (US East Coast)", "lat": LAT_DEG, "lon": LON_DEG},
        "reference_timezone": TZ_NAME,
        "reference_tz_abbr": midnight_local.tzname(),  # "EST" or "EDT", whichever is actually in effect today
        "computed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

    if cos_h0 < -1:
        result["status"] = "circumpolar"
        result["transit_utc"] = iso_utc(transit_local)
    elif cos_h0 > 1:
        result["status"] = "never_rises"
    else:
        h0_hours = math.degrees(math.acos(cos_h0)) / 15.0
        rise_elapsed = (transit_elapsed - h0_hours) % 24.0
        set_elapsed = (transit_elapsed + h0_hours) % 24.0

        result["status"] = "normal"
        result["rise_utc"] = iso_utc(midnight_local + datetime.timedelta(hours=rise_elapsed))
        result["transit_utc"] = iso_utc(transit_local)
        result["set_utc"] = iso_utc(midnight_local + datetime.timedelta(hours=set_elapsed))
        result["transit_altitude_deg"] = round(90 - abs(LAT_DEG - DEC_DEG), 1)
        result["visible_hours"] = round(2 * h0_hours, 1)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
        f.write("\n")

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
