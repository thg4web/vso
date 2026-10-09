# THG Media — Project Document Templates

**Purpose:** Five standard documents every THG Media project gets at deployment. Copy each section into the target file, replace the `{{PLACEHOLDER}}` variables, and customize to fit the project.

**Placeholders used throughout:**

| Placeholder | Example | Notes |
|-------------|---------|-------|
| `{{PROJECT_NAME}}` | Parallax | Display name of the project |
| `{{DESCRIPTION}}` | Dual-model AI verification tool | One-line summary |
| `{{WORKING_DIR}}` | `/Users/wahender/My_Library/Tech/thg-media/parallax/` | Absolute path |
| `{{DOMAIN}}` | ownyourcomputeragain.org | Production domain, if applicable |
| `{{DATE}}` | 2026-05-29 | Date the document is created |
| `{{AUTHOR}}` | Aaron Henderson, with THG Media team | Primary author(s) |
| `{{VERSION}}` | 0.1 | Starting version |
| `{{STATUS}}` | Active Development | Current project status |
| `{{TEAM_TABLE}}` | *(see each template)* | Project-specific team roster |
| `{{TECH_STACK}}` | Hugo 0.155.2, Python 3.14, etc. | Major technologies |
| `{{PALETTE_TABLE}}` | *(see design template)* | Color palette rows |
| `{{TYPOGRAPHY}}` | *(see design template)* | Font selections |
| `{{FILE_TREE}}` | *(see inventory template)* | Complete file listing |

**File destinations:**

| Document | Target Path |
|----------|-------------|
| README.md | `Project root/README.md` |
| Meeting Notes | `project/meetings/YYYY-MM-DD-topic.md` |
| Technical Design | `project/design/technical-design.md` |
| Planning & Roadmap | `project/docs/planning-roadmap.md` |
| All Files Inventory | `project/docs/all-files.md` |
| Project Memories | `project/memories/` (one fact per file) |

---
---

# 1. README.md

> **Destination:** `{{WORKING_DIR}}README.md`

```markdown
# {{PROJECT_NAME}}

{{DESCRIPTION}}

**Project:** THG Media
**Author:** {{AUTHOR}}
**Status:** {{STATUS}}
**Version:** {{VERSION}}

---

## Purpose

What this project does, why it exists, and who it serves. Keep it to a paragraph or two. If you can't explain it simply, the scope might need tightening.

---

## Scope

What's included and, just as importantly, what's not. Draw the boundaries early.

### In Scope

- Item one
- Item two

### Out of Scope

- Item one
- Item two

---

## Methodology

How the project is built, what frameworks or approaches drive it, and any conventions the team should know before diving in.

---

## Team

{{TEAM_TABLE}}

Adjust roles as the project evolves. Team members are listed in `~/.claude/team/staff/`.

---

## Technical Stack

{{TECH_STACK}}

---

## Build & Run

```bash
# Local development
./start_webserver.sh

# Production build
hugo --minify --gc
```

Adjust commands to match the project's actual toolchain.

---

## Update & Deploy

Describe the deployment pipeline. For Hugo projects, this is typically GitHub Actions to GitHub Pages. For tools, it might be a manual process or a script.

---

## Project Structure

```
content/             Page content
layouts/             Templates and partials
assets/scss/         Stylesheets
static/              Images, PDFs, static files
data/                Data files
project/docs/        Project documentation
project/design/      Design files
project/meetings/    Meeting notes
project/memories/    Project memories (one fact per file) — canonical save location
```

---

## Key Documents

- **CLAUDE.md:** Project instructions and standing directives
- **Technical Design:** `project/design/technical-design.md`
- **Planning & Roadmap:** `project/docs/planning-roadmap.md`
- **All Files Inventory:** `project/docs/all-files.md`
- **Project Memories:** `project/memories/` — canonical save location for all project memories (one fact per file; frontmatter `name`/`description`/`metadata.type`). Add a **Project Memories** standing directive to the project CLAUDE.md.

---

## Standards

All THG Media projects follow the Web Publishing Best Practices document at `project/docs/web-publishing-best-practices.md` in the parent repository. Standing directives from the parent THG Media CLAUDE.md carry forward.

---

*THG Media — The Henderson Group*
*Founded April 1, 2025. Not a joke.*
```

---
---

# 2. Meeting Notes

> **Destination:** `project/meetings/YYYY-MM-DD-topic.md`
> **Naming convention:** Date first, then a short topic slug. Example: `2026-05-29-kickoff.md`

