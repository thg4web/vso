---
pdf: "/downloads/seestar-tcrb-photometry-guide-provisional.pdf"
title: "Provisional Seestar S30 Pro / S50 Pro T CrB Photometry Guide"
description: "A short, early how-to for getting good frames of T Coronae Borealis for photometry with a ZWO Seestar S30 Pro or S50 Pro: which stars to include, set-up, capture and a quick check. Provisional, and updated as we learn more."
keywords: ["Seestar T CrB photometry", "Seestar S30 Pro photometry", "Seestar S50 Pro photometry", "T CrB photometry guide", "Seestar variable star photometry", "Seestar app photometry mode", "Blaze Star photometry", "Seestar T CrB frames"]
---

<div class="callout callout--provisional">
<strong>Provisional, early days.</strong> Photometry with a Seestar is new: the app's Photometry mode only arrived in v3.4.0 (October 2026), and ZWO has not yet published how it works. This is a short guide to getting good frames, written from early tests with an S30 Pro. I will keep updating it as I get better information and more data, so expect the advice to change. <strong>Treat it as a starting point and check it yourself.</strong>
<br><em>First version: 19 October 2026. See the update log at the bottom.</em>
</div>

## What you need

- A Seestar **S30 Pro** or **S50 Pro** with a recent app. These steps come from an S30 Pro; the S50 Pro should be similar, but check each point on your own frames.
- **AAVSO's comparison stars** for T CrB, free from the AAVSO Variable Star Plotter.

## 1. Choose your stars

Open the AAVSO Variable Star Plotter, enter T CrB (chart X43296GGQ) and note the comparison stars close to T CrB's brightness, about magnitude 10 to 11. Stars **102, 106, 107 and 112** (V 10.17 to 11.17) work well. Avoid much brighter stars: they are too bright for the camera and give bad readings.

In the app's Photometry mode you can **select several stars at once**. Select T CrB and a few of those comparison stars, and the app records all of them in every frame.

## 2. Set up the Seestar

- **Use equatorial mode** and keep it the same every night.
- **Use short exposures.** 30 s works much better than 60 s, because at 60 s T CrB is often too bright for the camera (see step 4).
- **Pick one exposure and one gain for the night.** A gain set in the app beforehand may not take effect, so check the `GAIN` header on a frame afterwards.
- **Write down** the app version (it is not in the FITS headers), the date, the conditions (seeing, transparency, Moon), where you pointed, the exposure and the gain.

## 3. Take the frames

- **Take at least 15 frames,** and keep every individual sub-frame, not just the stack.
- **Finish with a short, non-enhanced stack.** You need it later to place stars on the frames. Don't use an AI-enhanced image for measuring: it is no longer linear.

## 4. Check your frames

**Is any star too bright?** Each pixel can only record so much light. When the brightest pixel in a star hits that limit it stops counting, so the star measures fainter than it really is. That ruins a measurement, and it's the most common problem with T CrB. You can check for it:

1. Open a frame in any viewer that shows pixel values.
2. Hover over the brightest pixel of T CrB, and then of each comparison star. Look only at the **green** pixels. The Seestar's sensor has red, green and blue pixels in a repeating pattern, and the `BAYERPAT` header tells you which are green (GRBG on the S30 Pro; the community reports BGGR for the original S50).
3. **If the number is above about 45,000, that star is too bright for this exposure.** (The camera's maximum is 65535, but the green pixels stop counting earlier, at about 48,000 to 49,000.) The fix is a shorter exposure.

**Is the header what you expect?** Check `GAIN` and `EXPTIME`.

**Anything odd in a frame?** Clouds, a passing light, a trail. Note it and leave that frame out.

## Keep your location private

FITS headers carry your observing latitude and longitude, and some JPGs carry GPS and an owner field with the same. Strip them before you share anything.

## Then measure, and where to get help

With good frames in hand, the next step is measuring the stars and reporting your results. You don't need special equipment or an assistant. These are good places to start:

- **AAVSO's [Getting Started](https://aavso.org/getting-started/) and [For New Observers](https://archive.aavso.org/new-observers) pages.** They have free guides, and AAVSO members can ask for a mentor.
- **[VPhot](https://vphot.aavso.org),** AAVSO's free online photometry tool. AAVSO observers report that it can take colour Seestar images and split them into separate red, green and blue (TR, TG, TB) images.
- **The AAVSO forum thread [Transforming and Uploading Seestar S50 Data](https://forums.aavso.org/t/transforming-and-uploading-seestar-s50-data-new-to-aavso/4664)**, written for people new to this. AAVSO's [Photometry with smart telescope](https://archive.aavso.org/photometry-smart-telescope) page is also worth reading.
- **The Seestar channel in AAVSO's community Slack,** where Seestar observers swap what they learn.
- **The [Seestar VSO Manual](/seestar-vso-manual/)** for our provisional measuring steps and the sourced community reports.
- **Your local astronomy club.** Someone there may already do photometry.

Some of these pages are a few years old, so check what's current before you rely on them.

## What is not known yet

- How the app chooses stars and calculates its numbers, and whether the saved frames are dark-subtracted. ZWO has not published this.
- How to change the gain for photometry, and how other gains behave.
- Whether the S50 Pro behaves the same way.

If you try this and get different results, or you know any of the answers above, I would like to hear about it, because that is how this guide gets better.

## Update log

- **19 October 2026:** first provisional version.
- **20 October 2026:** cut back to how to get good frames.

## Further reading

- AAVSO Variable Star Plotter (VSP), chart X43296GGQ, for the T CrB comparison stars.
- AAVSO, [Reporting Photometric Magnitudes](https://www.aavso.org/reporting-photometric-magnitudes).
- [Seestar VSO Manual](/seestar-vso-manual/): measuring steps and sourced community reports.
- [The T CrB page](/t-crb/): live data and the references behind it.
