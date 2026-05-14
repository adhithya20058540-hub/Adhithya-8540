"""
generator.py - HTML portfolio website generator
Builds a single responsive HTML file using portfolio data and the chosen theme.
"""

import os
from themes import get_theme_css, THEMES


def generate_portfolio(data: dict, output_path: str = "portfolio.html") -> str:
    """
    Generate a complete HTML portfolio file from the data dict.
    Returns the path of the saved file.
    """
    theme_id = data.get("theme", "light_minimal")
    if theme_id not in THEMES:
        theme_id = "light_minimal"

    theme_info = THEMES[theme_id]
    css = get_theme_css(theme_id)
    personal = data.get("personal", {})
    skills = data.get("skills", [])
    education = data.get("education", [])
    projects = data.get("projects", [])
    experience = data.get("experience", [])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{_esc(personal.get('full_name', 'Portfolio'))} — {_esc(personal.get('title', ''))}</title>
  <meta name="description" content="{_esc(personal.get('bio', '')[:150])}">
  <style>
{css}
  </style>
</head>
<body>

<!-- ── NAVIGATION ───────────────────────────────── -->
<nav>
  <a href="#hero" class="nav-logo">{_initials(personal.get('full_name', 'P'))}</a>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#skills">Skills</a></li>
    <li><a href="#education">Education</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>

<!-- ── HERO ─────────────────────────────────────── -->
<section id="hero">
  <div class="hero-inner">
    <div class="hero-content">
      <span class="hero-tag">{_esc(personal.get('title', 'Developer'))}</span>
      <h1 class="hero-name">{_render_name(personal.get('full_name', 'Your Name'), theme_id)}</h1>
      <p class="hero-bio">{_esc(personal.get('bio', ''))}</p>
      <div class="hero-actions">
        <a href="#projects" class="btn-primary">View My Work</a>
        <a href="#contact" class="btn-secondary">Get In Touch</a>
      </div>
    </div>
    {_render_photo(personal, theme_id)}
  </div>
</section>

<!-- ── ABOUT ─────────────────────────────────────── -->
<section id="about">
  <div class="section-inner">
    <div class="about-grid">
      <div>
        <p class="section-label">Who I Am</p>
        <h2 class="section-title">About Me</h2>
        <div class="section-divider"></div>
        <div class="about-text">
          <p>{_esc(personal.get('bio', 'No bio provided.'))}</p>
          <p>I'm always looking to collaborate on interesting projects and solve meaningful problems. Feel free to explore my work and reach out!</p>
          {_dark_elegant_quote(theme_id)}
        </div>
      </div>
      <div>
        {_about_side_content(personal, skills, theme_id)}
      </div>
    </div>
  </div>
</section>

<!-- ── SKILLS ─────────────────────────────────────── -->
<section id="skills">
  <div class="section-inner">
    <p class="section-label">What I Know</p>
    <h2 class="section-title">Skills & Technologies</h2>
    <div class="section-divider"></div>
    <div class="skills-grid">
      {"".join(f'<span class="skill-tag">{_esc(s)}</span>' for s in skills)}
    </div>
  </div>
</section>

<!-- ── EDUCATION ─────────────────────────────────── -->
<section id="education">
  <div class="section-inner">
    <p class="section-label">My Background</p>
    <h2 class="section-title">Education</h2>
    <div class="section-divider"></div>
    <div class="edu-list">
      {_render_education(education, theme_id)}
    </div>
  </div>
</section>

<!-- ── PROJECTS ──────────────────────────────────── -->
<section id="projects">
  <div class="section-inner">
    <p class="section-label">What I've Built</p>
    <h2 class="section-title">Featured Projects</h2>
    <div class="section-divider"></div>
    <div class="projects-grid">
      {_render_projects(projects)}
    </div>
  </div>
</section>

<!-- ── EXPERIENCE ────────────────────────────────── -->
<section id="experience">
  <div class="section-inner">
    <p class="section-label">Where I've Worked</p>
    <h2 class="section-title">Experience</h2>
    <div class="section-divider"></div>
    <div class="exp-timeline">
      {_render_experience(experience)}
    </div>
  </div>
