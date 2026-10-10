# vso `data` branch

Generated data for vso.thgnetworks.com. Written ONLY by ebench (the single
writer), once per pipeline cycle. Never edit by hand and never merge into main:
the deploy workflow copies these files over the code checkout at build time.

- `data/tcrb_observations.json`
- `static/data/tcrb_rise_set.json`
- `static/exports/tcrb_latest24h.{json,csv}`

`.github/workflows/trigger-deploy.yml` starts the real deploy (on main) after each
data push. If it is edited, run `git pull --ff-only` on ebench before its next cycle.
