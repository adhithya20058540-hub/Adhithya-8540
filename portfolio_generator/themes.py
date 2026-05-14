"""
themes.py - Theme definitions for Portfolio Generator
Each theme includes CSS variables, fonts, and structural styling
for a unique visual identity.
"""

# ─────────────────────────────────────────────
#  THEME REGISTRY
# ─────────────────────────────────────────────

THEMES = {
    "light_minimal": {
        "id": "light_minimal",
        "label": "Light Minimal",
        "type": "light",
        "description": "Clean white modern style — crisp typography, lots of breathing room.",
        "icon": "☀️",
    },
    "light_professional": {
        "id": "light_professional",
        "label": "Light Professional",
        "type": "light",
        "description": "Blue-gray corporate style — polished, trustworthy, business-ready.",
        "icon": "🏢",
    },
    "dark_neon": {
        "id": "dark_neon",
        "label": "Dark Neon",
        "type": "dark",
        "description": "Black background with glowing neon accents — bold and electric.",
        "icon": "⚡",
    },
    "dark_elegant": {
        "id": "dark_elegant",
        "label": "Dark Elegant",
        "type": "dark",
        "description": "Dark gray with gold premium styling — refined, luxurious, sophisticated.",
        "icon": "✨",
    },
}


def get_theme_css(theme_id: str) -> str:
    """Return the full CSS string for the given theme."""
    generators = {
        "light_minimal": _light_minimal_css,
        "light_professional": _light_professional_css,
        "dark_neon": _dark_neon_css,
        "dark_elegant": _dark_elegant_css,
    }
    fn = generators.get(theme_id)
    if not fn:
        raise ValueError(f"Unknown theme: '{theme_id}'")
    return fn()


# ─────────────────────────────────────────────
#  THEME 1 – LIGHT MINIMAL
# ─────────────────────────────────────────────