</section>

<!-- ── CONTACT ───────────────────────────────────── -->
<section id="contact">
  <div class="section-inner">
    <p class="section-label">Let's Connect</p>
    <h2 class="section-title">Get In Touch</h2>
    <div class="section-divider"></div>
    <div class="contact-grid">
      <div class="contact-info">
        {_render_contact(personal)}
      </div>
      <div class="contact-cta">
        <p>I'm currently open to new opportunities, freelance projects, and interesting collaborations. Let's build something great together.</p>
        {"" if not personal.get("email") else f'<a href="mailto:{_esc(personal["email"])}" class="btn-primary">Send Me an Email</a>'}
      </div>
    </div>
  </div>
</section>

<!-- ── FOOTER ────────────────────────────────────── -->
<footer>
  <p>Designed &amp; Built by <strong>{_esc(personal.get('full_name', 'You'))}</strong> &nbsp;·&nbsp; Theme: {theme_info['label']}</p>
  <p style="margin-top: 6px; font-size: 0.78em; opacity: 0.6;">Generated with Portfolio Generator CLI</p>
</footer>

</body>
</html>
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return os.path.abspath(output_path)


# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def _esc(text: str) -> str:
    """HTML-escape a string to prevent XSS."""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


def _initials(name: str) -> str:
    """Return up to 2 initials from a name."""
    parts = name.strip().split()
    if len(parts) >= 2:
        return f"{parts[0][0]}{parts[-1][0]}".upper()
    return name[:2].upper() if name else "PF"


def _render_name(name: str, theme_id: str) -> str:
    """Render hero name; for dark_neon, wrap first name in span for color."""
    if theme_id == "dark_neon":
        parts = name.split(" ", 1)
        if len(parts) == 2:
            return f'<span>{_esc(parts[0])}</span> {_esc(parts[1])}'
    return _esc(name)


def _render_photo(personal: dict, theme_id: str) -> str:
    """Render the profile photo or a placeholder."""
    img_url = personal.get("profile_image", "").strip()
    initial = personal.get("full_name", "?")[0].upper()
    if img_url:
        return f'<img src="{_esc(img_url)}" alt="Profile photo" class="hero-photo" />'
    return f'<div class="hero-photo-placeholder">{initial}</div>'


def _dark_elegant_quote(theme_id: str) -> str:
    """Only dark_elegant theme shows a stylized quote block."""
    if theme_id == "dark_elegant":
        return '<p class="about-quote">"Craftsmanship is not about perfection — it\'s about intention."</p>'
    return ""


def _about_side_content(personal: dict, skills: list, theme_id: str) -> str:
    """Right side of About section — changes per theme."""
    if theme_id == "light_professional":
        # Stats grid
        return """
        <div style="padding-top: 60px;">
          <div class="stats-row">
            <div class="stat-box"><div class="stat-number">5+</div><div class="stat-label">Years Experience</div></div>
            <div class="stat-box"><div class="stat-number">20+</div><div class="stat-label">Projects Done</div></div>
            <div class="stat-box"><div class="stat-number">10+</div><div class="stat-label">Happy Clients</div></div>
            <div class="stat-box"><div class="stat-number">3</div><div class="stat-label">Awards Won</div></div>
          </div>
        </div>"""
    else:
        # Contact quick-info
        items = []
        email = personal.get("email")
        github = personal.get("github")
        linkedin = personal.get("linkedin")
        if email:
            items.append(f'<p style="margin-bottom: 8px;">📧 <a href="mailto:{_esc(email)}" style="color: inherit;">{_esc(email)}</a></p>')
        if github:
            items.append(f'<p style="margin-bottom: 8px;">💻 <a href="{_esc(github)}" style="color: inherit;" target="_blank">{_esc(github)}</a></p>')
        if linkedin:
            items.append(f'<p style="margin-bottom: 8px;">🔗 <a href="{_esc(linkedin)}" style="color: inherit;" target="_blank">LinkedIn Profile</a></p>')
        content = "\n".join(items)
        return f"""
        <div style="padding-top: 60px; opacity: 0.75; font-size: 0.9rem;">
          {content}
        </div>"""


