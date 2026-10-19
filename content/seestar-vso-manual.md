---
pdf: "/downloads/seestar-vso-manual.pdf"
title: "Seestar Variable Star Observing Manual"
keywords: ["Seestar photometry", "Seestar variable star", "Seestar S30 Pro photometry", "Seestar S50 photometry", "Seestar TG", "AAVSO Seestar", "variable star photometry", "variable star observing", "smart telescope photometry"]
description: "Variable-star photometry with a ZWO Seestar: AAVSO guidance and attributed community reports, plus our own provisional S30 Pro measuring steps, tested on T CrB."
---

**Status: first draft, building this out as we go.** Every claim here is attributed to a
real source — AAVSO's own documentation, or a named person in a public forum post, with
the date. Where we add our own measurements and steps (S30 Pro, T CrB, October 2026), they are
labelled as ours, are provisional, and are covered in more detail in the [provisional T CrB photometry guide](/seestar-tcrb-photometry-guide/). Where sources disagree, both sides are here rather than picked for you. Nothing
below is invented; if a step isn't sourced yet, it isn't in here yet.

---

## Is this realistic?

Yes, with real limits worth knowing up front:

- **Precision**: beginner-level work with careful technique lands around **0.05–0.1 mag**
  agreement against other observers (arnaudfiocret, AAVSO forum, Sep 2024, using ASTAP +
  the green channel). That's good enough to track real variability in stars with an
  amplitude of a few tenths of a magnitude or more — not good enough to chase
  millimagnitude transits.
- **Saturation**: the Seestar's sensor saturates around **V ≈ 8**. Linear and well-behaved
  below that (cross-checked against Gaia DR2 by a Cloudy Nights user). *Our own S30 Pro frames
  (Oct 2026, 30 and 60 s at gain 200) add a nuance: the red and blue pixels reached 65535 on stars
  of V 7.9 to 9.3, while the green pixels topped out near 48,000 to 49,000 for all of them, a soft
  ceiling below 65535 (a reader who examined our files pointed this out). It depends on the
  channel, exposure, gain and model, so check the pixel values in your own frames.* Above it — don't
  trust the numbers. Independently reported by multiple people (see the SUNY
  Dutchess/MHAA project below) — this is a real, recurring limit, not a one-off.
- **Field rotation** used to be a real problem for long time-series runs in the Seestar's
  native alt-az mode. Andrew Pearce (AAVSO forum, Aug 2025) calls **EQ mode** "a key
  enabler" that removed this as an issue entirely.

## It's already been done, on T CrB specifically

**Bikeman** (British Astronomical Association, Variable Star Section — BAA-VSS), AAVSO
forum, **April 12, 2024**: picked T CrB as a target specifically *because* it was sitting
around V≈10 at the time — "a sweet spot for the S50... not too bright, not too faint" —
and noted the ongoing campaign watching for her next eruption. By averaging **10×10s
subs**, got down to a standard deviation of about **0.01 mag in TG**. Results are in the
AAVSO light curve under **observer code EHEA**, date **2024-04-10**.

That's direct precedent: someone already ran this exact playbook, on this exact star, with
this exact scope, and it worked. Worth pulling up EHEA's AAVSO submissions as a reference
point for what a clean run looks like.

