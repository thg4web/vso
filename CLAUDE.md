# CLAUDE.md -- VSO

## What This Is

Variable star observing, for real: the T Coronae Borealis "Blaze Star" nova
watch, and a sourced, attributed Seestar variable-star photometry manual.
Split out of `gen-astronomy` into its own standalone project once it outgrew
being a clubhouse page, with Lila, Pam, Sara, and Astrid.

**Working directory:** `/Users/wahender/My_Library/Tech/core-projects/astronomy-imaging/astronomy/vso/`
**GitHub:** `thg4web/vso` -- deploy key `~/.ssh/id_vso-deploy` (write access, used for the daily publish)
**Local home (ebench, data generation + LAN preview):** `/home/wahender/My_Library/Tech/core-projects/astronomy-imaging/astronomy/vso/`

---

## Team

| Name | Role Here | Profile | Pronouns |
|------|-----------|---------|----------|
| Lila | CEO, THG Media | `~/.claude/team/staff/lila.md` | She/Her |
| Pam | President, THG Media | `~/.claude/team/staff/pam.md` | She/Her |
| Sara | Executive Assistant, THG Media | `~/.claude/team/staff/sara.md` | She/Her |
| Astrid Star | Astro Imaging Lead, THG Media (ex-ZWO Seestar team) | `~/.claude/team/staff/astrid.md` | She/Her |

Same four people, same voices, same personalities as everywhere else.
Astrid naturally leads here -- this is her domain.

---

## Technical Stack

- **Framework:** Hugo 0.155.2 (extended, pinned) -- also confirmed building
  clean on 0.131.0 (ebench's older install); template avoids version-specific
  features for exactly that reason.
- **Theme:** none, ships its own minimal layouts + a dedicated dark
  "observatory console" theme for the T CrB page specifically.
- **Styling:** SCSS (compiled by Hugo)
- **Data:** real AAVSO API pulls (`scripts/`), not placeholders -- see
  `project/docs/` and the page itself for the full sourcing story.
- **Deployment:** ebench generates data + builds locally; publishes out to
  `thg4web/vso` on GitHub, served via GitHub Pages. Not yet wired up to a
  scheduled Action as of this writing -- see Open Items.

---

## Data Pipeline (all real, all sourced -- see the page for attribution)

- `scripts/fetch_tcrb.py` -- sparse daily AAVSO sample, feeds the chart.
- `scripts/export_tcrb_recent.py` -- full 24h raw observation pull.
- `scripts/compute_rise_set.py` -- rise/transit/set, pure spherical
  astronomy, no network call, run via cron at 12:01 AM.
- `scripts/aavso_common.py` -- shared token/band-mapping helpers.
- `AAVSO_API_TOKEN` lives in `.env` (gitignored, never committed, never in
  client-side code).
- `project/tools/seevar/` -- a third-party Seestar photometry pipeline
  (github.com/edjuh/seevar), cloned locally for evaluation. Gitignored
  entirely -- not ours to publish, and it ships a 250MB+ venv once set up.

---

## Standing Directives

- **No bad data.** Garbage in, garbage out -- a hard rule here, not a
  guideline. If a dataset has a known quality problem (see: the 2024 Alt/Az
  Seestar archive and its field-rotation issue), it doesn't get used until
  that's actually fixed, no matter how tempting the shortcut.
- **Attribute everything.** Real sources, real names, real dates. Where
  sources disagree, both sides go in rather than picking one.
- **Ready Room Meetings** doesn't apply here -- not a THG Media business
  project. All other voice/personality/standing directives from each team
  member's own profile still apply.

---

## Open Items

- GitHub Actions workflow for scheduled rebuild + publish not yet built.
- Public base URL / custom domain not yet decided -- `hugo.toml`'s
  `baseURL` is still `/`, fine for local/LAN, will need a real value before
  the GitHub Pages build goes live.
- `gen-astronomy`'s home page links out to `github.com/thg4web/vso` as a
  placeholder until the real public URL exists -- update that link once it
  does.
