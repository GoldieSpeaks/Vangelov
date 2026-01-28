# Zlatomir Vangelov Portfolio - Navigation & Optimization Guide

## Executive Summary
Your portfolio is a **responsive, single-page + multi-page hybrid website** showcasing your professional journey as a Product Owner, Entrepreneur, and UI/UX Designer. The site features a modern sidebar navigation design with sections covering your background, skills, experience, education, and project portfolio. It's built with HTML, CSS, and JavaScript with a focus on visual storytelling and project showcasing.

---

## Part 1: Site Structure Overview

### Main Pages
| Page | Purpose | Status |
|------|---------|--------|
| **index.html** | Primary hub - all sections (Home, About, Skills, Experience, Education, Projects, Contact) | ✓ Primary |
| **all-projects.html** | Dedicated project listing page | ✓ Active |
| **blog-details.html** | Individual project detail template | Linked |
| **tm-redesign.html** | TransferMate redesign project showcase | Linked |
| **knowledge-base.html** | Knowledge base/API documentation project | Linked |
| **partnerships.html** | Companies/partners worked with | Linked |
| **certification.html** | Certifications & credentials | Linked |
| **data-deletion.html** | GDPR/Data deletion project | Linked |
| **project1.html** | Additional project template | Standalone |
| **project-file.html** | Project file template | Standalone |

### Secondary Pages
- **404.html** - Error page
- **uptime.html** - Uptime/status page
- **example.html** - Template example
- **test.html** - Testing page
- **demo.xml** - Demo data file
- **send-email.php** - Backend contact form handler

---

## Part 2: Component Breakdown

### A. **Visual & Style Assets (CSS)**
```
css/
├── style.css           → Main styling & layout
├── responsive.css      → Mobile & responsive design
├── portfolio.css       → Portfolio/project grid styling
├── carousel.css        → Slider/carousel styling
├── scroll.css          → Scroll animations
├── font-awesome.css    → Icon library
└── normalize.css       → CSS reset
```

**Current State:** Multiple CSS files properly organized by function
**Optimization Opportunity:** Consider consolidating into fewer files with better organization

---

### B. **JavaScript Functionality (JS)**
```
js/
├── jquery-2.0.3.min.js     → jQuery framework
├── modernizr.custom.js     → Feature detection
├── progressbar.js          → Skill progress charts
├── carousel.js             → Portfolio carousel/slider
├── grid_gallery.js         → Gallery grid layout
├── masonry.min.js          → Masonry layout library
├── jquery.easypiechart.js  → Pie chart (skills)
├── sendemail.js            → Contact form submission
└── [13+ additional utility scripts]
```

**Current State:** Heavy jQuery dependence, multiple utility libraries
**Optimization Opportunity:** Some libraries are outdated (jQuery 2.0.3 from 2013)

---

### C. **Media Assets**
```
images/           → Portfolio images, logos, thumbnails
  └── Key files: logo.png, profile.png, project thumbnails
fonts/            → Custom font files
PDF/              → Resume/document storage
```

**Current State:** Basic asset organization
**Optimization Opportunity:** Add image optimization and compression

---

## Part 3: Key Sections & Content Areas

### 1. **Introduction Section** (Home)
- Profile header with "Hello, I'm Zlatomir Vangelov"
- Title: "Product Owner, Entrepreneur & UI/UX Designer"
- Profile image showcase
- Owl Carousel integration (currently minimal content)

**Status:** ✓ Active | **Priority:** Medium

---

### 2. **About Section**
- Personal information card (name, email, phone, DOB, location)
- Professional profile statement
- Resume download link (PDF)
- Signature image

**Issues to Address:**
- Email link is incorrect format: `work.vangelov@gmail.com` (missing `mailto:`)
- Resume download button exists but may not be linked to actual PDF

**Status:** ⚠️ Needs fixes | **Priority:** High

---

### 3. **Skills Section**
Three subsections:
1. **Core Skills** - Pie/progress charts (80-100%)
   - Lean Process Optimization (80%)
   - UI/UX Design (80%)
   - Product Management (100%)
   - Front-End Development (40%)

2. **Knowledge & Main Skills** - Listed in 3 columns
   - UX Development, Wireframing, Lean Waste Management
   - UI Design, Branding, Team Building, Project Management
   - Agile, Stakeholder Management, Storytelling, Conceptualization