def _light_minimal_css() -> str:
    return """
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Serif+Display&display=swap');

    :root {
      --bg: #ffffff;
      --bg-alt: #f7f7f5;
      --surface: #ffffff;
      --border: #e8e8e4;
      --text: #1a1a18;
      --text-muted: #737370;
      --accent: #2d6a4f;
      --accent-light: #e8f5ee;
      --accent-hover: #1e4d37;
      --hero-bg: #f0f4f1;
      --card-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 4px 16px rgba(0,0,0,0.04);
      --font-heading: 'DM Serif Display', Georgia, serif;
      --font-body: 'DM Sans', sans-serif;
      --radius: 4px;
      --radius-lg: 8px;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      font-family: var(--font-body);
      background: var(--bg);
      color: var(--text);
      font-size: 16px;
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
    }

    /* NAV */
    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      background: rgba(255,255,255,0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 0 5%;
      display: flex; align-items: center; justify-content: space-between;
      height: 64px;
    }
    .nav-logo {
      font-family: var(--font-heading);
      font-size: 1.3rem;
      color: var(--text);
      text-decoration: none;
    }
    .nav-links { display: flex; gap: 2rem; list-style: none; }
    .nav-links a {
      text-decoration: none; color: var(--text-muted);
      font-size: 0.875rem; font-weight: 500; letter-spacing: 0.02em;
      transition: color 0.2s;
    }
    .nav-links a:hover { color: var(--accent); }

    /* HERO */
    #hero {
      min-height: 100vh;
      background: var(--hero-bg);
      display: flex; align-items: center;
      padding: 100px 5% 80px;
    }
    .hero-inner {
      max-width: 1100px; margin: 0 auto; width: 100%;
      display: grid; grid-template-columns: 1fr 340px;
      gap: 60px; align-items: center;
    }
    .hero-tag {
      display: inline-block;
      background: var(--accent-light); color: var(--accent);
      font-size: 0.8rem; font-weight: 600; letter-spacing: 0.08em;
      text-transform: uppercase; padding: 5px 14px;
      border-radius: 100px; margin-bottom: 1.5rem;
    }
    .hero-name {
      font-family: var(--font-heading);
      font-size: clamp(2.4rem, 5vw, 3.8rem);
      line-height: 1.15;
      color: var(--text);
      margin-bottom: 1.2rem;
    }
    .hero-bio {
      color: var(--text-muted);
      font-size: 1.05rem; max-width: 520px;
      margin-bottom: 2rem;
    }
    .btn-primary {
      display: inline-block;
      background: var(--accent); color: #fff;
      padding: 13px 28px; border-radius: var(--radius);
      text-decoration: none; font-weight: 600;
      font-size: 0.9rem; letter-spacing: 0.02em;
      transition: background 0.2s, transform 0.15s;
    }
    .btn-primary:hover { background: var(--accent-hover); transform: translateY(-1px); }
    .btn-secondary {
      display: inline-block;
      border: 1.5px solid var(--border); color: var(--text);
      padding: 12px 28px; border-radius: var(--radius);
      text-decoration: none; font-weight: 500;
      font-size: 0.9rem; margin-left: 12px;
      transition: border-color 0.2s, color 0.2s;
    }
    .btn-secondary:hover { border-color: var(--accent); color: var(--accent); }
    .hero-photo {
      width: 300px; height: 300px;
      border-radius: 50%; object-fit: cover;
      border: 3px solid var(--border);
      box-shadow: var(--card-shadow);
    }
    .hero-photo-placeholder {
      width: 300px; height: 300px; border-radius: 50%;
      background: var(--accent-light);
      display: flex; align-items: center; justify-content: center;
      font-family: var(--font-heading); font-size: 5rem; color: var(--accent);
    }

    /* SECTIONS */
    section { padding: 100px 5%; }
    .section-inner { max-width: 1100px; margin: 0 auto; }
    .section-label {
      font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em;
      text-transform: uppercase; color: var(--accent);
      margin-bottom: 0.6rem;
    }
    .section-title {
      font-family: var(--font-heading);
      font-size: clamp(1.8rem, 3vw, 2.6rem);
      color: var(--text); margin-bottom: 3rem;
    }
    .section-divider {
      width: 40px; height: 2px; background: var(--accent);
      margin: 1rem 0 3rem;
    }

    /* ABOUT */
    #about { background: var(--bg); }
    .about-grid {
      display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: start;
    }
    .about-text p { color: var(--text-muted); margin-bottom: 1rem; }

    /* SKILLS */
    #skills { background: var(--bg-alt); }
    .skills-grid {
      display: flex; flex-wrap: wrap; gap: 10px;
    }
    .skill-tag {
      background: var(--surface); border: 1px solid var(--border);
      color: var(--text); padding: 8px 18px;
      border-radius: 100px; font-size: 0.875rem; font-weight: 500;
      transition: border-color 0.2s, color 0.2s;
    }
    .skill-tag:hover { border-color: var(--accent); color: var(--accent); }

    /* EDUCATION */
    #education { background: var(--bg); }
    .edu-list { display: flex; flex-direction: column; gap: 24px; }
    .edu-card {
      background: var(--bg-alt); border: 1px solid var(--border);
      border-radius: var(--radius-lg); padding: 28px 32px;
      border-left: 3px solid var(--accent);
    }
    .edu-degree { font-weight: 700; font-size: 1.05rem; margin-bottom: 4px; }
    .edu-meta { color: var(--accent); font-size: 0.875rem; font-weight: 500; margin-bottom: 8px; }
    .edu-desc { color: var(--text-muted); font-size: 0.9rem; }

    /* PROJECTS */
    #projects { background: var(--bg-alt); }
    .projects-grid {
      display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 24px;
    }
    .project-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: var(--radius-lg); padding: 32px;
      box-shadow: var(--card-shadow);
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .project-card:hover { transform: translateY(-3px); box-shadow: 0 8px 32px rgba(0,0,0,0.1); }
    .project-name { font-family: var(--font-heading); font-size: 1.25rem; margin-bottom: 10px; }
    .project-desc { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 16px; }
    .project-tech { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
    .tech-badge {
      background: var(--accent-light); color: var(--accent);
      font-size: 0.75rem; font-weight: 600; padding: 3px 10px;
      border-radius: 100px;
    }
    .project-link {
      color: var(--accent); font-weight: 600; font-size: 0.875rem;
      text-decoration: none;
    }
    .project-link:hover { text-decoration: underline; }

    /* EXPERIENCE */
    #experience { background: var(--bg); }
    .exp-timeline { display: flex; flex-direction: column; gap: 0; }
    .exp-item {
      display: grid; grid-template-columns: 160px 1fr;
      gap: 40px; padding-bottom: 40px;
      border-left: 1px solid var(--border); margin-left: 20px; padding-left: 40px;
      position: relative;
    }
    .exp-item::before {
      content: ''; position: absolute; left: -5px; top: 6px;
      width: 9px; height: 9px; border-radius: 50%;
      background: var(--accent); border: 2px solid var(--bg);
    }
    .exp-period { color: var(--text-muted); font-size: 0.85rem; font-weight: 500; padding-top: 4px; }
    .exp-role { font-weight: 700; font-size: 1.05rem; margin-bottom: 4px; }
    .exp-company { color: var(--accent); font-weight: 600; font-size: 0.9rem; margin-bottom: 10px; }
    .exp-desc { color: var(--text-muted); font-size: 0.9rem; }

    /* CONTACT */
    #contact { background: var(--bg-alt); }
    .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: start; }
    .contact-item { display: flex; gap: 14px; margin-bottom: 24px; align-items: flex-start; }
    .contact-icon {
      width: 42px; height: 42px; border-radius: 50%;
      background: var(--accent-light); color: var(--accent);
      display: flex; align-items: center; justify-content: center;
      font-size: 1.1rem; flex-shrink: 0;
    }
    .contact-label { font-size: 0.75rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; color: var(--text-muted); }
    .contact-value { color: var(--text); font-weight: 500; }
    .contact-value a { color: var(--accent); text-decoration: none; }
    .contact-value a:hover { text-decoration: underline; }

    /* FOOTER */
    footer {
      background: var(--text); color: rgba(255,255,255,0.6);
      text-align: center; padding: 32px;
      font-size: 0.85rem;
    }
    footer strong { color: #fff; }

    @media (max-width: 768px) {
      .hero-inner { grid-template-columns: 1fr; }
      .hero-photo, .hero-photo-placeholder { display: none; }
      .about-grid, .contact-grid { grid-template-columns: 1fr; gap: 40px; }
      .exp-item { grid-template-columns: 1fr; gap: 4px; }
      .nav-links { display: none; }
    }
    """


# ─────────────────────────────────────────────
#  THEME 2 – LIGHT PROFESSIONAL
# ─────────────────────────────────────────────

