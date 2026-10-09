---
title: "Seestar Variable Star Observing Manual"
description: "Real, sourced steps for doing variable-star photometry with a ZWO Seestar S50/S30 Pro, built from AAVSO's own docs and community reports."
---

**Status: first draft, building this out as we go.** Every claim here is attributed to a
real source — AAVSO's own documentation, or a named person in a public forum post, with
the date. Where sources disagree, both sides are here rather than picked for you. Nothing
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
  below that (cross-checked against Gaia DR2 by a Cloudy Nights user). Above it — don't
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
  T CrB's eclipsing-binary **orbital period as roughly 227 days** — a completely different
  number from, and not to be confused with, her ~80-year recurrent-nova eruption cycle.
  Stated informally in a student Q&A, not footnoted to a paper, so treat it as "worth
  verifying against a real catalog" rather than fully confirmed.
- Honest null result: they also tried Polaris as a target and got nothing useful — its real
  variability range (~0.07 mag) is smaller than their measurement precision can resolve.
  Their own words: "not variable enough." Good reminder that not every target is a fit for
  this gear, and that's a legitimate finding, not a failure.

## Two paths

### Path A — Quick: whole-image plate-solve, no differential setup

Reported by **arnaudfiocret** (AAVSO forum, Sep 2024):

1. Shoot your target with the Seestar as normal (stacked FITS).
2. Open the stack in **ASTAP**. It automatically recognizes variable stars in the field.
3. ASTAP photometrically calibrates the *entire image* via plate-solving — you don't set
   up comparison stars by hand.
4. Read the magnitude directly off the variable star it identified.
5. This only works on the **green layer (TG)** — but for casual LPV (long-period variable)
   monitoring, that's enough. Reported agreement: 0.05–0.1 mag vs. other observers in CCD
   Green or visual.

Good for: fast checks, long-period variables, beginners who don't want to build a
comparison-star workflow yet.

### Path B — Rigorous: differential photometry against AAVSO comp stars

1. Get the AAVSO-standard comparison star sequence for your target from their **Variable
   Star Plotter (VSP)** — never substitute a star you just happen to know.
2. Stack your Seestar subs (the native app does this).
3. Split into channels if your tool needs it. **The Seestar's Bayer pattern is BGGR —
   don't crop before extracting channels**, cropping shifts which pixels map to which
   color and breaks the math (community-derived transformation coefficients post, AAVSO
   forum, Jan 2024).
4. Run differential (or ensemble) aperture photometry: target vs. one or more comparison
   stars, same frame, same exposure.

**Easiest option — VPhot now handles Seestar files natively.** George Silvis (SGEO, AAVSO
staff), AAVSO forum, **April 19, 2024**: VPhot can demosaic Seestar color FITS directly
into separate TB/TG/TR images, no manual channel-splitting needed.
- Set a telescope profile with **plate scale 2.378**, mapping TB→B, TG→V, TR→R.
- Use **Quick Upload** so you can set the target name.
- Either Light (sub) frames or Stacked frames work.
- Problems: contact George via AAVSO Slack or gsilvis@aavso.org.
- Goal going forward is broader support for Unistellar, Dwarf, and DSLR color images too —
  not Seestar-only.

**Alternative — Phoranso** (by Tonny Vanmunster, free, cbabelgium.com — *not* "Peranso," an
earlier version of this manual had that wrong). Bikeman's actual worked T CrB
workflow, AAVSO forum, April 2024:
1. Convert the Seestar's OSC FITS to green-channel-only images (Bikeman used AstroArt;
   any FITS tool works — Fitswork is a free option).
2. Follow [Phoranso's own tutorial](https://www.cbabelgium.com/Phoranso/UserGuideHTML/html/Tutorial.html)
   — skip the calibration section, the Seestar's files are already calibrated.
3. Use [Phoranso's FITS Header Editor](https://www.cbabelgium.com/Phoranso/UserGuideHTML/html/FITSHeadereditor.html)
   to set the `FILTER` header to `"V"` on all images, so Phoranso calibrates against V
   comparison-star magnitudes.
4. In the generated report, replace `"V"` back with `"TG"` before submitting — same
   principle as MZK's rule below: calibrate with V, report honestly as TG.

Pablo Lewin (LPAC), AAVSO forum, May 2024, after getting direct help from Ken Menzies and
Tonny Vanmunster himself: calls Phoranso "my go to software," notes it can also mine *old*
data (exoplanet/NEO/asteroid images, even general astrophotos) for variables after the
fact, auto-requests an AUID when one doesn't exist yet, and has an "Advised Stars" fallback
for targets without an AAVSO comp-star sequence loaded.

**Other tools people are actually using for this step:**
- **AstroImageJ** — free, widely used, has a multi-aperture tool built for exactly this.
- **TychoTracker** — demilson (AAVSO forum, Aug 2025) used it with Python scripting for
  a 5-hour SX Phe (Delta Scuti) session.

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
coefficients for the Seestar S50 (official page, plus a community-derived set posted by
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
it's known to misbehave.

## Capture technique

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