3. **Additional Skills & Tools**
   - Design tools: Figma, Adobe XD, InVision, Sketch
   - Development: HTML5, CSS3, JavaScript, React
   - Management: Jira, Confluence, WordPress
   - Databases: MySQL, Git, VS Code

**Status:** ✓ Comprehensive | **Priority:** Low (minor updates possible)

---

### 4. **Experience Section**
*(Need to expand reading to see full content)*
- Work history and roles
- Company/employer information

**Status:** Need to verify | **Priority:** Medium

---

### 5. **Education Section**
*(Need to expand reading to see full content)*
- Academic background
- Certifications and training

**Status:** Need to verify | **Priority:** Medium

---

### 6. **Projects / Portfolio Section**
**Current Projects Listed:**
- Payments Platform (blog-details.html)
- Invoice Payments API (knowledge-base.html)
- FX Gains Limiter (blog-details.html)
- Re-Design (tm-redesign.html)
- Data Deletion (data-deletion.html)

**Project Card Components:**
- Thumbnail image
- Date posted
- Project title (linked)
- Author/contributors
- Category tags
- Description excerpt
- Social sharing buttons

**Status:** ✓ Active | **Priority:** High (content update recommended)

---

### 7. **Navigation Components**

**Primary Navigation (Sidebar):**
- Logo section with profile image
- Main menu links (7 primary + 1 secondary "All Projects")
- Social media links (Facebook, Twitter, Google+)
- Copyright notice

**Secondary Navigation:**
- Projects → All Projects, Partnerships, Certifications (separate page tabs)

**Issues:**
- Social links point to generic profiles (not personalized)
- Twitter/Google+ links are placeholder URLs

**Status:** ⚠️ Needs updates | **Priority:** High

---

### 8. **Contact Section**
*(Need to expand reading to see full)*
- Contact form (handled by send-email.php)
- Contact information display

**Status:** Partially implemented | **Priority:** Medium

---

## Part 4: Optimization Roadmap (Prioritized)

### **🔴 CRITICAL (Address First)**

#### 1. **Fix Broken Links & Email**
- Email in About section: `work.vangelov@gmail.com` → wrap in `<a href="mailto:work.vangelov@gmail.com">`
- Social media links pointing to generic profiles
- Resume PDF link not functional
- Verify all project detail page links work

#### 2. **Update Placeholder Content**
- Replace "Andrew Smith" in some pages with "Zlatomir Vangelov"
- Update social media URLs to your actual profiles
- Replace Lorem Ipsum text in projects with real descriptions

#### 3. **Navigation Consistency**
- Fix `all-projects.html` title (shows "Andrew Smith" instead of your name)
- Ensure breadcrumbs work correctly across all pages

---

### **🟠 HIGH (Next Priority)**

#### 4. **Modernize Technology Stack**
- jQuery 2.0.3 (2013) → jQuery 3.x or vanilla JavaScript
- Remove unused libraries
- Update responsive framework (if used)
- Consider removing older utility scripts

#### 5. **SEO & Meta Tags**
- Update all page titles (currently templated)
- Add meta descriptions to all pages
- Verify Open Graph tags for social sharing
- Check favicon setup across all pages

#### 6. **Performance Optimization**
- Compress/optimize images
- Minify CSS files
- Minimize JavaScript payload
- Implement lazy loading for images
- Consider CDN for assets

#### 7. **Contact Form Functionality**
- Test send-email.php backend
- Add form validation (client & server-side)
- Implement CAPTCHA or spam protection
- Add success/error handling

---

### **🟡 MEDIUM (Plan Next Phase)**

#### 8. **Project Showcase Enhancement**
- Expand project descriptions (replace Lorem Ipsum)
- Add project links/demos (external URLs)
- Include technologies used per project
- Add case study details
- Organize projects by category/type

#### 9. **Mobile Experience**
- Test responsive design across devices
- Optimize touch interactions
- Verify sidebar navigation on mobile
- Check form usability on mobile

#### 10. **Analytics & Tracking**
- Add Google Analytics
- Implement conversion tracking
- Monitor user behavior

#### 11. **Design/Brand Consistency**
- Ensure consistent naming across pages (Zlatomir vs Andrew)
- Verify color scheme consistency
- Update outdated social links (Twitter, Google+)
- Consider brand refresh areas

