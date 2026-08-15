Phase 2 — Content. Every checkable fact below traces to profile.md. Where I added
words that profile.md does not state outright, they are motivation/voice/framing —
not a checkable fact — per spec.md J1. Word counts are given so the builder can
verify M11 without recounting.

---

## Meta
- `<title>`: something containing "Muhammad Naveed" — e.g. `Muhammad Naveed — AI Automation Engineer & Full Stack Developer`
- `<html lang="en">`

---

## hero  (id="hero")

**h1** (must contain the name on line 1 of profile.md):
Muhammad Naveed

**role line** (secondary, sits under the h1 — matches profile.md line 2 almost verbatim, it's already good):
AI Automation Engineer & Full Stack Developer

**tagline `<p>`** (≥ 4 words — required by M11; pick one or combine):
Forward-deployed on a live production operation — I don't just build systems, I run them.

(Alt, shorter: "Forward-deployed AI automation engineer. Production systems, not demos.")

**metric tiles** (design.md calls for a row of status-module tiles here — "production
systems shipped, roles, skills tracked". These are checkable numbers, so use exactly
these, sourced as shown. If the builder changes what's in projects/experience/skills
below, recount before shipping — a stale number here is a J1 failure waiting to happen):

- `5` — production systems (profile.md: "Built and operate **five** production Slack and
  Google Workspace automation systems and a live operations dashboard" — Experience,
  Activus Capital Partners entry)
- `3` — roles (the three `###` entries under profile.md's `## Experience`: Activus Capital
  Partners, NaveedTechLab, Fiverr & Direct Clients)
- `37` — skills tracked (count of `- ` list items under profile.md's `## Skills`; recount
  if the skills list below is edited)

Only the tile for the **current** role should carry the accent/live dot, per design.md —
that's the Activus Capital Partners row (dates: "April 2026 – Present"), since it's the
only entry on the page still open-ended and running.

---

## about  (id="about")

Full paragraph — **93 words**, clears the ≥ 40 word floor with room to spare:

> Naveed is a forward-deployed AI automation engineer — the kind of role where you don't
> ship a product and walk away, you sit inside somebody else's operation and keep it
> running. Right now that operation belongs to a pest-control client: five production
> Slack and Google Workspace systems and an operations dashboard he built and still
> operates, including diagnosing a week-long silent outage by hand. Outside that client
> work he runs his own small agency, NaveedTechLab, out of Karachi, and has taken
> freelance projects — Shopify stores, dashboards, automation workflows — from
> requirements through deployment since 2023.

Fact check against profile.md:
- "forward-deployed AI automation engineer" — matches Experience title exactly:
  "AI Automation Engineer (Forward-Deployed)".
- "five production Slack and Google Workspace systems and an operations dashboard he
  built and still operates" — matches "Built and operate five production Slack and
  Google Workspace automation systems and a live operations dashboard."
- "diagnosing a week-long silent outage by hand" — matches "diagnosed week-long silent
  production outage ... via full read-only data audit." (I deliberately dropped the
  307/61 numbers here since they already appear, correctly attributed, in the work
  entry below — no need to repeat a client's operational scale in the About section.)
- "pest-control client" — matches "Activus Capital Partners (Heat Wave Pest Control)".
- "runs his own small agency, NaveedTechLab, out of Karachi" — matches "Founder & Lead
  Developer — NaveedTechLab (Digital Agency)" + "Built a digital agency targeting
  Karachi businesses."
- "Shopify stores, dashboards, automation workflows ... since 2023" — matches the
  Freelance entry almost verbatim, dates 2023–Present.

Why this satisfies J3: it names the actual client relationship (forward-deployed at a
pest-control operation, not a generic "enterprise"), the actual named agency
(NaveedTechLab), the actual city (Karachi), and one distinctive, specific act
(diagnosing a silent outage himself). None of that fits a random classmate.

---

## projects  (id="projects")

Exactly **4** entries — one `<article>` per `###` under profile.md's `## Projects`, in
that order. Each description is well over the 25-word floor and names both what the
thing does and what Naveed did, so no entry could be pasted onto a different project.

### 1. Autonomous AI Marketing Agency
Status chip suggestion: `HACKATHON`
Dates: 2024

> An AI-powered marketing agency built for a hackathon in 2024 — it runs campaign
> strategy, content generation, and client outreach autonomously, chaining agents
> through each stage of a campaign instead of leaving a human to run each step by
> hand. Naveed built and deployed it live on Hugging Face Spaces so it could actually
> be opened and tried, not just described in a submission.

(63 words. Traces to: "AI-powered marketing agency that handles autonomous campaign
strategy, content generation, and client outreach. Deployed on Hugging Face Spaces.")

### 2. Personal AI Employee (Digital FTE)
Status chip suggestion: `HACKATHON`
Dates: 2024

> A hackathon project built as a standing digital employee rather than a one-off
> script: watcher processes keep an eye on Gmail and WhatsApp, an Obsidian-based memory
> system lets the agent hold context across sessions instead of starting fresh each
> time, and a set of MCP tools let it actually execute tasks around the clock rather
> than just report on them. Naveed built the watchers, the memory system, and the tool
> wiring in 2024.

(73 words. Traces to: "Autonomous AI employee with watchers, Gmail and WhatsApp
automation, an Obsidian memory system, and MCP tools for 24/7 task execution.")

### 3. Customer Success FTE (CRM Agent)
Status chip suggestion: `HACKATHON`
Dates: 2024

> A hackathon-built support agent that takes customer conversations from three
> different channels — Gmail, WhatsApp, and web forms — and lands them all in one
> queue instead of three separate inboxes. Naveed built the FastAPI backend and the
> PostgreSQL ticket system underneath it, so a ticket raised by email and a ticket
> raised by WhatsApp message end up as the same kind of object the team can work from.

(67 words. Traces to: "Multi-channel support agent across Gmail, WhatsApp, and web
forms with a PostgreSQL ticket system and FastAPI backend.")

### 4. Cloud-Native Microservices Architecture
Status chip suggestion: `SHIPPED` (or `2024` — this one has no "hackathon" label in
profile.md, unlike the other three; keep that distinction, don't flatten all four to
the same chip)
Dates: 2024

> A 2024 project exploring how automation and agent skills could be packaged as
> independent, containerized microservices instead of one monolith — reusable agent
> skills built on an event-driven architecture using Docker, Kafka, Dapr, and
> Kubernetes. Naveed built the service boundaries and the event wiring that connects
> them.

(53 words. Traces to: "Reusable agent skills and containerized microservices built on
an event-driven architecture using Docker, Kafka, Dapr, and Kubernetes." Note: unlike
the other three projects, profile.md does not call this one a hackathon entry, and I
have not called it one — the Source notes section says all four are "live and deployed
with demos available," which is the one claim safe to make uniformly across all four.)

---

## work / experience  (extra section — not one of M1's five, but design.md's whole
premise leans on these entries, so they need real words too. Suggested id="work",
placed after `projects` and before `skills` — check the nav in design.md for where it
expects this.)

### AI Automation Engineer (Forward-Deployed) — Activus Capital Partners (Heat Wave Pest Control)
Status chip: `LIVE` — this is the only still-open role (April 2026 – Present)

> Forward-deployed onto a live pest-control operation, building and operating five
> production Slack and Google Workspace automation systems plus a live operations
> dashboard, with direct ownership of incident response and API integration
> reliability. The Specialty Form Compliance Bot matches calendar events against
> Google Forms submissions using token-based property/service matching, compound-word
> decomposition, and Levenshtein fuzzy matching, and scaled to cover 123 registered
> properties with automatic header-based column detection. The Notes Verification Bot
> checks scheduling notes in real time off technician departure messages, with a
> 15-minute escalation and re-check workflow and skip logic for cancelled or duplicate
> entries — Naveed also diagnosed and fixed cross-property and cross-technician
> validation bugs in it. He built a Weekly Reporting Suite that auto-generates the
> specialty-services and bait-box/exterior-services reports, refined over multiple
> rounds of stakeholder feedback, and a Specialty Recommendation System that drafts
> recommendation emails to property managers from follow-up flags using tier-aware
> pricing — when that system went silent for a week, he diagnosed the outage by hand
> through a full read-only data audit covering 307 qualifying cases across 61
> properties. He also built the password-protected Operations Dashboard itself, with
> six live sections including a Slack-history-based Route Timing engine that computes
> per-technician daily timelines, and fixed a Google Sheets API rate-limit failure
> under 112+ concurrent reads by moving the data path to scheduled background
> precompute with snapshot caching — cutting load time from 60–90 seconds to an
> instant cached read.

Every number here (123 properties, 15-minute window, 307 cases, 61 properties, 112+
concurrent reads, 60–90 seconds) is quoted from profile.md's Experience entry and
attributed to the client's operation / the systems Naveed built for it — never
reworded as "his own" business metric. This is exactly the landmine the task flagged;
I kept the client's scale as the client's scale throughout.

### Founder & Lead Developer — NaveedTechLab (Digital Agency)
Status chip: `LIVE` (2025 – Present)

> His own digital agency, built to serve small Karachi businesses. He landed two
> clients — CCTV World Karachi and Ha-Aeen Dentistry — wrote their 6-month digital
> transformation roadmaps, partner agreements, and pricing strategies himself, and
> delivered their digital footprint, customer acquisition systems, and workflow
> automation end-to-end, from the first scoping call through delivery.

(Traces to profile.md's NaveedTechLab entry line-for-line — two named clients, roadmap
+ partner agreements + pricing strategy, end-to-end delivery.)

### Freelance Full Stack Developer — Fiverr & Direct Clients
Status chip: `LIVE` (2023 – Present)

> Client work outside the agency and the day job: Shopify stores, business websites,
> custom dashboards, CMS-based sites, and automation workflows, each taken from a
> client's stated requirements through design, development, and deployment on his own.

---

## education  (optional extra section — flagging a landmine explicitly)

If the builder includes an education module:

> Diploma in Computer Information Technology (DCIT) and Certificate in Information
> Technology (CIT), Governor House Initiative, 2023 – Present.

Use language like "studying for," "pursuing," or "in progress toward" if any framing
text surrounds this. **Do not** write "certified," "certification," "holds a diploma,"
or "graduated" — profile.md's Source notes section is explicit that these are
credentials currently being earned (2023–Present), not completed ones. If the builder
skips this section entirely, that's also fine — it isn't required by M1/M11.

---

## skills  (id="skills")

M11 requires one `<li>` per skill in profile.md, **all of them** — 37 total. Render
them as the tag/chip grid design.md calls for, in this exact order (copy verbatim,
do not add or remove any, do not merge "Anthropic API (Claude Code)" down to just
"Anthropic API" or drop the parenthetical — it's part of the stated skill):

Node.js, Python, FastAPI, REST APIs, Express, node-cron, Next.js, React, TypeScript,
Tailwind CSS, HTML5/CSS3, OpenAI API, Anthropic API (Claude Code), Gemini API,
LangChain, OpenRouter, Agents SDK, MCP, Slack Bot & Events API,
Google Sheets/Calendar/Gmail API, Webhooks, WhatsApp, Twilio, Railway, Docker,
Kubernetes, Kafka, Dapr, CI/CD, GitHub, MongoDB, PostgreSQL, Sanity CMS,
Event-driven design, Spec-driven design, Fuzzy matching / alias resolution,
Background precompute and caching.

No section heading text is needed beyond something like "Skills" or "Capabilities" —
the list itself is the content requirement.

---

## contact  (id="contact")

Framed as outbound channels per design.md, each with a monospace prefix. Use exactly
these values from profile.md — do not invent a portfolio tagline URL, a Twitter, or
anything not listed:

- `mail:` qureshinaveed21@hotmail.com → `<a href="mailto:qureshinaveed21@hotmail.com">`
- `tel:` +92 300 3627458 → `<a href="tel:+923003627458">`
- `git:` github.com/naveedtechlab → `<a href="https://github.com/naveedtechlab">`
- `web:` linkedin.com/in/naveedtechlab → `<a href="https://linkedin.com/in/naveedtechlab">`
- `demo:` naveedtechlab-portfolio.hf.space → `<a href="https://naveedtechlab-portfolio.hf.space">`
- location (text, not a link): Karachi, Pakistan

M11 only requires ≥ 1 `<a>` with `mailto:` or `https://` — the list above gives five,
any subset is fine as long as the mail link stays (it's the one channel a stranger
can act on immediately).

---

## Notes back to the pipeline (gaps, not fabrications)

- profile.md has no photo/headshot asset. If the builder wants an image in `hero` or
  `projects` (M5 requires non-empty alt there — those slots are never decorative),
  there is nothing in profile.md to source real alt text from. Do not invent a
  headshot or a project screenshot that doesn't exist in the source — either skip
  images in those sections, or use something genuinely available (e.g., a diagram the
  builder constructs and can honestly describe, not a photo of Naveed that doesn't
  exist in this project's assets).
- profile.md gives no outcome/impact numbers for the four hackathon/2024 projects
  beyond "deployed" — I did not invent usage numbers, awards, or placements for them.
  If a status chip design wants a metric per project card the way the Experience
  entries have one, there isn't one to give honestly for these four; a `HACKATHON` /
  `SHIPPED` status chip alone is the honest ceiling.
- profile.md does not give a company/team size, revenue, or valuation for either
  Activus Capital Partners or NaveedTechLab. None is asserted above.
- The Governor House credentials are explicitly in-progress; see the education note.

Everything else above is either quoted near-verbatim from profile.md or is voice/
motivation framing that asserts no checkable fact (why he built something, what a
role feels like, why a project mattered) — the kind of elaboration spec.md's J1
explicitly allows.
