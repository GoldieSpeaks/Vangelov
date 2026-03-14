# Showcase Template Playbook (Reference)

## Purpose
Reusable blueprint for creating high-impact project showcase pages with NDA-safe detail, visual credibility, and consistent structure.

## Primary Layout Order
1. Hero wallpaper image
2. Main heading + short project subtitle
3. NDA/Confidentiality notice (clear and explicit)
4. Delivery snapshot (short bullets)
5. External validation card (news release/client press/proof link)
6. Stats cards (4 key metrics)
7. Visualizations block A
   - Program phase timeline
   - Capability coverage bars
8. Tech stack pills
9. Role/team and key deliverables cards
10. Architecture pattern block (high-level, NDA-safe)
11. Challenge section
12. Authentication/flow screenshots (if allowed)
13. My role & approach
14. What we built
15. Outcomes & impact
16. Visualizations block B
   - Delivery distribution bars
   - Program velocity line chart (illustrative)
17. Key outcomes
18. Key learnings
19. Conclusion

## Content Rules (NDA-safe)
- Never include credentials, endpoint details, secrets, payload samples, private identifiers.
- Use architecture patterns and delivery outcomes, not implementation internals.
- Use aggregate metrics only (counts, ranges, percentages).
- Label visualizations as normalized/illustrative where needed.

## Tone Rules
- Senior, product-led, concise.
- Avoid buzzwords like "seamless".
- Prefer factual language: "integrated", "delivered", "coordinated", "optimized".

## Reusable Components
- External Validation block (CTA button to official source)
- Phase timeline cards (4 phases, including ongoing improvement phase)
- Capability bars
- Workstream distribution bars
- Velocity SVG trend chart

## Metric Guidelines
Use durable labels that remain valid over time:
- "Since YYYY" instead of "YYYY-Now"
- "Partnership Start" instead of "Current Timeline"
- "Tracked Work Items" instead of sensitive backlog references
- "Post-Go-Live Improvements" for ongoing optimization

## Recommended Link Placement Pattern
Place proof links immediately after NDA + snapshot and before stats.
Reason: viewers validate legitimacy early, then consume details.

## File Pattern Used
- Working draft copy for experiments: /Projects/<project>-enhanced.html
- Approved replacement target: /Projects/<project>.html

## Current Example Reference
- Enhanced source pattern validated on INSEAD case study.
- Includes reusable visualization CSS classes:
  - .viz-grid
  - .viz-card
  - .bar-row / .bar-track / .bar-fill
  - .phase-list / .phase-item
  - .architecture-flow / .arch-node

## Checklist Before Publishing
- [ ] No NDA-sensitive text
- [ ] No "seamless" wording
- [ ] At least 1 external proof link
- [ ] 2 visualization sections present
- [ ] Mobile layout still readable
- [ ] Stats are time-robust (not expiry-prone)
- [ ] Main page only replaced after draft approval