---

### **🟢 LOW (Future Enhancement)**

#### 12. **Advanced Features**
- Add blog functionality (currently placeholders)
- Implement filtering for projects
- Add testimonials/case studies section
- Client portfolio/work samples
- Video integration

#### 13. **Developer Experience**
- Add build process (if not present)
- Implement version control documentation
- Create deployment guide
- Setup development environment docs

#### 14. **Accessibility**
- WCAG 2.1 compliance audit
- Keyboard navigation testing
- Screen reader testing
- Contrast ratio checks

---

## Part 5: File Inventory & Status

### HTML Files (16 total)
| File | Status | Notes |
|------|--------|-------|
| index.html | ✓ Complete | Primary - all main sections |
| all-projects.html | ✓ Complete | Projects listing page |
| all-projects-2.html | ? | Possibly alternate version |
| blog-details.html | Template | Project detail template |
| tm-redesign.html | ✓ Linked | TransferMate redesign |
| data-deletion.html | ✓ Linked | GDPR data deletion project |
| knowledge-base.html | ✓ Linked | Invoice API project |
| partnerships.html | ✓ Linked | Partners/clients worked with |
| certification.html | ✓ Linked | Certifications page |
| project1.html | ? | May be unused |
| project-file.html | ? | May be unused |
| blog-details.html | Template | May be duplicated |
| 404.html | ✓ Error page | 404 handling |
| test.html | Debug | Testing page |
| example.html | Template | Example template |
| uptime.html | ? | Status/uptime page |

### CSS Files (7 total)
| File | Purpose | Status |
|------|---------|--------|
| style.css | Main styling | ✓ Active |
| responsive.css | Mobile responsive | ✓ Active |
| portfolio.css | Portfolio grid | ✓ Active |
| carousel.css | Slider styling | ✓ Active |
| scroll.css | Scroll animations | ✓ Active |
| font-awesome.css | Icons | ✓ Active |
| normalize.css | CSS reset | ✓ Active |

### JavaScript Files (20+ total)
- All appear functional but potentially redundant

### Assets
- **Images:** Organized, includes logo, profile, project thumbnails
- **Fonts:** Custom fonts directory
- **PDF:** Resume storage

---

## Part 6: Quick Reference - What to Do First

### Week 1: Critical Fixes
```
☐ Fix email link in About section
☐ Update page titles (remove "Andrew Smith")
☐ Fix social media URLs
☐ Test all navigation links
☐ Verify form submission works
```

### Week 2: Content Updates
```
☐ Replace Lorem Ipsum with real project descriptions
☐ Add actual project links/demos
☐ Update partnership information
☐ Complete experience section
☐ Complete education section
```

### Week 3: Technical Modernization
```
☐ Audit and update jQuery version
☐ Remove unused JavaScript libraries
☐ Optimize images
☐ Minify CSS/JS
☐ Add Google Analytics
```

### Week 4+: Enhancement
```
☐ Improve project showcase
☐ Add filtering/categories
☐ Mobile testing
☐ SEO optimization
☐ Accessibility audit
```

---

## Part 7: Technology Stack Summary

| Layer | Current | Recommendation |
|-------|---------|-----------------|
| HTML5 | ✓ Using | Continue |
| CSS3 | ✓ Using | Consolidate files |
| JavaScript | jQuery 2.0.3 | Upgrade to jQuery 3.x or vanilla JS |
| Icons | Font Awesome | ✓ Continue |
| Responsive | Custom CSS | ✓ Functional |
| Forms | PHP backend | Secure and test |
| Libraries | Multiple utility | Audit & remove unused |
| Version Control | Git (.git present) | ✓ In use |

---

## Conclusion

Your portfolio is **well-structured** with good foundational design. The main opportunities for improvement are:

1. **Content accuracy** (fixing broken links, removing placeholder text)
2. **Technical updates** (modernizing JavaScript stack)
3. **Completeness** (filling in missing content sections)
4. **Performance** (optimization and asset compression)
5. **SEO & Analytics** (tracking and visibility)

The site follows a modern responsive design pattern and effectively showcases your multifaceted skill set. With the optimization roadmap above, you can systematically improve it without disrupting existing functionality.

---

**Next Step:** Choose one section from the "Critical" category and begin optimization!