**A second, ongoing real project**: Leonides Lopez and Maria Garcia Martinez, students at
SUNY Dutchess, presented a status report to the **Mid-Hudson Astronomical Association**
(MHAA) in April 2026 — the fifth in a line of MHAA student experiments specifically testing
whether a Seestar S50 is viable for at-home variable star research. They've been tracking
T CrB continuously since **June 20, 2025** (a baseline started by their advisor, Dr.
Myers), alongside Polaris and a couple of other targets, using AstroImageJ. Source: ["Variable
Star Photometry & T CrB Nova Watch with the Seestar
S50"](https://www.youtube.com/watch?v=m1aasfGGWE4), MHAA YouTube, Sep 2026. (It's an
auto-captioned transcript — the numbers and names below came through clearly, a couple of
other star names did not and aren't repeated here.)

What they found, worth knowing before you start:
- Checked their AstroImageJ-derived T CrB magnitudes against AAVSO's published community
  data over their observing baseline: **average percent error 0.845%**, best case 0.15%,
  worst case 1.65% on one specific day. Independent confirmation this approach gets you
  genuinely close to the crowd-sourced consensus.
- **Hit the same saturation problem independently** — AstroImageJ flagged "oversaturated"
  stars on some of their stacks (sometimes a soft yellow warning, sometimes a hard error),
  and they hadn't fully root-caused whether it was an AstroImageJ setting or a genuine
  Seestar limit by the time of this talk. Their advisor separately found Vega itself "too
  darn bright" to use and had to pick dimmer stars nearby instead. Three independent
  reports of saturation trouble now (this one, Bikeman's V≈8 ceiling, and the general
  forum discussion) — treat it as a real, recurring limit, not a fluke.
- **Pointing drift fix**: when the Seestar wouldn't stay pointed at their actual target,
  they'd manually resync on **Polaris** first (fixed, never moves, so the scope "knows
  exactly where it is" again) before re-slewing to the variable star.
- They sourced comparison-star magnitudes from **both Stellarium and AAVSO's own
  comparison-star sequence charts** — two independent cross-checks rather than trusting
  one source blind.
- When graphing in Excel, they **reverse the Y-axis** specifically to match AAVSO's own
  light-curve convention (brighter = up) — exactly the same choice this project's own T CrB
  chart already makes.
- They explicitly **excluded AAVSO's "Fainter-than" flagged points** from their comparison
  data, since those are upper-limit non-detections that don't represent a real measured
  brightness — also exactly how this project's own data pipeline already treats
  `fainter_than` observations.
- One fact worth folding into the T CrB page itself at some point: in the Q&A, they cited
  T CrB's **orbital period as roughly 227 days** — a completely different number from, and
  not to be confused with, her ~80-year recurrent-nova eruption cycle. This checks out: Schaefer
  (2023, MNRAS 524, 3146) gives an orbital period of 227.5687 ± 0.0099 days.
- Honest null result: they also tried Polaris as a target and got nothing useful — its real
  variability range (~0.07 mag) is smaller than their measurement precision can resolve.
  Their own words: "not variable enough." Good reminder that not every target is a fit for
  this gear, and that's a legitimate finding, not a failure.

## The app's Photometry mode (v3.4.x): what it is and is not

The Seestar app gained a Photometry mode in v3.4.0 (October 2026). It writes a CSV per frame and a
summary CSV with the star's position, `Mag(obs)`, `Mag(err)` and SNR. What we found on the S30 Pro
(measured from our own files, October 2026):

- **Its magnitude is not V.** On T CrB (a red star) it read about 9.2 while AAVSO observers reported
  about 10.0: roughly 0.8 to 1.1 magnitude too bright. Which band and catalogue it uses is not documented.
- **`Mag(err)` is not photon noise** (0.19 reported where the noise alone gives about 0.017). On our
  files it is mostly the scatter of the app's own reference stars: one clipped bright reference (catalogue
  magnitude 3.76, measured about 2.5 magnitudes too faint) dominates it, and when that star dropped out of
  4 of 35 frames the error fell to 0.07 to 0.08 and T CrB's app magnitude moved 0.2 to 0.3 fainter. The app's
  magnitude therefore depends on which references it happens to use.
- **ZWO has not published how it works.** The v3.4.0 and v3.4.1 release notes say only "Added
  Photometry" and that the dark-frame library workflow changed. Whether the saved frames are
  dark-subtracted is unknown.
- **Use it to identify the star and to get pixel positions**, not for the magnitude. The `X Axis` and
  `Y Axis` columns are 1-based pixel positions in the raw frame (we verified that the pixel peaks sit at X−1, Y−1).
- It has also been reported that Photometry mode can measure several targets in one session. We have not tried it.

## Our Seestar photometry steps (provisional)

**These steps are ours, from two test nights on one telescope, and they are early.** We tested them on
a Seestar **S30 Pro** (telephoto camera, IRCUT filter, equatorial mode, gain 200, app v3.4.0) on the red
recurrent nova T CrB. They should carry over to other targets and to the S50 and S50 Pro, but we have not
tried that, so check each point on your own frames. The worked numbers, and what is still unknown, are in
the [provisional T CrB photometry guide](/seestar-tcrb-photometry-guide/). We will revise this section as
we learn more.

**Before the session**

1. **Get AAVSO's comparison stars.** Fetch the comparison sequence for your target from AAVSO's Variable
   Star Plotter (VSP) and write down each star's AUID and V magnitude. Never substitute a star you merely
   know. Pick comparison stars within about one magnitude of your target, not much brighter (bright stars
   saturate and force a long extrapolation). For T CrB (V about 10) we used chart X43296GGQ, stars V 10.17,
   10.55, 10.74 and 11.17.
2. **Use equatorial (EQ) mode** and keep it the same every night. Alt-az rotates the field during an
   exposure; we have not tested it. The FITS keyword `EQMODE` records the mode.
3. **Choose one exposure and one gain for the whole night.** Set the gain before you enter Photometry
   mode. Choose them so that your target and comparison stars stay below the ceiling in the channel you will
   measure: 65535 for red and blue, but only about 45,000 for green, which saturates near 48,000 to 49,000
   (as a starting point, a brightest pixel of 30,000 to 40,000; this is a suggestion, not tested).
