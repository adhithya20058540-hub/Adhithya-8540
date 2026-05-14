# 🖥️ Portfolio Generator CLI

Build a beautiful personal portfolio website interactively through your terminal — no web frameworks or frontend knowledge required.

---

## 📁 Project Structure

```
portfolio_generator/
├── main.py          # CLI application — run this
├── themes.py        # CSS definitions for all 4 themes
├── generator.py     # HTML generation engine
├── data.json        # Your portfolio data (auto-saved)
├── portfolio.html   # Generated website (created on demand)
└── README.md        # This file
```

---

## 🚀 Quick Start

**Requirements:** Python 3.7+  (no third-party packages needed)

```bash
# 1. Navigate to the project folder
cd portfolio_generator

# 2. Run the application
python main.py
```

That's it! The CLI will guide you through everything.

---

## 🎨 Available Themes

| # | Theme | Style | Description |
|---|-------|-------|-------------|
| 1 | ☀️ Light Minimal | Light | Clean white modern style, DM Serif typography |
| 2 | 🏢 Light Professional | Light | Blue-gray corporate style, bold gradient hero |
| 3 | ⚡ Dark Neon | Dark | Black + glowing cyan/pink neon, grid background |
| 4 | ✨ Dark Elegant | Dark | Dark gray + gold premium styling, Cormorant Garamond |

---

## 📋 Main Menu Options

```
[1]  Create / Edit Portfolio Data   → Enter name, bio, skills, projects, etc.
[2]  Choose / Change Theme          → Pick from 4 themes (required before generating)
[3]  Preview Saved Data             → See all your saved info in the terminal
[4]  Generate Portfolio Website     → Builds portfolio.html (opens in browser)
[q]  Exit
```

---

## 🗂️ Portfolio Sections Generated

The HTML file includes these fully styled sections:

- **Hero Banner** — Name, title, bio, buttons, profile photo
- **About Me** — Extended bio + contact/stats sidebar
- **Skills** — Tag cloud of your technologies
- **Education** — Degree cards with institution & year
- **Projects** — Cards with tech stack badges and links
- **Experience** — Timeline with role, company, period
- **Contact** — Email, phone, LinkedIn, GitHub
- **Footer** — Credit and theme name

---

## 💾 Data Storage

All your information is saved in `data.json`. This file is automatically updated after each edit. You can manually edit it too — just keep it valid JSON.

### data.json structure:

```json
{
  "personal": {
    "full_name": "Your Name",
    "title": "Your Title",
    "bio": "A short bio...",
    "email": "you@example.com",
    "phone": "+1 555 123 4567",
    "linkedin": "https://linkedin.com/in/you",
    "github": "https://github.com/you",
    "profile_image": "https://..."
  },
  "skills": ["Python", "JavaScript", "..."],
  "education": [
    {
      "degree": "B.Sc. Computer Science",
      "institution": "University Name",
      "year": "2022",
      "description": "Description..."
    }
  ],
  "projects": [
    {
      "name": "Project Name",
      "description": "What it does...",
      "tech": ["React", "Node.js"],
      "link": "https://github.com/..."
    }
  ],
  "experience": [
    {
      "role": "Senior Developer",
      "company": "Company Name",
      "period": "2022 – Present",
      "description": "What you did..."
    }
  ],
  "theme": "light_minimal"
}
```

---

## 🔄 Changing Themes

You can switch themes at any time from the main menu. Regenerating the site after a theme change will overwrite `portfolio.html` with the new design — your data stays intact.

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| Colors not showing on Windows | Run in Windows Terminal or VS Code terminal |
| Portfolio not opening in browser | Open `portfolio.html` manually in your browser |
| `data.json` corrupted | Delete the file and restart — you'll get a fresh template |
| Font not loading | You need an internet connection for Google Fonts |

---

## ✨ Tips

- The **profile image URL** can be any public image URL. Try `https://i.pravatar.cc/300` for a placeholder.
- Skills are entered as a **comma-separated list**: `Python, React, Docker, AWS`
- For the **Dark Neon** theme, URLs load the `Space Mono` + `Rajdhani` fonts — it looks best in a full browser window.
- The generated HTML is fully **self-contained** and can be hosted on GitHub Pages, Netlify, or any static host.

---

## 📦 Hosting Your Portfolio

Once generated, `portfolio.html` is a single-file website. To host it:

1. **GitHub Pages** — Push to a repo, enable Pages in settings
2. **Netlify Drop** — Drag and drop the file at netlify.com/drop
3. **Vercel** — Import the repo via vercel.com
