# Portfolio Site Map (Current State)

Last reviewed: 2026-04-09

## 1) Core Entry & Navigation Pages
- `index.html` — main one-page portfolio hub (home/about/skills/experience/education/projects/contact sections).
- `all-projects.html` — primary project listing page (page 1).
- `all-projects-2.html` — secondary listing/pagination page.
- `partnerships.html` — companies/partners page.
- `certification.html` — certifications page.

## 2) Main Case Study Pages (Primary)
- `Projects/payments-platform.html` — INSEAD payment platform case study.
- `Projects/invoice-payments-api.html` — invoice payments API case study.
- `Projects/tm-redesign-case-study.html` — payment links redesign case study.
- `Projects/transfermate-payments-dashboard.html` — payments dashboard case study.
- `Projects/company-a-payments-dashboard.html` — company A dashboard case study.
- `Projects/fx-gains-limiter.html` — FX gains limiter case study.
- `Projects/recurring-payments.html` — recurring payments case study.
- `Projects/aws-migration.html` — AWS migration case study.
- `Projects/document-collection.html` — document collection case study.
- `Projects/data-deletion.html` — data deletion case study.
- `Projects/tm-redesign.html` — legacy redesign page variant.

## 3) Legacy / Duplicate / Transitional Pages
- `tm-redesign.html` — root-level redesign legacy page.
- `data-deletion.html` — root-level data deletion legacy page.
- `blog-details.html` — template-derived old article page.
- `knowledge-base.html` — legacy/template page.
- `project1.html` — older project page.
- `project-file.html` — older project page.
- `test.html` — test page.
- `testpage.html` — company A redesign test/case page.
- `example.html` — sample page.
- `cv-portfolio-draft.html` — draft CV page.

## 4) Utility / Support Pages
- `404.html` — error page.
- `transfermate-product-owner-progress.html` — progress timeline page.
- `uptime.html` — document/status utility page.

## 5) Resource Pages (Not Primary Portfolio Navigation)
- `Resources/dashboard-info.html`
- `Resources/INSEAD/pivotreport-260130-1450.html`

## 6) Content Architecture Direction (Target)
Desired structure over time:
1. `index.html` as concise personal positioning page.
2. `all-projects.html` as project catalog hub.
3. `Projects/*.html` as canonical case studies.
4. Legacy root-level duplicates either redirected, archived, or removed from navigation.

## 7) Known Structural Risks
- Mixed legacy/template naming and inconsistent titles.
- Duplicate project pages at root and `Projects/` level.
- Some pages still contain placeholder/template content.
- Navigation labels differ across pages.
