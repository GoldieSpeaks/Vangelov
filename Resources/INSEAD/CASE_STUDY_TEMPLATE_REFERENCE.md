# Case Study Page - Template Reference Guide

**Project:** INSEAD Global Payment Platform Case Study  
**File:** `/Projects/payments-platform.html`  
**Created:** January 2026

---

## Overview

This document serves as a reference guide for creating professional case study pages for the portfolio. It outlines the structure, components, styling patterns, and best practices used in the INSEAD payment platform case study.

---

## Page Structure

### 1. **Header Section**
- Project title (large, bold)
- Subtitle/tagline describing the project
- Brief overview paragraph (2-3 sentences)
- NDA/Confidentiality notice (if applicable)

### 2. **Project Stats Grid**
- Duration (months/years)
- Team size
- Development cycles
- Features delivered
- Icons with numbers and labels

### 3. **Technologies & Integrations**
- Tech stack pills (pill-shaped badges)
- Key technologies used
- Integration points
- Methodologies

### 4. **Role & Team Section** (4-column grid)
- Role & Team composition
- Key Deliverables
- Technologies used
- Project Duration

### 5. **The Challenge Section**
- Main heading
- Subtitle
- Problem description (2-3 paragraphs)
- Two-column breakdown of specific challenges:
  - Left column: 3 challenge areas
  - Right column: 3 challenge areas

### 6. **My Role & Approach Section**
- Main heading + subtitle
- Two-column layout with 3 items each:
  - Left: Discovery, Cross-Org Leadership, Business Presentations
  - Right: Product Roadmap, Design Leadership, Technical Architecture

### 7. **What We Built Section**
- Deliverables checklist (✓ icons with "Delivered" status)
- Detailed component descriptions (6-7 subsections)
- Project Milestones timeline
- Product Ownership Process (6-step numbered flow)

### 8. **Outcomes & Impact Section**
- Before/After comparison cards
- Impact metrics shown visually
- Key outcomes (2x2 grid of outcome cards)

### 9. **Key Learnings Section**
- 4 main learnings as subsections
- Each with heading and detailed paragraph

### 10. **Conclusion Section**
- Why the project matters
- Skills demonstrated
- Value proposition

---

## Visual Components Used

### Stats Cards
```css
- Background: gradient green (rgba(125, 186, 92, 0.1) to rgba(125, 186, 92, 0.02))
- Border: 1px solid green with 0.2 opacity
- Hover: translateY(-5px) with shadow
- Grid: auto-fit, minmax(200px, 1fr)
```

### Tech Pills
```css
- Background: rgba(125, 186, 92, 0.15)
- Color: #7dba5c (green)
- Border: 1px solid green with 0.3 opacity
- Border radius: 20px
- Hover: darker background, move up 2px
```

### Timeline Component
```css
- Left border: 3px vertical line with green gradient
- Timeline items: left-bordered cards
- Dots: 12px circles with green background and glow
- Dates: green text, uppercase
- Hover: translate right 5px
```

### Checklist
```css
- Green checkmark icon (✓)
- Left border: 3px solid #4caf50
- Status badge: "Delivered" in green
- Hover: translateX(5px)
```

### Process Flow (Numbered Steps)
```css
- 2-column grid on desktop
- Numbered circles: gradient green background
- Border: 2px solid green with 0.2 opacity
- Hover: scale(1.05)
- Numbers: 1-6 in white/dark text
```

### Before/After Comparison
```css
- 3-column grid: Before | Arrow | After
- Before: red background/border
- After: green background/border
- Arrow: green color (→)
- Mobile: stack vertically, rotate arrow 90°
```

### Two-Column Section Cards
```css
- Grid: 1fr 1fr (50/50 split)
- Background: rgba(255, 255, 255, 0.02)
- Border: 1px solid with 0.05 opacity
- Hover: border green, translateY(-5px), shadow
```

---

## Color Scheme

### Primary Colors
- **Green (Main):** `#7dba5c`
- **Green (Dark):** `#6ba84e`
- **Green (Transparent):** `rgba(125, 186, 92, X)` where X = opacity

### Supporting Colors
- **Background:** `#1a1a1a` (dark)
- **Text Primary:** `#ffffff` (white)
- **Text Secondary:** `#b8b8b8` (light gray)
- **Text Tertiary:** `#999` (medium gray)
- **Success:** `#4caf50` (checklist items)
- **Error/Before:** `#f44336` (red for "before" states)