```markdown
---
title: "{{PROJECT_NAME}} — {{MEETING_TITLE}}"
date: {{DATE}}
location: "The Ready Room, 123 Prosperity Way, Asheville, NC"
present:
  - "Aaron Henderson"
  - "Pam Simpson"
  - "Lila"
preceding: "{{PRECEDING_MEETING_REF}}"
description: "{{MEETING_DESCRIPTION}}"
status: complete
maintained_by: "Sara Johansen, Executive Assistant"
---

# {{PROJECT_NAME}} — {{MEETING_TITLE}}

**Date:** {{DATE_DISPLAY}}
**Location:** The Ready Room, 123 Prosperity Way, Asheville, NC

---

## Context

Why this meeting happened. What prompted it, what the team needed to resolve or advance. A sentence or two sets the stage.

---

## Overview

Summary of what was discussed and accomplished. This is the section someone reads to get caught up without reading every line below.

---

## Key Moments

### Topic One

What happened, who said what, what the outcome was.

### Topic Two

Same treatment. Each topic gets its own heading.

---

## Key Decisions

| # | Decision | Owner | Notes |
|---|----------|-------|-------|
| 1 | Decision description | Who owns it | Any context |
| 2 | | | |

---

## Action Items

| # | Item | Owner | Due | Status |
|---|------|-------|-----|--------|
| 1 | Action description | Assigned to | Date or "Next session" | Open |
| 2 | | | | |

---

## Files Created / Modified

- `path/to/file.md` — Description
- `path/to/another.md` — Description

---

## Next Steps

What happens after this meeting. Who picks up what.

---

*Notes maintained by Sara Johansen, Executive Assistant to the President.*
```

---
---

# 3. Technical Design Document

> **Destination:** `project/design/technical-design.md`

```markdown
# {{PROJECT_NAME}} — Technical Design Document

**Project:** THG Media
**Author:** {{AUTHOR}}
**Date:** {{DATE}}
**Status:** {{STATUS}}
**Version:** {{VERSION}}

---

## 1. Overview

What this project is, in technical terms. The README tells people what it does. This document tells the team how it works.

---

## 2. Architecture

High-level architecture. How the pieces connect.

```
Component A
    |
    v
Component B --> Component C
    |
    v
Component D
```

Describe the flow and the reasoning behind the architecture choices.

---

## 3. Component Overview

| Component | Purpose | Technology | Owner |
|-----------|---------|------------|-------|
| Component A | What it does | What it's built with | Who owns it |
| Component B | | | |
| Component C | | | |

---

## 4. Data Flow

How data moves through the system, from input to output. Include formats, transformations, and storage.

### Input

What goes in, where it comes from, what format.

### Processing

What happens to it. Transformations, validations, business logic.

### Output

What comes out, where it goes, what format.

---

## 5. Design System

### Palette

| Token | Hex | Usage |
|-------|-----|-------|
| {{PALETTE_TABLE}} | | |

### Typography

| Role | Font | Weight | Size |
|------|------|--------|------|
| Headings | {{HEADING_FONT}} | | |
| Body | {{BODY_FONT}} | | |
| Mono | {{MONO_FONT}} | | |

### Visual Language

Any other design conventions: spacing, borders, shadows, iconography, illustration style.

---

## 6. Technical Stack

{{TECH_STACK}}

---

## 7. Scope

### In Scope

- Feature or capability one
- Feature or capability two

### Out of Scope

- Explicitly excluded item one
- Explicitly excluded item two

---

## 8. Known Issues & Constraints

| # | Issue | Severity | Notes |
|---|-------|----------|-------|
| 1 | Description | Low / Medium / High | Workaround or plan |
| 2 | | | |

---

## 9. Dependencies

External services, APIs, libraries, or other THG projects this depends on.

| Dependency | Version | Purpose |
|------------|---------|---------|
| | | |

---

## 10. Future Considerations

Things the team should keep in mind as the project evolves. Not committed work, just awareness.

---

*THG Media — The Henderson Group*
```

---
---

# 4. Planning & Roadmap

> **Destination:** `project/docs/planning-roadmap.md`

```markdown
# {{PROJECT_NAME}} — Planning & Roadmap

**Project:** THG Media
**Author:** {{AUTHOR}}
**Date:** {{DATE}}
**Status:** {{STATUS}}
**Maintained by:** {{MAINTAINER}}

---

## Current State

Where the project stands right now. One honest paragraph. What's done, what's in progress, what's blocking.

---

## Phased Feature Roadmap

### Phase 1 — Foundation

| Feature | Owner | Priority | Description |
|---------|-------|----------|-------------|
| Feature name | Who | P1 / P2 / P3 | What it is and why it matters |
| | | | |

**Target:** {{PHASE_1_TARGET}}
**Status:** Not started / In progress / Complete

### Phase 2 — Core Features

| Feature | Owner | Priority | Description |
|---------|-------|----------|-------------|
| | | | |

**Target:** {{PHASE_2_TARGET}}
**Status:** Not started / In progress / Complete

### Phase 3 — Polish & Launch

| Feature | Owner | Priority | Description |
|---------|-------|----------|-------------|
| | | | |

**Target:** {{PHASE_3_TARGET}}
**Status:** Not started / In progress / Complete

Add or remove phases as needed. Some projects are one phase. Some are ten.

---

## Proposed Features

Ideas that have been raised but not committed to a phase yet. Good ideas deserve a place to live even before they're scheduled.

| Feature | Proposed By | Notes |
|---------|-------------|-------|
| | | |

---

## Decision Log

Significant decisions that shaped the project direction. The "why" matters more than the "what" here.

| Date | Decision | Context | Decided By |
|------|----------|---------|------------|
| {{DATE}} | Decision description | Why this choice was made | Who made the call |
| | | | |

---

## Milestones

| Milestone | Target Date | Status | Notes |
|-----------|-------------|--------|-------|
| Project kickoff | {{DATE}} | Complete | |
| | | | |

---

## Risks & Dependencies

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| | Low / Medium / High | Low / Medium / High | Plan |

---

*Roadmap is a living document. Update it when priorities shift, decisions are made, or phases complete.*
*THG Media — The Henderson Group*
```