def _render_education(education: list, theme_id: str) -> str:
    parts = []
    for edu in education:
        degree = _esc(edu.get("degree", "Degree"))
        institution = _esc(edu.get("institution", "Institution"))
        year = _esc(edu.get("year", ""))
        desc = _esc(edu.get("description", ""))

        if theme_id == "light_professional":
            parts.append(f"""
            <div class="edu-card">
              <div><span class="edu-year-badge">{year}</span></div>
              <div>
                <p class="edu-degree">{degree}</p>
                <p class="edu-meta">{institution}</p>
                <p class="edu-desc">{desc}</p>
              </div>
            </div>""")
        else:
            parts.append(f"""
            <div class="edu-card">
              <p class="edu-degree">{degree}</p>
              <p class="edu-meta">{institution} &nbsp;·&nbsp; {year}</p>
              <p class="edu-desc">{desc}</p>
            </div>""")

    return "\n".join(parts) if parts else "<p>No education data added yet.</p>"


def _render_projects(projects: list) -> str:
    parts = []
    for proj in projects:
        name = _esc(proj.get("name", "Project"))
        desc = _esc(proj.get("description", ""))
        tech_list = proj.get("tech", [])
        link = proj.get("link", "#")

        tech_badges = "".join(
            f'<span class="tech-badge">{_esc(t)}</span>' for t in tech_list
        )

        parts.append(f"""
        <div class="project-card">
          <h3 class="project-name">{name}</h3>
          <p class="project-desc">{desc}</p>
          <div class="project-tech">{tech_badges}</div>
          <a href="{_esc(link)}" target="_blank" class="project-link">View Project</a>
        </div>""")

    return "\n".join(parts) if parts else "<p>No projects added yet.</p>"


def _render_experience(experience: list) -> str:
    parts = []
    for exp in experience:
        role = _esc(exp.get("role", "Role"))
        company = _esc(exp.get("company", "Company"))
        period = _esc(exp.get("period", ""))
        desc = _esc(exp.get("description", ""))

        parts.append(f"""
        <div class="exp-item">
          <div class="exp-period">{period}</div>
          <div>
            <p class="exp-role">{role}</p>
            <p class="exp-company">{company}</p>
            <p class="exp-desc">{desc}</p>
          </div>
        </div>""")

    return "\n".join(parts) if parts else "<p>No experience added yet.</p>"


def _render_contact(personal: dict) -> str:
    items = []

    if email := personal.get("email"):
        items.append(f"""
        <div class="contact-item">
          <div class="contact-icon">📧</div>
          <div>
            <p class="contact-label">Email</p>
            <p class="contact-value"><a href="mailto:{_esc(email)}">{_esc(email)}</a></p>
          </div>
        </div>""")

    if phone := personal.get("phone"):
        items.append(f"""
        <div class="contact-item">
          <div class="contact-icon">📱</div>
          <div>
            <p class="contact-label">Phone</p>
            <p class="contact-value">{_esc(phone)}</p>
          </div>
        </div>""")

    if linkedin := personal.get("linkedin"):
        items.append(f"""
        <div class="contact-item">
          <div class="contact-icon">🔗</div>
          <div>
            <p class="contact-label">LinkedIn</p>
            <p class="contact-value"><a href="{_esc(linkedin)}" target="_blank">LinkedIn Profile</a></p>
          </div>
        </div>""")

    if github := personal.get("github"):
        items.append(f"""
        <div class="contact-item">
          <div class="contact-icon">💻</div>
          <div>
            <p class="contact-label">GitHub</p>
            <p class="contact-value"><a href="{_esc(github)}" target="_blank">GitHub Profile</a></p>
          </div>
        </div>""")

    return "\n".join(items) if items else "<p>No contact information provided.</p>"
