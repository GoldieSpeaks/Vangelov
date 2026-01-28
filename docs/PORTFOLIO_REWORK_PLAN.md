# Portfolio Rework — Action Plan

Goal: Rework the portfolio into a clear, up-to-date, accessible site. Break the work into small chunks so we can execute one task at a time.

## Phase 1 — Discovery (small chunks)
- 1.1 Inventory files: list all pages, images, scripts, and docs.
- 1.2 Identify live links that must remain (clients, hosted assets).
- 1.3 Gather goals: list what the portfolio must show (roles, outcomes).
- 1.4 Prioritize projects: tag projects as Primary / Secondary / Archive.
- 1.5 Note constraints: deadlines, brand assets, CMS needs.

## Phase 2 — Content (small chunks)
- 2.1 For each Primary project: write a 1-paragraph summary.
- 2.2 For each Primary project: list 3 measurable outcomes or results.
- 2.3 Create a short author bio (1-2 sentences) and contact blurb.
- 2.4 Collect and optimize images: crop, resize, name consistently.
- 2.5 Create a content spreadsheet (title, slug, summary, images).

## Phase 3 — Information Architecture & Design (small chunks)
- 3.1 Draft a sitemap with main pages (Home, All Projects, Project, About, Contact).
- 3.2 Create a simple wireframe for Home and All Projects (low-fi).
- 3.3 Decide on visual direction: fonts, colors, and spacing (moodboard).
- 3.4 Design a single Project detail template (hero, summary, images, results).
- 3.5 Define responsive breakpoints and nav behavior for mobile.

## Phase 4 — Frontend Development (small chunks)
- 4.1 Create a base HTML template and include shared header/footer.
- 4.2 Implement responsive navigation (desktop + mobile toggle).
- 4.3 Build `all-projects.html` listing using the content spreadsheet.
- 4.4 Build one `project-detail.html` using the Project template.
- 4.5 Implement image lazy-loading and optimized formats (webp fallback).
- 4.6 Add basic CSS variables and utility classes for spacing/typography.

## Phase 5 — Integration & polish (small chunks)
- 5.1 Wire up contact form (or `mailto:`) and test submission flow.
- 5.2 Add canonical URLs, meta titles, and meta descriptions per page.
- 5.3 Implement social sharing tags (Open Graph, Twitter card).
- 5.4 Ensure internal links and breadcrumbs point to correct pages.
- 5.5 Replace remaining incorrect `Blog` nav labels with `All projects`.

## Phase 6 — SEO, Performance & Accessibility (small chunks)
- 6.1 Run Lighthouse and note top 5 performance fixes.
- 6.2 Compress and cache static assets; add `Cache-Control` recommendations.
- 6.3 Add alt text for all images from spreadsheet.
- 6.4 Ensure headings follow a single logical order (H1 → H2 → H3).
- 6.5 Validate keyboard navigation and ARIA where needed.

## Phase 7 — QA & Cross-Browser Testing (small chunks)
- 7.1 Test on iOS Safari and Android Chrome at common screen widths.
- 7.2 Test on desktop Chrome / Firefox / Safari for layout regressions.
- 7.3 Validate forms and external links.
- 7.4 Fix any layout issues and re-run accessibility checks.

## Phase 8 — Launch & Post-Launch (small chunks)
- 8.1 Prepare a deploy checklist: backups, DNS, redirects.
- 8.2 Deploy to staging and run smoke tests.
- 8.3 Deploy to production and verify critical pages.
- 8.4 Set up analytics and basic event tracking for CTA clicks.
- 8.5 Monitor for 72 hours and triage any high-severity bugs.

## Phase 9 — Iterate & Handoff (small chunks)
- 9.1 Collect feedback from stakeholders (one-page report).
- 9.2 Triage feedback and schedule quick wins (<1 day each).
- 9.3 Update the `docs/` folder with final content source and how-to.
- 9.4 Handoff: provide a short README explaining deploy and edits.

## How to use this plan
- Pick one numbered item (e.g., "1.1 Inventory files") and mark it done when complete.
- Keep each task to ~15–90 minutes where possible; split further if needed.
- Use the content spreadsheet to drive development and page creation.

---
Created as a small-chunk action plan to rework the portfolio incrementally.