4. **Record** the app version (it is not in the FITS headers), the date, conditions (seeing, transparency,
   Moon), exposure, gain and mount mode.

**At the telescope**

5. **Take at least 5 individual sub-frames; 15 or more is better** so you can see the scatter. Keep every sub:
   the stack hides per-frame problems.
6. **Save a short, non-enhanced stack at the end.** You need it to place stars on the frames. Do not use an
   AI-enhanced image for measuring: it is stretched and denoised, so it is no longer linear.

**Measuring**

7. **Work on the raw FITS** (16-bit, `BITPIX 16`, `BZERO 32768`). Do not debayer. Read the `BAYERPAT` header:
   our S30 Pro frames read **GRBG** (checked against the star signals); the community reports the original
   S50 as BGGR, so check yours, and do not crop before you separate the colour planes.
8. **Measure the green pixels only.** On our frames the red and blue pixels reached 65535 on bright stars
   while the green pixels topped out near 48,000 to 49,000, so green gives more room than red or blue, but it
   still saturates below 65535. Place the target and each
   comparison star on every frame (we fit the app's per-frame CSV positions to RA and Dec, then re-centre each
   star with a centroid), then do aperture photometry: radius 5 pixels, sky as the median of an annulus from
   9 to 14 pixels, flux as the sum of (pixel − sky). The S30 Pro's plate scale is about 3.7 arcseconds per pixel
   (2.9 µm pixels, 160 mm focal length, 3.67 measured).
9. **Reject saturated stars.** In the red and blue planes treat any pixel at 65000 or more as clipped; in the
   green plane treat about 45,000 or more as saturated, because the green peaks of stars of very different
   brightness pile up at about 48,000 to 49,000 (a soft ceiling). Apply this to the target and every comparison
   star. If a star saturates, drop it or shorten the exposure. Dropping our near-ceiling T CrB frames moved the
   result by 0.015 magnitude or less.
10. **Calibrate each frame.** The zero point is the median of (catalogue V − instrumental magnitude) over your
    comparison stars. Then check it: treat each comparison star in turn as the unknown and see whether you
    recover its catalogue value (we got within about 0.02 to 0.05 magnitude). A star that does not recover its
    value means the night is not usable. Confirm the zero point is steady across frames and that flux scales with
    exposure time (60 s against 30 s gave a ratio of about 2.0).
11. **Combine the frames** and report the mean with its scatter.

**The colour problem**

12. **A red star measured against bluer comparison stars reads too bright.** T CrB is far redder than any
    AAVSO comparison star in its field, and the green channel measured against V comparison stars read about
    0.06 to 0.3 magnitude too bright. If your target is much redder (or bluer) than your comparison stars,
    correct for colour. Our method: use Gaia DR3 stars in the same field, find how the instrumental green
    magnitude relates to Gaia colour (BP−RP), apply it to the target's Gaia colour, and convert Gaia G to V with
    the relation in the Gaia documentation (we checked it against AAVSO's V for eight comparison stars: root-mean-square
    0.025). On our two T CrB nights this gave V between 10.06 and 10.33 (night 1) and between 10.09 and 10.31
    (night 2), with a systematic uncertainty we put at about ±0.2 magnitude. The red end is the weak spot:
    very few calibration stars are as red as T CrB.

**Reporting**

13. **Call it TG.** A green-channel measurement calibrated against V comparison stars, without a
    transformation, is reported to AAVSO as **TG**, not V (see "What to call your band" below). Read the current
    AAVSO pages before your first submission. We have not submitted anything yet.

**Quality checklist before you trust a night:** no saturated pixels in the target or any comparison star, in the
measured channel (for green, no peak above about 45,000); at least one comparison star recovered within its expected error; a steady zero point; at
least 5 frames; your colour correction stated with its uncertainty; and your location removed from anything you
share. FITS headers carry your observing latitude and longitude, and some JPGs carry GPS and an owner field
with the same.

## What to call your band (important — don't mislabel this)

The Seestar's native R/G/B channels, **reported untransformed**, are AAVSO's **TR / TG /
TB** bands (Tri-Color Red / Green / Blue — these are real AAVSO band codes, not a Seestar
invention).

**MZK's rule** (AAVSO forum, Sep 2024): *"If your camera image has a TG bayer filter
channel, report your magnitude as TG but use the known V comparison star magnitudes for
untransformed photometry."* — i.e. it's fine to measure against V-magnitude comp stars
without deriving a full transformation, as long as you're honest that your result is TG,
not true V.