---
---

# 5. All Files Inventory

> **Destination:** `project/docs/all-files.md`

```markdown
# {{PROJECT_NAME}} — All Files Inventory

**Project:** THG Media
**Generated:** {{DATE}}
**Total files:** {{TOTAL_FILE_COUNT}}
**Maintained by:** {{MAINTAINER}}

---

## Overview

Complete file listing for the {{PROJECT_NAME}} project. Every file has a purpose. If it doesn't, it shouldn't be here.

---

## Root Directory

| File | Purpose |
|------|---------|
| `README.md` | Project overview and quick start |
| `CLAUDE.md` | Project instructions and standing directives |
| `hugo.toml` | Hugo site configuration |
| `.gitignore` | Git exclusion rules |
| `start_webserver.sh` | Local development server launcher |

---

## content/

Page content and markdown sources.

| File | Purpose |
|------|---------|
| `content/_index.md` | Homepage content |
| | |

**File count:** {{CONTENT_COUNT}}

---

## layouts/

Hugo templates and partials.

| File | Purpose |
|------|---------|
| `layouts/_default/baseof.html` | Base template wrapper |
| `layouts/_default/single.html` | Single page template |
| `layouts/_default/list.html` | List page template |
| `layouts/partials/head.html` | HTML head partial |
| `layouts/partials/header.html` | Site header partial |
| `layouts/partials/footer.html` | Site footer partial |
| | |

**File count:** {{LAYOUTS_COUNT}}

---

## assets/

Stylesheets, scripts, and processed assets.

| File | Purpose |
|------|---------|
| `assets/scss/main.scss` | Primary stylesheet |
| | |

**File count:** {{ASSETS_COUNT}}

---

## static/

Images, PDFs, and other static files served as-is.

| File | Purpose |
|------|---------|
| | |

**File count:** {{STATIC_COUNT}}

---

## data/

Hugo data files (YAML, JSON, TOML).

| File | Purpose |
|------|---------|
| | |

**File count:** {{DATA_COUNT}}

---

## project/

Project documentation, design files, and meeting notes.

### project/docs/

| File | Purpose |
|------|---------|
| `project/docs/planning-roadmap.md` | Phased roadmap and decision log |
| `project/docs/all-files.md` | This file |
| | |

### project/design/

| File | Purpose |
|------|---------|
| `project/design/technical-design.md` | Architecture and design system |
| | |

### project/meetings/

| File | Purpose |
|------|---------|
| `project/meetings/{{DATE}}-kickoff.md` | Project kickoff meeting notes |
| | |

**File count:** {{PROJECT_COUNT}}

---

## .github/

CI/CD configuration.

| File | Purpose |
|------|---------|
| `.github/workflows/deploy.yml` | GitHub Actions deployment pipeline |

**File count:** {{GITHUB_COUNT}}

---

## archive/

Archived files no longer in active use but preserved for reference.

| File | Purpose |
|------|---------|
| | |

**File count:** {{ARCHIVE_COUNT}}

---

## Summary

| Directory | Files |
|-----------|-------|
| Root | {{ROOT_COUNT}} |
| content/ | {{CONTENT_COUNT}} |
| layouts/ | {{LAYOUTS_COUNT}} |
| assets/ | {{ASSETS_COUNT}} |
| static/ | {{STATIC_COUNT}} |
| data/ | {{DATA_COUNT}} |
| project/ | {{PROJECT_COUNT}} |
| .github/ | {{GITHUB_COUNT}} |
| archive/ | {{ARCHIVE_COUNT}} |
| **Total** | **{{TOTAL_FILE_COUNT}}** |

---

*Inventory is regenerated when files are added, renamed, or removed.*
*THG Media — The Henderson Group*
```

---
---

# Usage Notes

1. **Copy, don't link.** Each project gets its own copies of these documents. They diverge from the template the moment they're deployed, and that's the point.

2. **Replace all placeholders.** Search for `{{` in the new file and make sure every placeholder is filled or removed. A template variable left in a shipped document is a sign nobody read it.

3. **Customize freely.** These templates are starting points, not straitjackets. Add sections that matter. Remove sections that don't. The goal is useful documentation, not compliance theater.

4. **Meeting notes accumulate.** The meeting template gets used repeatedly. Every meeting gets its own file with the date-topic naming convention.

5. **All Files Inventory stays current.** Update it when the file tree changes. It's a living document, not a snapshot from day one.

6. **PDF companions.** Per standing directive, any markdown file that is requested or created gets a corresponding PDF generated alongside it.

---

*THG Media — The Henderson Group*
*Founded April 1, 2025 at Joe's Java Shack. Everyone thought it was a joke. It wasn't.*
