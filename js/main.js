(function(){

    // ===== INTRO PRELOADER SEQUENCE =====
    var introOverlay = document.getElementById('intro-overlay');
    var introReady = false;

    if (introOverlay) {
        document.body.style.overflow = 'hidden';
        var letters = introOverlay.querySelectorAll('.intro-letter');
        var introName = introOverlay.querySelector('.intro-name');
        var introTitle = introOverlay.querySelector('.intro-title');
        var introLine = introOverlay.querySelector('.intro-line');

        // Step 1: Draw SVG letters
        anime({
            targets: Array.from(letters),
            strokeDashoffset: [400, 0],
            duration: 1400,
            delay: anime.stagger(200, { start: 300 }),
            easing: 'easeInOutCubic',
            complete: function() {
                // Step 2: Fade in name + title
                anime({
                    targets: introName,
                    opacity: [0, 1],
                    translateY: [12, 0],
                    duration: 600,
                    easing: 'easeOutCubic'
                });
                anime({
                    targets: introTitle,
                    opacity: [0, 1],
                    translateY: [12, 0],
                    duration: 600,
                    delay: 150,
                    easing: 'easeOutCubic'
                });
                // Step 3: Expand line
                anime({
                    targets: introLine,
                    width: ['0px', '120px'],
                    duration: 700,
                    delay: 300,
                    easing: 'easeOutCubic',
                    complete: function() {
                        // Step 4: Slide overlay up after brief hold
                        setTimeout(function() {
                            introOverlay.classList.add('done');
                            document.body.style.overflow = '';
                            introReady = true;
                            runHeroEntrance();
                            setTimeout(function() { introOverlay.classList.add('removed'); }, 1000);
                        }, 400);
                    }
                });
            }
        });
    } else {
        introReady = true;
    }

    function observeAndAnimate(selector, animationFn, options) {
        var els = document.querySelectorAll(selector);
        if (!els.length) return;
        var io = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) {
                if (e.isIntersecting) {
                    animationFn(e.target);
                    io.unobserve(e.target);
                }
            });
        }, options || { threshold: 0.08 });
        els.forEach(function(el) { io.observe(el); });
    }

    // ===== HERO ENTRANCE (index page) =====
    var hero = document.querySelector('.hero');
    var heroAnimated = false;

    if (hero) {
        var heroLabel = hero.querySelector('.hero-label');
        var heroH1 = hero.querySelector('h1');
        var heroP = hero.querySelector('p');
        var heroTags = hero.querySelectorAll('.hero-tag');
        var scrollInd = hero.querySelector('.scroll-indicator');

        var heroTargets = [heroLabel, heroH1, heroP].filter(Boolean);
        heroTargets.forEach(function(el) { el.style.opacity = '0'; el.style.transform = 'translateY(30px)'; });
        if (scrollInd) { scrollInd.style.opacity = '0'; }
        heroTags.forEach(function(tag) { tag.style.opacity = '0'; tag.style.transform = 'translateY(16px)'; });
    }

    function runHeroEntrance() {
        if (heroAnimated || !hero) return;
        heroAnimated = true;

        anime({
            targets: heroTargets,
            opacity: [0, 1],
            translateY: [30, 0],
            duration: 900,
            delay: anime.stagger(150, { start: 200 }),
            easing: 'easeOutCubic'
        });

        anime({
            targets: Array.from(heroTags),
            opacity: [0, 1],
            translateY: [16, 0],
            duration: 600,
            delay: anime.stagger(60, { start: 800 }),
            easing: 'easeOutCubic'
        });

        if (scrollInd) {
            anime({
                targets: scrollInd,
                opacity: [0, 1],
                duration: 800,
                delay: 1400,
                easing: 'easeOutCubic'
            });
        }
    }

    // If no intro overlay, run hero immediately
    if (!introOverlay) { runHeroEntrance(); }

    // ===== ABOUT CARDS =====
    observeAndAnimate('.about-grid', function(grid) {
        grid.style.opacity = '1';
        grid.style.transform = 'none';
        var cards = grid.querySelectorAll('.about-card');
        cards.forEach(function(c) { c.style.opacity = '0'; c.style.transform = 'translateY(40px)'; });
        anime({
            targets: Array.from(cards),
            opacity: [0, 1],
            translateY: [40, 0],
            duration: 700,
            delay: anime.stagger(100),
            easing: 'easeOutCubic'
        });
    }, { threshold: 0.1 });

    // ===== SKILL BARS =====
    var bars = document.querySelectorAll('.skill-fill');
    bars.forEach(function(bar) {
        var targetWidth = bar.style.width;
        bar.style.width = '0%';
        bar.setAttribute('data-target-width', targetWidth);
    });
    observeAndAnimate('.skills-grid', function(grid) {
        grid.style.opacity = '1';
        grid.style.transform = 'none';
        var fills = grid.querySelectorAll('.skill-fill');
        fills.forEach(function(bar, i) {
            var tw = bar.getAttribute('data-target-width') || '0%';
            anime({
                targets: bar,
                width: tw,
                duration: 1200,
                delay: i * 60,
                easing: 'easeOutExpo'
            });
        });
    }, { threshold: 0.2 });

    // Language bars
    var langBars = document.querySelectorAll('.lang-item .skill-fill');
    langBars.forEach(function(bar) {
        var tw = bar.style.width;
        bar.style.width = '0%';
        bar.setAttribute('data-target-width', tw);
    });
    observeAndAnimate('.language-section', function(section) {
        var fills = section.querySelectorAll('.skill-fill');
        fills.forEach(function(bar, i) {
            var tw = bar.getAttribute('data-target-width') || '0%';
            anime({
                targets: bar,
                width: tw,
                duration: 1200,
                delay: i * 120,
                easing: 'easeOutExpo'
            });
        });
    }, { threshold: 0.3 });

    // ===== TIMELINE ITEMS =====
    var timelineContainers = document.querySelectorAll('.timeline');
    timelineContainers.forEach(function(tl) {
        var items = tl.querySelectorAll('.timeline-item');
        items.forEach(function(item) { item.style.opacity = '0'; item.style.transform = 'translateX(-20px)'; });
    });
    observeAndAnimate('.timeline', function(tl) {
        var parent = tl.closest('.reveal');
        if (parent) { parent.style.opacity = '1'; parent.style.transform = 'none'; }
        tl.style.opacity = '1';
        tl.style.transform = 'none';
        var items = tl.querySelectorAll('.timeline-item');
        anime({
            targets: Array.from(items),
            opacity: [0, 1],
            translateX: [-20, 0],
            duration: 600,
            delay: anime.stagger(120),
            easing: 'easeOutCubic'
        });
    }, { threshold: 0.1 });

    // ===== FEATURED CARDS =====
    observeAndAnimate('.featured-grid', function(grid) {
        grid.style.opacity = '1';
        grid.style.transform = 'none';
        var cards = grid.querySelectorAll('.featured-card');
        cards.forEach(function(c) { c.style.opacity = '0'; c.style.transform = 'translateY(30px) scale(0.97)'; });
        anime({
            targets: Array.from(cards),
            opacity: [0, 1],
            translateY: [30, 0],
            scale: [0.97, 1],
            duration: 700,
            delay: anime.stagger(150),
            easing: 'easeOutCubic'
        });
    }, { threshold: 0.1 });

    // ===== PARTNER LOGOS =====
    observeAndAnimate('.partners-grid', function(grid) {
        var cards = grid.querySelectorAll('.partner-card');
        cards.forEach(function(c) { c.style.opacity = '0'; c.style.transform = 'scale(0.9)'; });
        anime({
            targets: Array.from(cards),
            opacity: [0, 1],
            scale: [0.9, 1],
            duration: 500,
            delay: anime.stagger(80),
            easing: 'easeOutCubic'
        });
    }, { threshold: 0.2 });

    // ===== CLOSING HERO =====
    var closingHero = document.querySelector('.closing-hero');
    if (closingHero) {
        var closingContent = closingHero.querySelector('.closing-content');
        if (closingContent) {
            closingContent.style.opacity = '0';
            closingContent.style.transform = 'translateY(20px)';
            observeAndAnimate('.closing-hero', function() {
                anime({
                    targets: closingContent,
                    opacity: [0, 1],
                    translateY: [20, 0],
                    duration: 1000,
                    easing: 'easeOutCubic'
                });
            }, { threshold: 0.3 });
        }
    }

    // ===== PROJECT CARDS (all-projects page) =====
    var tierSections = document.querySelectorAll('.tier-section');
    tierSections.forEach(function(tier) {
        var cards = tier.querySelectorAll('.project-card, .project-card-wrap');
        cards.forEach(function(c) { c.style.opacity = '0'; c.style.transform = 'translateY(24px)'; });
    });
    observeAndAnimate('.tier-section', function(tier) {
        var cards = tier.querySelectorAll('.project-card, .project-card-wrap');
        anime({
            targets: Array.from(cards),
            opacity: [0, 1],
            translateY: [24, 0],
            duration: 500,
            delay: anime.stagger(70),
            easing: 'easeOutCubic'
        });
    }, { threshold: 0.05 });

    // ===== HEADER STATS (all-projects) — count up =====
    var headerStats = document.querySelectorAll('.header-stat .num');
    if (headerStats.length) {
        headerStats.forEach(function(el) {
            var text = el.textContent.trim();
            var match = text.match(/^(\d+)(.*)$/);
            if (match) {
                el.setAttribute('data-count', match[1]);
                el.setAttribute('data-suffix', match[2]);
                el.textContent = '0' + match[2];
            }
        });
        observeAndAnimate('.header-stats', function(container) {
            var nums = container.querySelectorAll('.num[data-count]');
            nums.forEach(function(el, i) {
                var target = parseInt(el.getAttribute('data-count'));
                var suffix = el.getAttribute('data-suffix') || '';
                var obj = { val: 0 };
                anime({
                    targets: obj,
                    val: target,
                    round: 1,
                    duration: 1200,
                    delay: i * 150,
                    easing: 'easeOutExpo',
                    update: function() { el.textContent = obj.val + suffix; }
                });
            });
        }, { threshold: 0.5 });
    }

    // ===== CASE STUDY: STAT COUNTERS =====
    var counterEls = document.querySelectorAll('.stat-number[data-count]');
    if (counterEls.length) {
        counterEls.forEach(function(el) {
            el.textContent = '0' + (el.getAttribute('data-suffix') || '');
        });
        var counterIO = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) {
                if (e.isIntersecting) {
                    var el = e.target;
                    var target = parseInt(el.getAttribute('data-count'));
                    var suffix = el.getAttribute('data-suffix') || '';
                    var obj = { val: 0 };
                    anime({
                        targets: obj,
                        val: target,
                        round: 1,
                        duration: 1500,
                        easing: 'easeOutExpo',
                        update: function() { el.textContent = obj.val + suffix; }
                    });
                    counterIO.unobserve(el);
                }
            });
        }, { threshold: 0.5 });
        counterEls.forEach(function(el) { counterIO.observe(el); });
    }

    // ===== CASE STUDY: PROGRESS RING =====
    var ringEl = document.querySelector('.progress-ring-circle');
    if (ringEl) {
        ringEl.style.strokeDasharray = '0 439.8';
        var ringIO = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) {
                if (e.isIntersecting) {
                    anime({
                        targets: e.target,
                        strokeDasharray: ['0 439.8', '345.6 94.2'],
                        duration: 2000,
                        easing: 'easeOutCubic'
                    });
                    ringIO.unobserve(e.target);
                }
            });
        }, { threshold: 0.3 });
        ringIO.observe(ringEl);
    }

    // ===== CASE STUDY: SECTION REVEALS =====
    var caseReveals = document.querySelectorAll('.blog-details .reveal');
    if (caseReveals.length) {
        caseReveals.forEach(function(el) { el.style.opacity = '0'; el.style.transform = 'translateY(30px)'; });
        var revealIO = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) {
                if (e.isIntersecting) {
                    anime({
                        targets: e.target,
                        opacity: [0, 1],
                        translateY: [30, 0],
                        duration: 800,
                        easing: 'easeOutCubic'
                    });
                    revealIO.unobserve(e.target);
                }
            });
        }, { threshold: 0.08 });
        caseReveals.forEach(function(el) { revealIO.observe(el); });
    }

    // ===== GENERIC REVEAL (fallback for elements not handled by anime.js) =====
    var genericReveals = document.querySelectorAll('.reveal:not(.visible)');
    if (genericReveals.length) {
        var gIO = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) {
                if (e.isIntersecting) {
                    e.target.classList.add('visible');
                    gIO.unobserve(e.target);
                }
            });
        }, { threshold: 0.08 });
        genericReveals.forEach(function(el) {
            var dominated = el.closest('.blog-details') ||
                el.classList.contains('about-grid') || el.closest('.about-grid') ||
                el.classList.contains('featured-grid') || el.closest('.featured-grid') ||
                el.classList.contains('skills-grid') || el.closest('.skills-grid') ||
                el.classList.contains('timeline') ||
                el.classList.contains('partners-grid') || el.closest('.partners-grid');
            if (!dominated) {
                gIO.observe(el);
            }
        });
    }

    // ===== ACTIVE NAV HIGHLIGHT (index page) =====
    var navLinks = document.querySelectorAll('.sidebar nav a[href^="#"]');
    if (navLinks.length) {
        var sections = [];
        navLinks.forEach(function(l) { var id = l.getAttribute('href').slice(1); var el = document.getElementById(id); if (el) sections.push({ el: el, link: l }); });
        if (sections.length) {
            window.addEventListener('scroll', function() {
                var y = window.scrollY + 200;
                var active = sections[0];
                sections.forEach(function(s) { if (s.el.offsetTop <= y) active = s; });
                if ((window.innerHeight + window.scrollY) >= (document.body.scrollHeight - 100)) {
                    active = sections[sections.length - 1];
                }
                navLinks.forEach(function(l) { l.classList.remove('active'); });
                if (active) active.link.classList.add('active');
            });
        }
    }

    // ===== FILTER (all-projects page) =====
    var filterBtns = document.querySelectorAll('.filter-btn');
    if (filterBtns.length) {
        var cards = document.querySelectorAll('.project-card');
        var wraps = document.querySelectorAll('.project-card-wrap');
        var tiers = document.querySelectorAll('.tier-section');
        filterBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                filterBtns.forEach(function(b) { b.classList.remove('active'); });
                btn.classList.add('active');
                var filter = btn.getAttribute('data-filter');

                if (filter === 'all') {
                    cards.forEach(function(c) { c.style.display = ''; c.style.opacity = '1'; c.style.transform = ''; });
                    wraps.forEach(function(w) { w.style.display = ''; w.style.opacity = '1'; w.style.transform = ''; });
                    tiers.forEach(function(t) { t.style.display = ''; });
                } else {
                    cards.forEach(function(c) {
                        c.style.display = c.getAttribute('data-category') === filter ? '' : 'none';
                    });
                    wraps.forEach(function(w) {
                        w.style.display = w.getAttribute('data-category') === filter ? '' : 'none';
                    });
                    tiers.forEach(function(t) {
                        var visible = t.querySelectorAll('.project-card:not([style*="display: none"]), .project-card-wrap:not([style*="display: none"])');
                        t.style.display = visible.length ? '' : 'none';
                    });
                }

                var visibleCards = [];
                tiers.forEach(function(t) {
                    if (t.style.display !== 'none') {
                        t.querySelectorAll('.project-card:not([style*="display: none"]), .project-card-wrap:not([style*="display: none"])').forEach(function(c) {
                            visibleCards.push(c);
                        });
                    }
                });
                anime({
                    targets: visibleCards,
                    opacity: [0, 1],
                    translateY: [16, 0],
                    duration: 400,
                    delay: anime.stagger(40),
                    easing: 'easeOutCubic'
                });
            });
        });
    }

})();