**If you want closer-to-standard V/B/R**, apply AAVSO's own BVR transformation
coefficients for the Seestar S50 (S50 only: they do not carry over to the S30 Pro or S50 Pro without checking) (official page, plus a community-derived set posted by
Andrew Pearce with R² near 0.99 from the NGC 3532 standard field — worth having both to
cross-check).

**Known color problems, reported directly, not smoothed over** (Bikeman, AAVSO forum, Sep
2024, observing a nova in Vulpecula):
- **TR** (red channel): results looked "ok-ish."
- **TG** (green channel): scattered a lot for this particular target — likely because the
  object was red with emission concentrated near the edge of the green filter's band
  (probably H-alpha). TG is not universally reliable; it depends on your target's color
  and spectrum.
- **TB** (blue channel): internally consistent with other observers' blue measurements,
  but "very much off" compared to true Johnson B.

**Takeaway**: TG is the most commonly used and generally most reliable channel, but check
your specific target isn't a case (very red, strong narrow emission near 500-560nm) where
it's known to misbehave. *A very red star without strong emission lines also needs care: on two
October 2026 S30 Pro nights, T CrB (a red giant) measured in the green channel against V
comparison stars read brighter than its true V, by roughly 0.06 to 0.3 magnitude, until we added a
Gaia colour correction. Details and caveats are in the
[provisional T CrB guide](/seestar-tcrb-photometry-guide/).*

## Capture technique

- **Several targets in one session — reported, not yet tried here.** It has been reported
  that the Seestar app's Photometry mode lets you select more than one target to measure in
  the same session. We have not tried this and do not yet have the original source for the
  report, so treat it as unconfirmed until we do.
- **Use EQ mode** for anything longer than a quick check — kills field rotation, which
  otherwise ruins long time-series photometry (Andrew Pearce, Aug 2025).
- **Average multiple short subs per data point**, don't rely on single frames. kb0fhp
  (AAVSO forum, Aug 2025) uses groups of 12–18 subs at 20s each (240–360s total) per
  point — "lets me see a little deeper, and reduces the noise in the data," from a Bortle
  7 (light-polluted) backyard.
- **More averaging reduces scatter in the light curve itself**, but doesn't necessarily
  improve derived quantities like time-of-maximum in a polynomial fit — Roy Axelsen (AAVSO
  forum, Mar 2026) ran this as a real experiment on a Delta Scuti star and found the fit
  error was about the same either way, even though the averaged curve looked visually
  cleaner. One run, not a broad study — worth keeping in mind rather than assuming "more
  averaging = more precise" unconditionally.
- **Take flat frames** — the native Seestar app gained this capability at some point before
  Aug 2025 (Andrew Pearce), along with a **planning mode** that lets you set up an
  all-night unattended run.

## Automation / control software

- **seestar_run** — Python batching script. Andrew Pearce used this for 10-11 hour
  unattended all-night runs (Jul 2024 post) and, as of Aug 2025, still calls it sufficient
  for his needs even after seestar_alp matured.
- **seestar_alp** — broader control software. Andrew had trouble getting it working as of
  Sep 2024; by Aug 2025 he reports it's become his "go to software to control the Seestar."
  Software that was rough a year ago may be solid now — check current state before
  dismissing it.

## Good first targets to practice on

Andrew Pearce's method (Smart Telescope Underworld, Jul 2024): search AAVSO's **VSX** for
stars in your scope's clean brightness range, with periods under 4-6 hours and amplitude
0.4-0.5 mag. Delta Scuti variables (short-period pulsators) fit this well — his example
was **EH Lib**, amplitude ~0.5 mag, period ~2 hours, clean light curve from a single
night's run.

T CrB herself isn't a good *practice* target by this method — her "period" is a human
lifetime, not a few hours — but these short-period stars are a good way to build skill and
confidence on the workflow while you wait on her.

## Further resources

- Andrew Pearce's YouTube video, **"Doing Science with the Seestar S50"** — covers
  photometry and astrometry of variable stars, comets, and asteroids.
- demilson's YouTube videos: **"SX Phe: 5-Hour Loop of a Delta Scuti Star's Pulsations and
  Light Curve"** and **"SS S50: Comet C/2025 K1 (Atlas)."**
- AAVSO forum thread this manual draws from: **"Using the ZWO Seestar S50 for
  photometry"** (Technology → Instrumentation & Equipment category).
- AAVSO's **DSLR Observing Manual** — the Seestar is treated like a one-shot-color DSLR for
  photometry purposes, so this is the underlying reference.

---

*Built from real forum posts and AAVSO documentation, attributed and dated. If you find
something that updates or contradicts a claim here, bring it back and we'll fix the page,
not just add to it.*