### Special Cases
- **NDA Notice:** Keep yellow (#ffc107) for visibility
  - Background: rgba(255, 193, 7, 0.1)
  - Border: 4px solid #ffc107

---

## Responsive Design Breakpoints

### Desktop (Default)
- Two-column layouts
- Full grid displays
- Process flow: 2 columns

### Tablet (1024px)
- Maintain 2-column where possible
- Reduce gaps to 30px
- Process flow: 2 columns

### Mobile (768px)
- Single column layouts
- Stack all grids
- Process flow: 1 column
- Timeline: reduce padding

### Small Mobile (480px)
- Further reduced padding
- Smaller font sizes
- Process flow: 1 column with less gap
- Hide breadcrumbs

---

## Content Guidelines

### Language & Tone
- **Professional but accessible**
- Use "I" for personal contributions
- Use "we" for team efforts
- Avoid jargon unless necessary
- Focus on outcomes, not just activities

### Section Length
- **Overview:** 2-3 paragraphs max
- **Challenge:** 2 intro paragraphs + 6 specific challenges
- **Role:** 6 areas of responsibility
- **What We Built:** 7-8 components with descriptions
- **Outcomes:** 6-8 outcome cards
- **Learnings:** 4 key takeaways
- **Conclusion:** 3 paragraphs

### NDA Compliance
- Always include NDA notice if applicable
- Anonymize company names when required
- Avoid specific metrics if confidential
- Use ranges instead of exact numbers
- Keep focus on skills/process vs proprietary details

---

## Key Terminology Choices

### Project Management
- ✅ **Use:** Agile, iterative development cycles, development cycles
- ❌ **Avoid:** Sprints, Scrum (unless specifically used)

### Role Description
- ✅ **Use:** Product Owner, led, coordinated, facilitated
- ❌ **Avoid:** Managed (unless accurate), handled

### Deliverables
- ✅ **Use:** Delivered, built, implemented, created
- ❌ **Avoid:** Completed, finished (less impactful)

### Outcomes
- ✅ **Use:** Successful launch, integration delivered, platform deployed
- ❌ **Avoid:** Vague claims without context

---

## File Organization

### HTML Structure
```
- External CSS links (style.css, styles2.css, etc.)
- Inline <style> block for page-specific styling
- Content wrapped in proper semantic HTML
- Sections with clear class names
```

### CSS Organization (Inline Style Block)
1. Base responsive styles
2. Component styles (stats, tech pills, timeline, etc.)
3. Layout sections (two-col, grids)
4. Responsive breakpoints (1024px, 768px, 480px)

---

## Common Pitfalls to Avoid

### HTML Issues
- ❌ Unclosed tags (especially `<b>`, `<p>`, `<div>`)
- ❌ Orphaned content without parent elements
- ❌ Duplicate IDs or malformed classes
- ✅ Always validate HTML structure
- ✅ Use proper nesting

### CSS Issues
- ❌ Using `auto-fit` for horizontal items that overflow
- ❌ Forgetting mobile breakpoints
- ❌ Inconsistent color values
- ✅ Use 2-column grid for numbered processes
- ✅ Test on all breakpoints

### Content Issues
- ❌ Too much technical jargon
- ❌ Focusing on bugs/fixes vs platform development
- ❌ Vague outcomes without context
- ✅ Balance technical and business value
- ✅ Show leadership and cross-functional work

---

## Reusable Code Snippets

### Timeline Item Template
```html
<div class="timeline-item">
    <div class="timeline-date">Month X-Y</div>
    <div class="timeline-title">Phase Name</div>
    <div class="timeline-desc">Description of what happened</div>
</div>
```

### Outcome Card Template
```html
<div class="two-col-section">
    <div>
        <div style="padding-bottom: 20px; font-size: 24px; font-weight: bold; color: white;">Outcome Title</div>
        <p style="color: #b8b8b8;">Detailed description of the outcome and its impact.</p>
    </div>
</div>
```

### Process Step Template
```html
<div class="process-step">
    <div class="process-number">1</div>
    <div class="process-title">Step Name</div>
    <div class="process-desc">Step description</div>
</div>
```

### Checklist Item Template
```html
<div class="checklist-item">
    <span class="checklist-icon">✓</span>
    <span class="checklist-text">Deliverable name</span>
    <span class="checklist-status">Delivered</span>
</div>
```

---

## Best Practices Summary

1. **Start with structure** - outline sections before content
2. **Use consistent components** - reuse patterns for cohesion
3. **Green color scheme** - except NDA notices (yellow)
4. **Mobile-first responsive** - test all breakpoints
5. **Clear hierarchy** - use heading levels properly
6. **Focus on outcomes** - not just activities
7. **Show leadership** - cross-org, presentations, decision-making
8. **Keep it scannable** - use bullets, short paragraphs, cards
9. **Validate HTML** - check for unclosed tags regularly
10. **Test on live server** - see actual rendering

---

## Future Improvements

### Potential Enhancements
- Add image/screenshot sections (currently text-only)
- Include video demos or walkthroughs
- Add "Skills Used" tag cloud
- Interactive timeline with click-to-expand
- Testimonials or stakeholder quotes
- Metrics visualization (charts/graphs)

### Accessibility
- Add ARIA labels to interactive elements
- Ensure sufficient color contrast
- Add alt text for any images
- Keyboard navigation for interactive components

---

## Related Files
- Template: `/Resources/Template.md`
- Reference Project: `/Projects/tm-redesign.html`
- This Implementation: `/Projects/payments-platform.html`
- Project Data: `/Resources/INSEAD/INSEAD Project Tracker V3(Project Tracker).csv`

---

**Last Updated:** January 30, 2026  
**Maintainer:** Portfolio Development  
**Status:** ✅ Production Ready