def _light_professional_css() -> str:
    return """
    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

    :root {
      --bg: #f4f6f9;
      --surface: #ffffff;
      --bg-alt: #eef1f6;
      --border: #d6dce8;
      --text: #1c2b3a;
      --text-muted: #5a6e82;
      --accent: #1e4d8c;
      --accent-2: #2a7fc9;
      --accent-light: #deeaf8;
      --hero-bg: linear-gradient(135deg, #1e3a6e 0%, #1e4d8c 50%, #2a7fc9 100%);
      --card-shadow: 0 2px 8px rgba(30,77,140,0.08), 0 1px 2px rgba(0,0,0,0.04);
      --font-heading: 'Source Serif 4', Georgia, serif;
      --font-body: 'IBM Plex Sans', sans-serif;
      --radius: 6px;
      --radius-lg: 10px;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      font-family: var(--font-body);
      background: var(--bg);
      color: var(--text);
      font-size: 16px;
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
    }

    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 0 5%;
      display: flex; align-items: center; justify-content: space-between;
      height: 68px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .nav-logo {
      font-family: var(--font-heading);
      font-size: 1.2rem; font-weight: 700;
      color: var(--accent); text-decoration: none;
    }
    .nav-links { display: flex; gap: 2.5rem; list-style: none; }
    .nav-links a {
      text-decoration: none; color: var(--text-muted);
      font-size: 0.875rem; font-weight: 500;
      padding-bottom: 2px;
      border-bottom: 2px solid transparent;
      transition: color 0.2s, border-color 0.2s;
    }
    .nav-links a:hover { color: var(--accent); border-color: var(--accent-2); }

    #hero {
      min-height: 100vh;
      background: var(--hero-bg);
      display: flex; align-items: center;
      padding: 100px 5% 80px;
      position: relative; overflow: hidden;
    }
    #hero::after {
      content: '';
      position: absolute; bottom: -1px; left: 0; right: 0; height: 80px;
      background: var(--bg);
      clip-path: ellipse(55% 100% at 50% 100%);
    }
    .hero-inner {
      max-width: 1100px; margin: 0 auto; width: 100%;
      display: grid; grid-template-columns: 1fr 320px;
      gap: 60px; align-items: center; position: relative; z-index: 1;
    }
    .hero-tag {
      display: inline-block;
      background: rgba(255,255,255,0.15); color: rgba(255,255,255,0.9);
      font-size: 0.78rem; font-weight: 600; letter-spacing: 0.1em;
      text-transform: uppercase; padding: 5px 14px;
      border-radius: 100px; margin-bottom: 1.5rem;
      border: 1px solid rgba(255,255,255,0.25);
    }
    .hero-name {
      font-family: var(--font-heading);
      font-size: clamp(2.2rem, 4.5vw, 3.5rem);
      line-height: 1.2; color: #ffffff;
      margin-bottom: 1rem;
    }
    .hero-bio { color: rgba(255,255,255,0.75); font-size: 1rem; max-width: 500px; margin-bottom: 2rem; }
    .btn-primary {
      display: inline-block;
      background: #ffffff; color: var(--accent);
      padding: 13px 28px; border-radius: var(--radius);
      text-decoration: none; font-weight: 600;
      font-size: 0.9rem; transition: background 0.2s, transform 0.15s;
    }
    .btn-primary:hover { background: #e8f0fa; transform: translateY(-1px); }
    .btn-secondary {
      display: inline-block;
      border: 1.5px solid rgba(255,255,255,0.5); color: rgba(255,255,255,0.9);
      padding: 12px 28px; border-radius: var(--radius);
      text-decoration: none; font-weight: 500;
      font-size: 0.9rem; margin-left: 12px;
      transition: border-color 0.2s, color 0.2s;
    }
    .btn-secondary:hover { border-color: #fff; color: #fff; }
    .hero-photo {
      width: 280px; height: 280px;
      border-radius: var(--radius-lg); object-fit: cover;
      border: 4px solid rgba(255,255,255,0.3);
      box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    .hero-photo-placeholder {
      width: 280px; height: 280px;
      border-radius: var(--radius-lg);
      background: rgba(255,255,255,0.15);
      display: flex; align-items: center; justify-content: center;
      font-family: var(--font-heading); font-size: 5rem; color: rgba(255,255,255,0.7);
      border: 4px solid rgba(255,255,255,0.25);
    }

    section { padding: 90px 5%; }
    .section-inner { max-width: 1100px; margin: 0 auto; }
    .section-label {
      font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em;
      text-transform: uppercase; color: var(--accent-2); margin-bottom: 0.5rem;
    }
    .section-title {
      font-family: var(--font-heading);
      font-size: clamp(1.8rem, 3vw, 2.4rem);
      color: var(--text); margin-bottom: 2.5rem;
    }
    .section-divider {
      width: 48px; height: 3px;
      background: linear-gradient(90deg, var(--accent), var(--accent-2));
      margin: 0.8rem 0 3rem;
      border-radius: 2px;
    }

    #about { background: var(--surface); }
    .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: start; }
    .about-text p { color: var(--text-muted); margin-bottom: 1rem; }

    .stat-box {
      background: var(--bg); border: 1px solid var(--border);
      border-radius: var(--radius-lg); padding: 24px;
      text-align: center; margin-bottom: 12px;
    }
    .stat-number { font-family: var(--font-heading); font-size: 2.5rem; color: var(--accent); font-weight: 700; }
    .stat-label { color: var(--text-muted); font-size: 0.85rem; font-weight: 500; }
    .stats-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }

    #skills { background: var(--bg); }
    .skills-grid { display: flex; flex-wrap: wrap; gap: 10px; }
    .skill-tag {
      background: var(--surface); border: 1px solid var(--border);
      color: var(--text); padding: 8px 18px;
      border-radius: var(--radius); font-size: 0.875rem; font-weight: 500;
      box-shadow: var(--card-shadow);
      transition: all 0.2s;
    }
    .skill-tag:hover { background: var(--accent-light); border-color: var(--accent); color: var(--accent); }

    #education { background: var(--surface); }
    .edu-list { display: flex; flex-direction: column; gap: 20px; }
    .edu-card {
      background: var(--bg); border: 1px solid var(--border);
      border-radius: var(--radius-lg); padding: 28px 32px;
      display: grid; grid-template-columns: auto 1fr; gap: 24px; align-items: start;
    }
    .edu-year-badge {
      background: var(--accent); color: white;
      font-size: 0.85rem; font-weight: 700;
      padding: 6px 14px; border-radius: var(--radius);
      white-space: nowrap;
    }
    .edu-degree { font-weight: 700; font-size: 1.05rem; margin-bottom: 4px; }
    .edu-meta { color: var(--accent-2); font-size: 0.875rem; font-weight: 500; margin-bottom: 8px; }
    .edu-desc { color: var(--text-muted); font-size: 0.9rem; }

    #projects { background: var(--bg); }
    .projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px; }
    .project-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: var(--radius-lg); padding: 28px;
      box-shadow: var(--card-shadow);
      transition: transform 0.2s, box-shadow 0.2s;
      border-top: 3px solid var(--accent);
    }
    .project-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(30,77,140,0.12); }
    .project-name { font-family: var(--font-heading); font-size: 1.2rem; margin-bottom: 10px; color: var(--text); }
    .project-desc { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 16px; }
    .project-tech { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 18px; }
    .tech-badge {
      background: var(--accent-light); color: var(--accent);
      font-size: 0.75rem; font-weight: 600; padding: 3px 10px; border-radius: var(--radius);
    }
    .project-link { color: var(--accent-2); font-weight: 600; font-size: 0.875rem; text-decoration: none; }
    .project-link:hover { text-decoration: underline; }

    #experience { background: var(--surface); }
    .exp-timeline { display: flex; flex-direction: column; gap: 0; }
    .exp-item {
      display: grid; grid-template-columns: 180px 1fr;
      gap: 40px; padding-bottom: 40px;
      border-left: 2px solid var(--border); margin-left: 20px; padding-left: 40px;
      position: relative;
    }
    .exp-item::before {
      content: ''; position: absolute; left: -7px; top: 6px;
      width: 12px; height: 12px; border-radius: 2px;
      background: var(--accent);
    }
    .exp-period { color: var(--text-muted); font-size: 0.82rem; font-weight: 600; padding-top: 4px; letter-spacing: 0.02em; }
    .exp-role { font-weight: 700; font-size: 1.05rem; margin-bottom: 4px; }
    .exp-company { color: var(--accent-2); font-weight: 600; font-size: 0.9rem; margin-bottom: 10px; }
    .exp-desc { color: var(--text-muted); font-size: 0.9rem; }

    #contact { background: var(--accent); }
    #contact .section-label { color: rgba(255,255,255,0.6); }
    #contact .section-title { color: #ffffff; }
    #contact .section-divider { background: rgba(255,255,255,0.4); }
    .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: start; }
    .contact-item { display: flex; gap: 14px; margin-bottom: 20px; align-items: center; }
    .contact-icon {
      width: 44px; height: 44px; border-radius: var(--radius);
      background: rgba(255,255,255,0.15); color: white;
      display: flex; align-items: center; justify-content: center;
      font-size: 1.1rem; flex-shrink: 0;
    }
    .contact-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: rgba(255,255,255,0.5); }
    .contact-value { color: #ffffff; font-weight: 500; }
    .contact-value a { color: rgba(255,255,255,0.85); text-decoration: none; }
    .contact-value a:hover { color: #fff; text-decoration: underline; }
    .contact-cta p { color: rgba(255,255,255,0.8); margin-bottom: 1.5rem; font-size: 1.05rem; }
    .btn-contact {
      display: inline-block;
      background: white; color: var(--accent);
      padding: 14px 32px; border-radius: var(--radius);
      text-decoration: none; font-weight: 700; font-size: 0.95rem;
      transition: background 0.2s;
    }
    .btn-contact:hover { background: #e8f0fa; }

    footer {
      background: var(--text); color: rgba(255,255,255,0.5);
      text-align: center; padding: 32px; font-size: 0.85rem;
    }
    footer strong { color: rgba(255,255,255,0.85); }

    @media (max-width: 768px) {
      .hero-inner { grid-template-columns: 1fr; }
      .hero-photo, .hero-photo-placeholder { display: none; }
      .about-grid, .contact-grid { grid-template-columns: 1fr; gap: 40px; }
      .exp-item { grid-template-columns: 1fr; gap: 4px; }
      .edu-card { grid-template-columns: 1fr; }
      .nav-links { display: none; }
    }
    """


