---
pdf: "/downloads/seestar-tcrb-photometry-guide-provisional.pdf"
title: "Provisional Seestar S30 Pro / S50 Pro T CrB Photometry Guide"
description: "An early, provisional guide to measuring T Coronae Borealis with a ZWO Seestar S30 Pro or S50 Pro: what the app's Photometry mode does, what we measured, the red-star problem, and what is still unknown. Updated as new data arrives."
keywords: ["Seestar T CrB photometry", "Seestar S30 Pro photometry", "Seestar S50 Pro photometry", "T CrB photometry guide", "Seestar variable star photometry", "Seestar TG", "Seestar app photometry mode", "Blaze Star photometry"]
---

<div class="callout callout--provisional">
<strong>Provisional, early days.</strong> Photometry with a Seestar is new: the app's Photometry mode only arrived in v3.4.0 (October 2026), and ZWO has not yet published how it works. Everything here comes from two test nights, on one telescope, by one observer. I will keep updating this guide as I get better information and more data, so expect numbers and advice to change. <strong>Treat it as a starting point and check it yourself.</strong>
<br><em>First version: 19 October 2026. See the update log at the bottom.</em>
</div>

## What this guide covers, and what it does not

- **Tested on:** a Seestar **S30 Pro** (telephoto camera, built-in IRCUT filter, equatorial mode, gain 200), app v3.4.0 (night 2: v3.4.0 or v3.4.1, not confirmed), on **T Coronae Borealis** (the Blaze Star), two nights in October 2026.
- **Not tested:** the **S50 Pro**, the original S50, alt-az mode, other gains, other targets. The S50 Pro should follow the same workflow, but its colour response may differ, so repeat the checks below before trusting any number. For community results on the original S50, see the [Seestar VSO Manual](/seestar-vso-manual/).
- **Not done:** nothing here has been submitted to AAVSO, and these measurements are not the AAVSO data plotted on the [T CrB page](/t-crb/). The only numbers shown there come from AAVSO's accepted observations.

## 1. Why T CrB is a hard target for a Seestar

