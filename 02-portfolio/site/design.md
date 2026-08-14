# The design decision
The page is an operations status board for a career: every section is a status module — a monospace label, a live/verified state marker, and a metric — the same grammar Naveed's own Slack and Sheets dashboards use to turn raw operational activity into an at-a-glance state, and the single accent colour (a signal green) is reserved for that live-state marker alone, never for decoration.

## Why this person
His actual second job is building the thing this page borrows from: a "Notes Verification Bot" with a 15-minute escalation/re-check workflow, a "Specialty Form Compliance Bot" that reports match state across 123 properties, and an "Operations Dashboard" with six live sections that replaced a 60–90 second load with an instant cached read. He does not write about status systems — he ships them. A page for any other developer would have no honest claim to this grammar; for him it is just his other tab, open.

## How the page carries it out
- **Nav** is a fixed section rail with uppercase monospace labels, mirroring the section rail of his own Operations Dashboard (Overview, Route Timing, Units Allocation…); the current section is marked with a single accent dot — an "active system" indicator, not a decorative underline.
- **Hero** is a status readout, not a title page: name and role line, then a row of metric tiles (production systems shipped, roles, skills tracked) built from the same module grammar as the rest of the page; only the tile for the current role carries the accent dot, because it is the one thing on the page that is actually live right now.
- **Projects and experience** render as modules/cards, each with a monospace status chip in the corner (`LIVE`, `SHIPPED`, `HACKATHON`) and any scale numbers (123 properties, 307 cases, 61 properties) set in monospace against `--fg-dim`, with prose underneath in the body face. A set of things looks like a set — never stacked paragraphs.
- **Skills** render as a tag/chip inventory in a wrapping grid — a system's registered capabilities — never a plain bulleted list with default `<ul>` padding.
- **Contact** is an outbound-channels module: each link carries its channel type as a monospace prefix (`mail:`, `git:`, `web:`), the same way a dashboard labels its integrations.
- **At 390px**, it survives by keeping the module grammar intact rather than collapsing it: cards stack to one column but each keeps its status chip + monospace label + accent dot; the hero's metric row goes to a 2-column wrap instead of dissolving into plain stacked numbers — the identity is typographic and chromatic, not dependent on the grid staying wide.
- The accent is refusable in one direction only: if a colour choice is not marking a live/current state, it is not accent — it is `--fg` or `--fg-dim`. No gradients, no glow, no colour used "because it looks nice."

## Tokens
```css
:root {
  /* colour — dark operations-console surface, signal-green accent means "live" and nothing else */
  --bg:      #0b0e14;
  --bg-raised: #12161f;   /* card/module surface, one step up from --bg */
  --fg:      #e6e8ec;
  --fg-dim:  #9aa4b2;     /* secondary/meta text: labels, timestamps, scale numbers */
  --accent:  #3ddc84;     /* signal green — used only for the live-state marker */

  /* computed: --fg on --bg = 15.75:1 (AA pass)
               --accent on --bg = 10.83:1 (AA pass)
               --fg-dim on --bg = 7.66:1 (AA pass, safe for secondary text too) */

  /* type scale — contrast of scale carries hierarchy, not weight alone */
  --text-xs:   0.72rem;
  --text-sm:   0.86rem;
  --text-base: 1.05rem;
  --text-lg:   1.3rem;
  --text-xl:   clamp(2rem, 5vw, 3.2rem);
  --text-2xl:  clamp(2.8rem, 9vw, 6.5rem);

  /* spacing scale */
  --space-1: 0.3rem;
  --space-2: 0.6rem;
  --space-3: 1.1rem;
  --space-4: 2rem;
  --space-5: 3.5rem;
  --space-6: 7rem;

  /* measure: apply to .prose / <p>, never to <body>. 47ch is a starting point, not
     a guarantee — ch is the advance width of "0", not an average glyph. Render the
     built page, select a real paragraph, and count actual characters per line;
     retune this value until it measures 45–75, don't trust the number as declared. */
  --measure: 47ch;

  /* faces: monospace carries the "system" signature (labels, chips, meta numbers);
     the body face carries prose. Both must come from the system stack — no network fonts. */
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  --font-sans: system-ui, -apple-system, "Segoe UI", sans-serif;
}
```