# ─────────────────────────────────────────────
#  THEME 3 – DARK NEON
# ─────────────────────────────────────────────

def _dark_neon_css() -> str:
    return """
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Rajdhani:wght@400;500;600;700&display=swap');

    :root {
      --bg: #050508;
      --bg-alt: #0a0a10;
      --surface: #0f0f18;
      --border: #1e1e30;
      --text: #e8e8f0;
      --text-muted: #6b6b88;
      --neon-cyan: #00f5ff;
      --neon-pink: #ff00aa;
      --neon-purple: #bf00ff;
      --accent: #00f5ff;
      --accent-glow: rgba(0,245,255,0.15);
      --accent-glow-strong: rgba(0,245,255,0.3);
      --card-border: rgba(0,245,255,0.15);
      --font-heading: 'Rajdhani', sans-serif;
      --font-mono: 'Space Mono', monospace;
      --radius: 2px;
      --radius-lg: 4px;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      font-family: var(--font-heading);
      background: var(--bg);
      color: var(--text);
      font-size: 16px;
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
    }

    /* Scanline effect */
    body::before {
      content: '';
      position: fixed; top: 0; left: 0; right: 0; bottom: 0;
      background: repeating-linear-gradient(
        0deg, transparent, transparent 2px,
        rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px
      );
      pointer-events: none; z-index: 999;
    }

    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      background: rgba(5,5,8,0.9);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--neon-cyan);
      box-shadow: 0 0 20px rgba(0,245,255,0.1);
      padding: 0 5%;
      display: flex; align-items: center; justify-content: space-between;
      height: 64px;
    }
    .nav-logo {
      font-family: var(--font-mono);
      font-size: 1rem; color: var(--neon-cyan);
      text-decoration: none;
      text-shadow: 0 0 10px var(--neon-cyan);
    }
    .nav-links { display: flex; gap: 2.5rem; list-style: none; }
    .nav-links a {
      text-decoration: none; color: var(--text-muted);
      font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em;
      text-transform: uppercase;
      transition: color 0.2s, text-shadow 0.2s;
    }
    .nav-links a:hover { color: var(--neon-cyan); text-shadow: 0 0 8px var(--neon-cyan); }

    #hero {
      min-height: 100vh;
      display: flex; align-items: center;
      padding: 100px 5% 80px;
      background: var(--bg);
      position: relative; overflow: hidden;
    }
    /* Grid overlay */
    #hero::before {
      content: '';
      position: absolute; inset: 0;
      background-image:
        linear-gradient(rgba(0,245,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,245,255,0.03) 1px, transparent 1px);
      background-size: 60px 60px;
    }
    .hero-inner {
      max-width: 1100px; margin: 0 auto; width: 100%;
      display: grid; grid-template-columns: 1fr 320px;
      gap: 60px; align-items: center; position: relative; z-index: 1;
    }
    .hero-tag {
      display: inline-block; font-family: var(--font-mono);
      background: transparent; color: var(--neon-cyan);
      font-size: 0.78rem; letter-spacing: 0.12em;
      text-transform: uppercase; margin-bottom: 1.5rem;
    }
    .hero-tag::before { content: '> '; }
    .hero-name {
      font-family: var(--font-heading);
      font-size: clamp(2.8rem, 6vw, 5rem);
      font-weight: 700; line-height: 1.05;
      color: #ffffff;
      text-transform: uppercase; letter-spacing: -0.02em;
      margin-bottom: 1rem;
    }
    .hero-name span {
      color: var(--neon-cyan);
      text-shadow: 0 0 20px var(--neon-cyan), 0 0 60px rgba(0,245,255,0.4);
    }
    .hero-bio {
      color: var(--text-muted); font-size: 0.95rem; max-width: 480px;
      margin-bottom: 2.5rem; font-family: var(--font-mono); line-height: 1.8;
    }
    .btn-primary {
      display: inline-block;
      background: transparent; color: var(--neon-cyan);
      padding: 12px 28px;
      border: 1px solid var(--neon-cyan);
      box-shadow: 0 0 12px rgba(0,245,255,0.2), inset 0 0 12px rgba(0,245,255,0.05);
      text-decoration: none; font-weight: 700;
      font-size: 0.82rem; letter-spacing: 0.1em; text-transform: uppercase;
      transition: all 0.2s;
    }
    .btn-primary:hover {
      background: rgba(0,245,255,0.1);
      box-shadow: 0 0 24px rgba(0,245,255,0.4), inset 0 0 24px rgba(0,245,255,0.1);
    }
    .btn-secondary {
      display: inline-block;
      border: 1px solid var(--neon-pink); color: var(--neon-pink);
      padding: 12px 28px;
      text-decoration: none; font-weight: 700;
      font-size: 0.82rem; letter-spacing: 0.1em; text-transform: uppercase;
      margin-left: 12px;
      box-shadow: 0 0 12px rgba(255,0,170,0.2);
      transition: all 0.2s;
    }
    .btn-secondary:hover {
      background: rgba(255,0,170,0.1);
      box-shadow: 0 0 24px rgba(255,0,170,0.4);
    }
    .hero-photo {
      width: 280px; height: 280px; object-fit: cover;
      border: 1px solid var(--neon-cyan);
      box-shadow: 0 0 30px rgba(0,245,255,0.2), 0 0 80px rgba(0,245,255,0.1);
      filter: saturate(0.8) contrast(1.1);
    }
    .hero-photo-placeholder {
      width: 280px; height: 280px;
      background: var(--surface);
      border: 1px solid var(--neon-cyan);
      box-shadow: 0 0 30px rgba(0,245,255,0.2);
      display: flex; align-items: center; justify-content: center;
      font-size: 5rem;
    }

    section { padding: 90px 5%; }
    .section-inner { max-width: 1100px; margin: 0 auto; }
    .section-label {
      font-family: var(--font-mono); font-size: 0.72rem;
      letter-spacing: 0.15em; text-transform: uppercase;
      color: var(--neon-cyan); margin-bottom: 0.5rem;
    }
    .section-label::before { content: '// '; }
    .section-title {
      font-family: var(--font-heading);
      font-size: clamp(2rem, 3.5vw, 3rem);
      font-weight: 700; text-transform: uppercase;
      letter-spacing: 0.02em; color: var(--text);
      margin-bottom: 1rem;
    }
    .section-divider {
      width: 60px; height: 1px;
      background: linear-gradient(90deg, var(--neon-cyan), transparent);
      margin: 0.5rem 0 3rem;
    }

    #about { background: var(--bg-alt); }
    .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: start; }
    .about-text p { color: var(--text-muted); margin-bottom: 1rem; font-family: var(--font-mono); font-size: 0.9rem; line-height: 1.9; }

    #skills { background: var(--bg); }
    .skills-grid { display: flex; flex-wrap: wrap; gap: 10px; }
    .skill-tag {
      background: var(--surface);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      padding: 7px 16px;
      font-family: var(--font-mono); font-size: 0.8rem;
      transition: all 0.2s;
    }
    .skill-tag:hover {
      border-color: var(--neon-cyan); color: var(--neon-cyan);
      box-shadow: 0 0 10px rgba(0,245,255,0.2);
    }

    #education { background: var(--bg-alt); }
    .edu-list { display: flex; flex-direction: column; gap: 16px; }
    .edu-card {
      background: var(--surface);
      border: 1px solid var(--card-border);
      padding: 24px 28px;
      border-left: 2px solid var(--neon-cyan);
      box-shadow: -4px 0 16px rgba(0,245,255,0.05);
    }
    .edu-degree { font-weight: 700; font-size: 1.05rem; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.03em; }
    .edu-meta { color: var(--neon-cyan); font-size: 0.82rem; font-family: var(--font-mono); margin-bottom: 8px; }
    .edu-desc { color: var(--text-muted); font-size: 0.85rem; font-family: var(--font-mono); line-height: 1.7; }

    #projects { background: var(--bg); }
    .projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 20px; }
    .project-card {
      background: var(--surface);
      border: 1px solid var(--card-border);
      padding: 28px;
      position: relative; overflow: hidden;
      transition: all 0.3s;
    }
    .project-card::before {
      content: ''; position: absolute;
      top: 0; left: 0; right: 0; height: 1px;
      background: linear-gradient(90deg, var(--neon-cyan), var(--neon-pink));
    }
    .project-card:hover {
      border-color: rgba(0,245,255,0.3);
      box-shadow: 0 0 30px rgba(0,245,255,0.1);
      transform: translateY(-2px);
    }
    .project-name { font-weight: 700; font-size: 1.1rem; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.03em; }
    .project-desc { color: var(--text-muted); font-size: 0.85rem; font-family: var(--font-mono); margin-bottom: 16px; line-height: 1.7; }
    .project-tech { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 18px; }
    .tech-badge {
      background: transparent; border: 1px solid rgba(191,0,255,0.4); color: var(--neon-purple);
      font-family: var(--font-mono); font-size: 0.72rem; padding: 2px 8px;
    }
    .project-link { color: var(--neon-cyan); font-family: var(--font-mono); font-size: 0.8rem; text-decoration: none; }
    .project-link::before { content: '→ '; }
    .project-link:hover { text-shadow: 0 0 8px var(--neon-cyan); }

    #experience { background: var(--bg-alt); }
    .exp-timeline { display: flex; flex-direction: column; gap: 0; }
    .exp-item {
      display: grid; grid-template-columns: 160px 1fr;
      gap: 40px; padding-bottom: 40px;
      border-left: 1px solid rgba(0,245,255,0.15); margin-left: 20px; padding-left: 40px;
      position: relative;
    }
    .exp-item::before {
      content: ''; position: absolute; left: -4px; top: 6px;
      width: 7px; height: 7px;
      background: var(--neon-cyan);
      box-shadow: 0 0 10px var(--neon-cyan);
    }
    .exp-period { color: var(--text-muted); font-family: var(--font-mono); font-size: 0.78rem; padding-top: 4px; }
    .exp-role { font-weight: 700; font-size: 1rem; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.04em; }
    .exp-company { color: var(--neon-cyan); font-family: var(--font-mono); font-size: 0.82rem; margin-bottom: 10px; }
    .exp-desc { color: var(--text-muted); font-size: 0.85rem; font-family: var(--font-mono); line-height: 1.7; }

    #contact { background: var(--bg); }
    .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: start; }
    .contact-item { display: flex; gap: 14px; margin-bottom: 20px; align-items: flex-start; }
    .contact-icon {
      width: 40px; height: 40px;
      border: 1px solid var(--neon-cyan);
      color: var(--neon-cyan);
      display: flex; align-items: center; justify-content: center;
      font-size: 1rem; flex-shrink: 0;
      box-shadow: 0 0 8px rgba(0,245,255,0.15);
    }
    .contact-label { font-family: var(--font-mono); font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-muted); }
    .contact-value { color: var(--text); font-family: var(--font-mono); font-size: 0.9rem; }
    .contact-value a { color: var(--neon-cyan); text-decoration: none; }
    .contact-value a:hover { text-shadow: 0 0 8px var(--neon-cyan); }

    footer {
      background: var(--bg-alt);
      border-top: 1px solid rgba(0,245,255,0.15);
      text-align: center; padding: 28px;
      font-family: var(--font-mono); font-size: 0.78rem;
      color: var(--text-muted);
    }

    @media (max-width: 768px) {
      .hero-inner { grid-template-columns: 1fr; }
      .hero-photo, .hero-photo-placeholder { display: none; }
      .about-grid, .contact-grid { grid-template-columns: 1fr; gap: 40px; }
      .exp-item { grid-template-columns: 1fr; gap: 4px; }
      .nav-links { display: none; }
    }
    """