1. **It is very red.** T CrB is a red giant paired with a white dwarf (Gaia colour BP−RP about 2.3). Most comparison stars are much bluer, and a colour camera sees red stars brighter than a standard V filter would.
2. **The Seestar is a one-shot colour camera behind a built-in IR-cut filter.** There is no filter wheel, and the real colour response of the whole system has not been published.
3. **The star is about magnitude 10 now but could reach about 2 within hours of an eruption** ([see the references on the T CrB page](/t-crb/#references)). The settings that work at 10 will saturate on a bright star.

## 2. What the app's Photometry mode gives you (v3.4.x)

The app writes a CSV per frame (and a summary CSV), with the star's name, position, `Mag(obs)`, `Mag(err)`, SNR and the exposure times. It recognised T CrB as "Blaze Star" (from the fourth frame on the first night, from the first frame on the second).

What we found, measured from the files:

- **The app's magnitude is not V.** It reported about **9.2** for T CrB while AAVSO observers reported about **10.0**. For a red star the app reads roughly **0.8 to 1.1 magnitude too bright**. We do not know which band or catalogue it uses.
- **`Mag(err)` is not photon noise; it is mostly the scatter of the app's own reference stars.** For a frame with SNR 62.7, noise alone would give about 0.017 mag, but the app reported 0.19. On our files it is reproduced to within about 0.001 by √[(s/√N)² + (1.0857/SNR)² + 0.01²], where s is the scatter of (app magnitude − catalogue magnitude) over the N = 15 reference stars. One of those reference stars (catalogue magnitude 3.76) is clipped and was measured about 2.5 magnitudes too faint, so it dominates s. In 4 of our 35 frames it dropped out of the reference set: the error fell from about 0.17 to 0.20 down to 0.07 to 0.08, and the app's magnitude for T CrB moved about 0.2 to 0.3 fainter. So the error does not say how well the star was measured, and the app's magnitude depends on which references it happens to use. *(A reader who reviewed our files suspected the reference stars; we then reproduced the result ourselves.)*
- **ZWO has not documented it yet.** The release notes for 3.4.0 and 3.4.1 say only "Added Photometry" (and that the dark-frame library workflow changed). The catalogue, the measured colour channel, the CSV columns and the error calculation are not described. Questions have been put to ZWO; there has been no reply.
- **Whether the saved frames have the dark library applied is unknown.** The FITS headers have no keyword for it.

**Bottom line:** use the app's CSV to identify the star and as a rough guide, but do your own measurement against proper comparison stars if you want a number you can trust.

## 3. Setting up the session

- **Use equatorial mode** and keep it the same every night. (Alt-az rotates the field during an exposure. We have not tested it.) The FITS header keyword `EQMODE` records the mode.
- **Pick one exposure and one gain for the whole night.** The app does not appear to offer a gain setting inside Photometry mode, so set the gain *before* you enter it.
- **Mind the clipping.** The raw frames are 16-bit (2160 × 3840), so 65535 is the ceiling.
  - At **60 s, gain 200** T CrB's *red* pixels reached the 65535 ceiling in 12 of 15 frames. The *green* pixels never reached 65535, but green saturates much lower, at about 48,000 to 49,000 (next point).
  - At **30 s, gain 200** the red pixels clipped in 7 of 20 frames, and the app's frame-to-frame scatter roughly halved (0.155 to 0.077).
  - **Staying below 65535 does not mean the green pixels were unsaturated.** The green peaks of very different stars (V 7.9 to 9.8) all sit at about **47,600 to 49,500**, and the largest green value anywhere in a frame is about 51,000 to 51,800, a soft ceiling well below 65535, while red and blue reach 65535. A reader who examined our files pointed this out, and our measurements confirm it. We now treat a green peak above about **45,000** as saturated. T CrB itself reached that level in 9 of 15 frames on night 1 and 5 of 20 on night 2. Dropping those frames, and any comparison star above it, changed our results by 0.015 magnitude or less (section 5). An eruption to magnitude 2 would saturate it badly, so you would need much shorter exposures then.
  - As a starting point, aim for the star's brightest pixel at roughly 30,000 to 40,000 (my suggestion, not tested). Other gains are untested so far.
- **Keep every individual sub-frame**, not just the stack. The stack hides per-frame problems.
- **Save a short, non-enhanced stack at the end of the session.** You need it later to place stars on the frames. Do not use an AI-enhanced image for measurement: it is stretched and denoised, so it is no longer linear.
- **Write down** the app version, date, conditions (seeing, transparency, Moon), exposure, gain and mount mode. The app version is *not* in the FITS headers.
- **Check your files before sharing them.** FITS headers carry your observing latitude and longitude, and some JPGs carry GPS and an owner field with the same. Strip them before you send anything to anyone.

## 4. Measuring it yourself

1. **Use AAVSO's comparison stars, not the app's reference stars.** The app's references are mostly brighter than T CrB and clip. AAVSO's sequence for T CrB (chart X43296GGQ) has comparison stars 102, 106, 107 and 112 (V = 10.17 to 11.17); in the green pixels, 106, 107 and 112 stayed well below 45,000 and 102 came near it in 2 of 15 frames on night 1. Stars 79, 84 and 93 (V 7.9 to 9.3) clipped in their red pixels in nearly every frame, and their green peaks all sat at the same soft ceiling of about 48,000 to 49,000, so do not use stars like them.
2. **Work on the raw frames** and measure each Bayer channel separately. We used the **green** pixels. On our S30 Pro frames the pattern is **GRBG** (the `BAYERPAT` header, confirmed from the star signals; community posts about the original S50 report BGGR, so check your own header and do not crop before splitting the channels): small circular aperture (radius 5 pixels; the S30 Pro's plate scale is about **3.7 arcseconds per pixel**, from the FITS header's 2.9 µm pixels and 160 mm focal length, and 3.67 measured from the app's star positions), sky from the median of an annulus (9 to 14 pixels), flux as the sum of pixel minus sky. In the red and blue planes count any pixel at 65000 or more as clipped; in the green plane treat about 45,000 or more as saturated (section 3).
3. **Calibrate each frame** with a zero point from the comparison stars (the median of catalogue minus instrumental), then check it by treating each comparison star as the unknown and recovering its catalogue value. Ours recovered to within about 0.02 to 0.05.
4. **Check scaling.** Raw flux should scale with exposure time. We found about a factor of 2.0 between 60 s and 30 s frames (two different nights, so approximate), which is what you want.
5. **Call it what it is.** Green-channel values calibrated against V comparison stars are reported to AAVSO as **TG** (untransformed). AAVSO guidance, as we read it, is to report the green channel as TG and not to transform TB or TR for a nova. Please read the current AAVSO pages yourself before a first submission (see the references).

## 5. The red-star problem, and our early numbers

Measured against bluer comparison stars, a very red star reads too bright. We corrected for this with **Gaia DR3** colours: stars in the same field with known Gaia colours show how the green channel responds to colour, and T CrB's colour gives the correction. This works, but it is the weakest link (very few calibrators are as red as T CrB).

| | Night 1: 17 Oct 2026 (60 s, 15 frames) | Night 2: 18 Oct 2026 (30 s, 20 frames) |
|---|---|---|
| App's own magnitude (mean) | 9.16 | 9.19 |
| Green channel against V comparison stars (TG-style) | 9.999 ± 0.036 | 9.963 ± 0.036 |
| With the Gaia colour correction (V, a range from different fits) | 10.06 to 10.33 | 10.09 to 10.31 |
| T CrB red pixels at the ceiling | 12 of 15 frames | 7 of 20 frames |
| T CrB green peak above about 45,000 (near the green ceiling) | 9 of 15 frames | 5 of 20 frames |
| Green (TG-style) using only frames where T CrB and the comparison stars are below that | 9.985 ± 0.015 (6 frames) | 9.957 ± 0.033 (15 frames) |
| AAVSO observers that UT day | visual 10.0 to 10.56 | V about 10.02 (two observers), visual 10.0 to 10.39 |

- **The near-ceiling frames barely matter:** dropping them moves the green result by 0.014 magnitude (night 1) and 0.006 (night 2).
- **Systematic uncertainty is about ±0.2 magnitude.** Frame-to-frame scatter is only about 0.04, but the colour correction dominates.
- **Night 2 is a weaker colour calibration than night 1.** I had no stack from that night, so only about 60 calibration stars matched (none redder than a colour index of 1.6), against about 360 on night 1. A same-night stack matters.
- **Conditions:** night 2 had above-average transparency and average seeing. I did not record night 1's sky.
- Both nights agree with AAVSO's values to within the uncertainty, and neither showed any sign of brightening.

## 6. A quality checklist before you trust a night

- No saturated pixels in the target or any comparison star, in the channel you measure (for green, no peak above about 45,000).
- At least one comparison star recovered within its expected error.
- Zero point steady across frames.
- At least 5 frames (15 or more is better so you can see the scatter).
- Your colour correction is stated, along with its uncertainty.
- Location removed from anything you share.

## 7. What is still unknown

- How the app chooses the target and reference stars, which catalogue and band it uses, and how it computes `Mag(err)` (asked of ZWO).
- Whether the saved frames are dark-subtracted. The saturated green peaks vary by about ±1,000 around 48,000 to 49,000 instead of sitting at one value, which may hint at processing before saving, but we cannot tell.
- The S30 Pro's real colour response, which ZWO has not published.
- Whether a lower gain clips less and measures better (other gains are untested so far).
- Whether the S50 Pro behaves the same way.
- How good the colour calibration can get: more red calibration stars and a same-night stack help.

If you try this and get different numbers, or you know any of the answers above, I would like to hear about it, because that is how this guide gets better.

## Update log

- **19 October 2026:** first provisional version, from two test nights (17 and 18 October 2026, S30 Pro).
- **19 October 2026 (later):** corrected two points after a reader reviewed our files. The green channel does saturate, at about 48,000 to 49,000, well below 65535 (the first version said it never clipped). And the app's `Mag(err)` is mostly the scatter of its own reference stars, driven by one clipped bright star, not photon noise.

## References and further reading

- AAVSO, [What is Tri-G magnitude?](https://www.aavso.org/what-tri-g-magnitude) and [Reporting Photometric Magnitudes](https://www.aavso.org/reporting-photometric-magnitudes): how TG is defined and reported. *(Summarised from search results; AAVSO's pages could not be fetched automatically, so read them directly.)*
- AAVSO, [BVR transformation coefficients for the Seestar S50](https://archive.aavso.org/node/90658): published for a different camera. Do not copy them to the S30 Pro or S50 Pro.
- AAVSO, [Smart telescopes (Unistellar, Seestar, Dwarf)](https://www.aavso.org/smart-telescopes-unistellar-evscopeequinox-seestar-dwarf).
- AAVSO Variable Star Plotter (VSP), chart X43296GGQ, for the T CrB comparison sequence.
- Gaia Collaboration, *Gaia* Data Release 3, via the ESA Gaia archive: field-star colours and the G-to-V relation used here.
- The T CrB facts and the references behind the [T CrB page](/t-crb/#references): Schaefer 2023 (MNRAS 524, 3146) and Merc et al. 2025 (MNRAS Letters 541, L14).
- ZWO Seestar app release notes, v3.4.0 and v3.4.1 (App Store version history).
- [Seestar VSO Manual](/seestar-vso-manual/): sourced community reports on Seestar photometry.