# ─────────────────────────────────────────────
#  THEME 4 – DARK ELEGANT
# ─────────────────────────────────────────────

def _dark_elegant_css() -> str:
    return """
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Jost:wght@300;400;500;600&display=swap');

    :root {
      --bg: #111111;
      --bg-alt: #181818;
      --surface: #1e1e1e;
      --border: #2a2a2a;
      --border-gold: rgba(196,160,82,0.25);
      --text: #e8e4dc;
      --text-muted: #888880;
      --gold: #c4a052;
      --gold-light: #e8c87a;
      --gold-pale: rgba(196,160,82,0.08);
      --card-shadow: 0 4px 24px rgba(0,0,0,0.4);
      --font-heading: 'Cormorant Garamond', Georgia, serif;
      --font-body: 'Jost', sans-serif;
      --radius: 2px;
      --radius-lg: 3px;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      font-family: var(--font-body);
      background: var(--bg);
      color: var(--text);
      font-size: 16px;
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
      font-weight: 300;
    }

    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      background: rgba(17,17,17,0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-gold);
      padding: 0 6%;
      display: flex; align-items: center; justify-content: space-between;
      height: 68px;
    }
    .nav-logo {
      font-family: var(--font-heading);
      font-size: 1.4rem; font-weight: 600;
      color: var(--gold); text-decoration: none;
      letter-spacing: 0.03em;
    }
    .nav-links { display: flex; gap: 3rem; list-style: none; }
    .nav-links a {
      text-decoration: none; color: var(--text-muted);
      font-size: 0.8rem; font-weight: 500; letter-spacing: 0.12em;
      text-transform: uppercase;
      transition: color 0.3s;
    }
    .nav-links a:hover { color: var(--gold); }

    #hero {
      min-height: 100vh;
      display: flex; align-items: center;
      padding: 100px 6% 80px;
      background: var(--bg);
      position: relative; overflow: hidden;
    }
    #hero::before {
      content: '';
      position: absolute; top: 0; right: 0;
      width: 50%; height: 100%;
      background: radial-gradient(ellipse at 80% 50%, rgba(196,160,82,0.04) 0%, transparent 70%);
    }
    #hero::after {
      content: '';
      position: absolute; bottom: 0; left: 0; right: 0; height: 1px;
      background: linear-gradient(90deg, transparent, var(--gold), transparent);
    }
    .hero-inner {
      max-width: 1100px; margin: 0 auto; width: 100%;
      display: grid; grid-template-columns: 1fr 300px;
      gap: 80px; align-items: center; position: relative; z-index: 1;
    }
    .hero-tag {
      display: inline-flex; align-items: center; gap: 12px;
      color: var(--gold); font-size: 0.78rem; font-weight: 500;
      letter-spacing: 0.15em; text-transform: uppercase;
      margin-bottom: 2rem;
    }
    .hero-tag::before, .hero-tag::after {
      content: ''; display: inline-block;
      width: 28px; height: 1px; background: var(--gold); opacity: 0.6;
    }
    .hero-name {
      font-family: var(--font-heading);
      font-size: clamp(3rem, 6vw, 5.5rem);
      font-weight: 400; line-height: 1.08;
      color: var(--text); margin-bottom: 1.2rem;
      letter-spacing: -0.01em;
    }
    .hero-bio {
      color: var(--text-muted); font-size: 0.98rem;
      font-weight: 300; max-width: 480px; margin-bottom: 2.5rem;
    }
    .btn-primary {
      display: inline-block;
      background: var(--gold); color: #111111;
      padding: 13px 32px;
      text-decoration: none; font-weight: 600;
      font-size: 0.78rem; letter-spacing: 0.12em; text-transform: uppercase;
      transition: background 0.3s, transform 0.2s;
    }
    .btn-primary:hover { background: var(--gold-light); transform: translateY(-1px); }
    .btn-secondary {
      display: inline-block;
      border: 1px solid var(--border-gold); color: var(--gold);
      padding: 12px 32px;
      text-decoration: none; font-weight: 500;
      font-size: 0.78rem; letter-spacing: 0.12em; text-transform: uppercase;
      margin-left: 16px;
      transition: background 0.3s, border-color 0.3s;
    }
    .btn-secondary:hover { background: var(--gold-pale); border-color: var(--gold); }
    .hero-photo {
      width: 280px; height: 360px; object-fit: cover;
      border: 1px solid var(--border-gold);
      box-shadow: var(--card-shadow);
      filter: grayscale(20%);
    }
    .hero-photo-placeholder {
      width: 280px; height: 360px;
      background: var(--surface);
      border: 1px solid var(--border-gold);
      display: flex; align-items: center; justify-content: center;
      font-family: var(--font-heading); font-size: 6rem; color: var(--gold);
      opacity: 0.7;
    }

    section { padding: 100px 6%; }
    .section-inner { max-width: 1100px; margin: 0 auto; }
    .section-label {
      font-size: 0.7rem; font-weight: 500; letter-spacing: 0.2em;
      text-transform: uppercase; color: var(--gold); opacity: 0.8;
      margin-bottom: 0.8rem;
    }
    .section-title {
      font-family: var(--font-heading);
      font-size: clamp(2rem, 3.5vw, 3rem);
      font-weight: 400; color: var(--text); margin-bottom: 1rem;
      letter-spacing: 0.01em;
    }
    .section-divider {
      width: 48px; height: 1px;
      background: linear-gradient(90deg, var(--gold), transparent);
      margin: 1rem 0 4rem;
    }

    #about { background: var(--bg-alt); }
    .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 100px; align-items: start; }
    .about-text p { color: var(--text-muted); margin-bottom: 1.2rem; font-weight: 300; }

    .about-quote {
      border-left: 1px solid var(--gold); padding-left: 24px;
      margin-top: 2rem; color: var(--text-muted); font-style: italic;
      font-family: var(--font-heading); font-size: 1.15rem;
    }

    #skills { background: var(--bg); }
    .skills-grid { display: flex; flex-wrap: wrap; gap: 10px; }
    .skill-tag {
      background: transparent; border: 1px solid var(--border-gold);
      color: var(--text-muted); padding: 8px 20px;
      font-size: 0.82rem; font-weight: 400; letter-spacing: 0.05em;
      transition: all 0.3s;
    }
    .skill-tag:hover {
      border-color: var(--gold); color: var(--gold);
      background: var(--gold-pale);
    }

    #education { background: var(--bg-alt); }
    .edu-list { display: flex; flex-direction: column; gap: 24px; }
    .edu-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-top: 1px solid var(--border-gold);
      padding: 32px 36px;
    }
    .edu-degree { font-family: var(--font-heading); font-weight: 600; font-size: 1.2rem; margin-bottom: 6px; color: var(--text); }
    .edu-meta { color: var(--gold); font-size: 0.8rem; font-weight: 500; letter-spacing: 0.05em; margin-bottom: 10px; }
    .edu-desc { color: var(--text-muted); font-size: 0.9rem; font-weight: 300; }

    #projects { background: var(--bg); }
    .projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px; }
    .project-card {
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 32px;
      position: relative;
      transition: all 0.3s;
    }
    .project-card::before {
      content: '';
      position: absolute; top: 0; left: 0; right: 0; height: 1px;
      background: var(--gold); opacity: 0;
      transition: opacity 0.3s;
    }
    .project-card:hover { border-color: var(--border-gold); box-shadow: var(--card-shadow); }
    .project-card:hover::before { opacity: 1; }
    .project-name {
      font-family: var(--font-heading); font-weight: 600;
      font-size: 1.3rem; margin-bottom: 10px; color: var(--text);
    }
    .project-desc { color: var(--text-muted); font-size: 0.88rem; font-weight: 300; margin-bottom: 18px; }
    .project-tech { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
    .tech-badge {
      background: var(--gold-pale); border: 1px solid var(--border-gold); color: var(--gold);
      font-size: 0.72rem; font-weight: 500; padding: 3px 10px; letter-spacing: 0.05em;
    }
    .project-link { color: var(--gold); font-size: 0.82rem; font-weight: 500; text-decoration: none; letter-spacing: 0.06em; text-transform: uppercase; }
    .project-link:hover { color: var(--gold-light); }

    #experience { background: var(--bg-alt); }
    .exp-timeline { display: flex; flex-direction: column; gap: 0; }
    .exp-item {
      display: grid; grid-template-columns: 180px 1fr;
      gap: 60px; padding-bottom: 48px;
      border-left: 1px solid var(--border-gold); margin-left: 20px; padding-left: 48px;
      position: relative;
    }
    .exp-item::before {
      content: ''; position: absolute; left: -4px; top: 8px;
      width: 7px; height: 7px;
      background: var(--gold);
    }
    .exp-period { color: var(--text-muted); font-size: 0.8rem; letter-spacing: 0.05em; padding-top: 4px; }
    .exp-role { font-family: var(--font-heading); font-weight: 600; font-size: 1.2rem; margin-bottom: 4px; color: var(--text); }
    .exp-company { color: var(--gold); font-size: 0.85rem; font-weight: 500; letter-spacing: 0.04em; margin-bottom: 12px; }
    .exp-desc { color: var(--text-muted); font-size: 0.88rem; font-weight: 300; line-height: 1.8; }

    #contact { background: var(--bg); }
    .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: start; }
    .contact-item { display: flex; gap: 16px; margin-bottom: 24px; align-items: flex-start; }
    .contact-icon {
      width: 42px; height: 42px;
      border: 1px solid var(--border-gold); color: var(--gold);
      display: flex; align-items: center; justify-content: center;
      font-size: 1rem; flex-shrink: 0;
    }
    .contact-label { font-size: 0.68rem; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-muted); }
    .contact-value { color: var(--text); font-weight: 300; font-size: 0.95rem; }
    .contact-value a { color: var(--gold); text-decoration: none; }
    .contact-value a:hover { color: var(--gold-light); }
    .contact-cta p { color: var(--text-muted); margin-bottom: 2rem; font-size: 1rem; font-weight: 300; }

    footer {
      background: #0d0d0d;
      border-top: 1px solid var(--border-gold);
      text-align: center; padding: 36px;
      color: var(--text-muted); font-size: 0.82rem; font-weight: 300; letter-spacing: 0.06em;
    }
    footer strong { color: var(--gold); font-weight: 500; }

    @media (max-width: 768px) {
      .hero-inner { grid-template-columns: 1fr; }
      .hero-photo, .hero-photo-placeholder { display: none; }
      .about-grid, .contact-grid { grid-template-columns: 1fr; gap: 40px; }
      .exp-item { grid-template-columns: 1fr; gap: 4px; }
      .nav-links { display: none; }
    }
    """
