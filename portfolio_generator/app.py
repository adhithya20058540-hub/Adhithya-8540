"""
main.py - Portfolio Generator CLI
Entry point for the interactive terminal application.

Run with:  python main.py
"""

import json
import os
import sys
import platform
from copy import deepcopy

from themes import THEMES
from generator import generate_portfolio

# ─────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "portfolio.html")

# ─────────────────────────────────────────────
#  COLORS (ANSI escape codes)
# ─────────────────────────────────────────────

class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE    = "\033[94m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"

    @staticmethod
    def disable():
        """Disable colors (e.g., on Windows without ANSI support)."""
        for attr in ["RESET","BOLD","DIM","CYAN","GREEN","YELLOW",
                     "RED","MAGENTA","BLUE","WHITE","GRAY"]:
            setattr(C, attr, "")


# Disable colors on Windows if terminal doesn't support them
if platform.system() == "Windows":
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        C.disable()


# ─────────────────────────────────────────────
#  PRINT HELPERS
# ─────────────────────────────────────────────

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")


def banner():
    print(f"""
{C.CYAN}{C.BOLD}
  ╔═══════════════════════════════════════════╗
  ║        PORTFOLIO GENERATOR  v1.0          ║
  ║   Build your personal website from CLI    ║
  ╚═══════════════════════════════════════════╝
{C.RESET}""")


def hr(char="─", width=48, color=C.GRAY):
    print(f"{color}{char * width}{C.RESET}")


def success(msg: str):
    print(f"\n{C.GREEN}  ✓  {msg}{C.RESET}")


def warn(msg: str):
    print(f"\n{C.YELLOW}  ⚠  {msg}{C.RESET}")


def error(msg: str):
    print(f"\n{C.RED}  ✗  {msg}{C.RESET}")


def info(msg: str):
    print(f"{C.GRAY}  {msg}{C.RESET}")


def prompt(label: str, default: str = "") -> str:
    """Show a styled input prompt and return the user's input."""
    hint = f" {C.GRAY}[{default}]{C.RESET}" if default else ""
    try:
        value = input(f"  {C.CYAN}›{C.RESET} {label}{hint}: ").strip()
    except (KeyboardInterrupt, EOFError):
        print()
        return default
    return value if value else default


def pause(msg: str = "Press Enter to continue…"):
    try:
        input(f"\n  {C.GRAY}{msg}{C.RESET}")
    except (KeyboardInterrupt, EOFError):
        print()


# ─────────────────────────────────────────────
#  DATA MANAGEMENT
# ─────────────────────────────────────────────

def load_data() -> dict:
    """Load portfolio data from the JSON file, or return empty scaffold."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            warn(f"'{DATA_FILE}' is corrupted. Starting with empty data.")
    return _empty_data()


def save_data(data: dict):
    """Persist portfolio data to JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        success(f"Data saved to  {DATA_FILE}")
    except IOError as e:
        error(f"Could not save file: {e}")


def _empty_data() -> dict:
    return {
        "personal": {
            "full_name": "",
            "title": "",
            "bio": "",
            "email": "",
            "phone": "",
            "linkedin": "",
            "github": "",
            "profile_image": "",
        },
        "skills": [],
        "education": [],
        "projects": [],
        "experience": [],
        "theme": "light_minimal",
    }


# ─────────────────────────────────────────────
#  INPUT HELPERS
# ─────────────────────────────────────────────

def ask_list(label: str, existing: list) -> list:
    """
    Ask the user to enter a comma-separated list.
    Shows existing values as default.
    """
    default_str = ", ".join(existing) if existing else ""
    raw = prompt(f"{label} (comma-separated)", default_str)
    return [item.strip() for item in raw.split(",") if item.strip()]


def ask_yes_no(question: str, default: bool = True) -> bool:
    """Ask a yes/no question and return True/False."""
    hint = "Y/n" if default else "y/N"
    answer = prompt(f"{question} [{hint}]")
    if not answer:
        return default
    return answer.lower() in ("y", "yes")


def validate_email(email: str) -> bool:
    """Basic email format check."""
    return "@" in email and "." in email.split("@")[-1]


def validate_url(url: str) -> bool:
    """Accept empty strings or strings that start with http/https."""
    return url == "" or url.startswith("http://") or url.startswith("https://")


# ─────────────────────────────────────────────
#  SECTION EDITORS
# ─────────────────────────────────────────────

def edit_personal(data: dict):
    """Interactively edit the personal info section."""
    clear()
    banner()
    print(f"{C.BOLD}  ── Personal Information ──{C.RESET}\n")
    p = data["personal"]

    p["full_name"] = prompt("Full Name", p.get("full_name", ""))
    if not p["full_name"]:
        warn("Full name is required.")
        p["full_name"] = prompt("Full Name (required)")

    p["title"] = prompt("Professional Title", p.get("title", ""))
    print(f"\n  {C.GRAY}Bio (a short paragraph about yourself):{C.RESET}")
    p["bio"] = prompt("Bio", p.get("bio", ""))

    print()
    p["email"] = prompt("Contact Email", p.get("email", ""))
    if p["email"] and not validate_email(p["email"]):
        warn("That doesn't look like a valid email address.")

    p["phone"] = prompt("Phone Number", p.get("phone", ""))

    print(f"\n  {C.GRAY}Social / Professional Links:{C.RESET}")
    p["linkedin"] = prompt("LinkedIn URL", p.get("linkedin", ""))
    if p["linkedin"] and not validate_url(p["linkedin"]):
        warn("LinkedIn URL should start with https://")

    p["github"] = prompt("GitHub URL", p.get("github", ""))
    if p["github"] and not validate_url(p["github"]):
        warn("GitHub URL should start with https://")

    p["profile_image"] = prompt("Profile Image URL (optional)", p.get("profile_image", ""))
    if p["profile_image"] and not validate_url(p["profile_image"]):
        warn("Profile image URL should start with https://")

    data["personal"] = p
    save_data(data)


def edit_skills(data: dict):
    """Edit the skills list."""
    clear()
    banner()
    print(f"{C.BOLD}  ── Skills & Technologies ──{C.RESET}\n")
    info("Enter your skills as a comma-separated list.")
    info("Example: Python, JavaScript, React, Docker, AWS\n")
    data["skills"] = ask_list("Skills", data.get("skills", []))
    save_data(data)


def edit_education(data: dict):
    """Edit education entries with add/remove options."""
    while True:
        clear()
        banner()
        print(f"{C.BOLD}  ── Education ──{C.RESET}\n")
        edu_list = data.get("education", [])

        if edu_list:
            for i, edu in enumerate(edu_list):
                print(f"  {C.CYAN}[{i+1}]{C.RESET} {edu.get('degree', '?')} — {edu.get('institution', '?')} ({edu.get('year', '?')})")
        else:
            info("No education entries yet.")

        print(f"\n  {C.GRAY}[a]{C.RESET} Add entry   {C.GRAY}[d]{C.RESET} Delete entry   {C.GRAY}[b]{C.RESET} Back")
        choice = prompt("Action", "b").lower()

        if choice == "a":
            print()
            degree = prompt("Degree / Qualification")
            institution = prompt("Institution / School")
            year = prompt("Year of Completion")
            description = prompt("Short Description")
            edu_list.append({
                "degree": degree,
                "institution": institution,
                "year": year,
                "description": description,
            })
            data["education"] = edu_list
            save_data(data)

        elif choice == "d" and edu_list:
            idx = prompt("Entry number to delete")
            try:
                idx = int(idx) - 1
                if 0 <= idx < len(edu_list):
                    removed = edu_list.pop(idx)
                    data["education"] = edu_list
                    save_data(data)
                    success(f"Removed: {removed.get('degree', '')}")
                else:
                    error("Invalid entry number.")
            except ValueError:
                error("Please enter a valid number.")
            pause()

        elif choice == "b":
            break


def edit_projects(data: dict):
    """Edit project entries."""
    while True:
        clear()
        banner()
        print(f"{C.BOLD}  ── Projects ──{C.RESET}\n")
        proj_list = data.get("projects", [])

        if proj_list:
            for i, proj in enumerate(proj_list):
                print(f"  {C.CYAN}[{i+1}]{C.RESET} {proj.get('name', '?')}")
                info(f"       {proj.get('description', '')[:70]}…")
        else:
            info("No projects added yet.")

        print(f"\n  {C.GRAY}[a]{C.RESET} Add project   {C.GRAY}[d]{C.RESET} Delete project   {C.GRAY}[b]{C.RESET} Back")
        choice = prompt("Action", "b").lower()

        if choice == "a":
            print()
            name = prompt("Project Name")
            description = prompt("Description")
            tech_raw = prompt("Tech Stack (comma-separated)")
            tech = [t.strip() for t in tech_raw.split(",") if t.strip()]
            link = prompt("GitHub / Live URL (optional)")
            proj_list.append({
                "name": name,
                "description": description,
                "tech": tech,
                "link": link,
            })
            data["projects"] = proj_list
            save_data(data)

        elif choice == "d" and proj_list:
            idx = prompt("Project number to delete")
            try:
                idx = int(idx) - 1
                if 0 <= idx < len(proj_list):
                    removed = proj_list.pop(idx)
                    data["projects"] = proj_list
                    save_data(data)
                    success(f"Removed: {removed.get('name', '')}")
                else:
                    error("Invalid project number.")
            except ValueError:
                error("Please enter a valid number.")
            pause()

        elif choice == "b":
            break


def edit_experience(data: dict):
    """Edit work experience entries."""
    while True:
        clear()
        banner()
        print(f"{C.BOLD}  ── Work Experience ──{C.RESET}\n")
        exp_list = data.get("experience", [])

        if exp_list:
            for i, exp in enumerate(exp_list):
                print(f"  {C.CYAN}[{i+1}]{C.RESET} {exp.get('role', '?')} @ {exp.get('company', '?')} ({exp.get('period', '?')})")
        else:
            info("No experience entries added yet.")

        print(f"\n  {C.GRAY}[a]{C.RESET} Add entry   {C.GRAY}[d]{C.RESET} Delete entry   {C.GRAY}[b]{C.RESET} Back")
        choice = prompt("Action", "b").lower()

        if choice == "a":
            print()
            role = prompt("Job Title / Role")
            company = prompt("Company Name")
            period = prompt("Period (e.g. 2021 – 2023)")
            description = prompt("Description of responsibilities")
            exp_list.append({
                "role": role,
                "company": company,
                "period": period,
                "description": description,
            })
            data["experience"] = exp_list
            save_data(data)

        elif choice == "d" and exp_list:
            idx = prompt("Entry number to delete")
            try:
                idx = int(idx) - 1
                if 0 <= idx < len(exp_list):
                    removed = exp_list.pop(idx)
                    data["experience"] = exp_list
                    save_data(data)
                    success(f"Removed: {removed.get('role', '')}")
                else:
                    error("Invalid entry number.")
            except ValueError:
                error("Please enter a valid number.")
            pause()

        elif choice == "b":
            break


# ─────────────────────────────────────────────
#  THEME SELECTOR
# ─────────────────────────────────────────────

def choose_theme(data: dict):
    """Display theme options and let the user pick one."""
    clear()
    banner()
    print(f"{C.BOLD}  ── Choose Your Theme ──{C.RESET}\n")
    print(f"  {'#':<4} {'Theme':<22} {'Type':<8} Description")
    hr()

    theme_keys = list(THEMES.keys())
    for i, key in enumerate(theme_keys):
        t = THEMES[key]
        current_marker = f" {C.GREEN}← current{C.RESET}" if key == data.get("theme") else ""
        type_color = C.YELLOW if t["type"] == "light" else C.MAGENTA
        print(f"  {C.CYAN}{i+1:<4}{C.RESET} {t['icon']} {t['label']:<20} "
              f"{type_color}{t['type']:<8}{C.RESET} {C.GRAY}{t['description']}{C.RESET}"
              f"{current_marker}")

    hr()
    print()
    while True:
        choice = prompt("Enter theme number (1–4)")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(theme_keys):
                selected_key = theme_keys[idx]
                data["theme"] = selected_key
                save_data(data)
                t = THEMES[selected_key]
                success(f"Theme set to: {t['icon']}  {t['label']}")
                pause()
                return
            else:
                error("Please enter a number between 1 and 4.")
        except ValueError:
            error("Please enter a valid number.")


# ─────────────────────────────────────────────
#  PREVIEW DATA
# ─────────────────────────────────────────────

def preview_data(data: dict):
    """Print a formatted summary of the current portfolio data."""
    clear()
    banner()
    print(f"{C.BOLD}  ── Current Portfolio Data ──{C.RESET}\n")

    p = data.get("personal", {})
    theme_id = data.get("theme", "light_minimal")
    theme_label = THEMES.get(theme_id, {}).get("label", theme_id)

    print(f"  {C.YELLOW}PERSONAL{C.RESET}")
    print(f"  Name    : {C.WHITE}{p.get('full_name', '—')}{C.RESET}")
    print(f"  Title   : {p.get('title', '—')}")
    print(f"  Email   : {p.get('email', '—')}")
    print(f"  Phone   : {p.get('phone', '—')}")
    print(f"  LinkedIn: {p.get('linkedin', '—')}")
    print(f"  GitHub  : {p.get('github', '—')}")
    print(f"  Image   : {p.get('profile_image', 'None')}")

    hr()
    skills = data.get("skills", [])
    print(f"\n  {C.YELLOW}SKILLS{C.RESET}  ({len(skills)} total)")
    if skills:
        print("  " + ", ".join(skills))

    hr()
    edu_list = data.get("education", [])
    print(f"\n  {C.YELLOW}EDUCATION{C.RESET}  ({len(edu_list)} entries)")
    for edu in edu_list:
        print(f"  · {edu.get('degree', '?')} — {edu.get('institution', '?')} ({edu.get('year', '?')})")

    hr()
    proj_list = data.get("projects", [])
    print(f"\n  {C.YELLOW}PROJECTS{C.RESET}  ({len(proj_list)} entries)")
    for proj in proj_list:
        print(f"  · {proj.get('name', '?')}")

    hr()
    exp_list = data.get("experience", [])
    print(f"\n  {C.YELLOW}EXPERIENCE{C.RESET}  ({len(exp_list)} entries)")
    for exp in exp_list:
        print(f"  · {exp.get('role', '?')} @ {exp.get('company', '?')} ({exp.get('period', '?')})")

    hr()
    print(f"\n  {C.YELLOW}THEME{C.RESET}  {THEMES.get(theme_id, {}).get('icon', '')} {theme_label}")

    pause()


# ─────────────────────────────────────────────
#  GENERATE WEBSITE
# ─────────────────────────────────────────────

def run_generate(data: dict):
    """Prompt for theme if not set, then generate the HTML portfolio."""
    clear()
    banner()
    print(f"{C.BOLD}  ── Generate Portfolio Website ──{C.RESET}\n")

    # Check that we have at least a name
    if not data.get("personal", {}).get("full_name"):
        warn("You haven't entered your name yet. Please fill in personal info first.")
        pause()
        return

    current_theme = data.get("theme", "")
    theme_info = THEMES.get(current_theme, {})

    if current_theme:
        print(f"  Current theme: {theme_info.get('icon', '')} {C.BOLD}{theme_info.get('label', current_theme)}{C.RESET}")
        change = ask_yes_no("  Keep this theme?", default=True)
        if not change:
            choose_theme(data)
            clear()
            banner()
            print(f"{C.BOLD}  ── Generating Portfolio ──{C.RESET}\n")
    else:
        info("No theme selected yet. Please choose one now.\n")
        pause("Press Enter to open the theme selector…")
        choose_theme(data)
        clear()
        banner()
        print(f"{C.BOLD}  ── Generating Portfolio ──{C.RESET}\n")

    t = THEMES.get(data["theme"], {})
    print(f"\n  Building with theme: {t.get('icon', '')} {C.BOLD}{t.get('label', '')}{C.RESET}")
    print(f"  Output file       : {C.CYAN}{OUTPUT_FILE}{C.RESET}\n")

    try:
        path = generate_portfolio(data, output_path=OUTPUT_FILE)
        print(f"\n  {C.GREEN}{C.BOLD}✓  Portfolio generated successfully!{C.RESET}")
        hr("─", 48, C.GREEN)
        print(f"\n  Open this file in your browser:")
        print(f"  {C.CYAN}{C.BOLD}{path}{C.RESET}\n")

        # Try to auto-open in browser
        if ask_yes_no("  Open in browser now?", default=True):
            import webbrowser
            webbrowser.open(f"file://{path}")

    except Exception as e:
        error(f"Generation failed: {e}")

    pause()


# ─────────────────────────────────────────────
#  EDIT SUBMENU
# ─────────────────────────────────────────────

def edit_menu(data: dict):
    """Submenu for editing different sections of the portfolio."""
    while True:
        clear()
        banner()
        print(f"{C.BOLD}  ── Edit Portfolio Data ──{C.RESET}\n")

        p = data.get("personal", {})
        name = p.get("full_name", "Not set")
        skill_count = len(data.get("skills", []))
        edu_count = len(data.get("education", []))
        proj_count = len(data.get("projects", []))
        exp_count = len(data.get("experience", []))

        options = [
            ("1", "Personal Info",  f"Name: {name}"),
            ("2", "Skills",         f"{skill_count} skill(s)"),
            ("3", "Education",      f"{edu_count} entr{'y' if edu_count==1 else 'ies'}"),
            ("4", "Projects",       f"{proj_count} project(s)"),
            ("5", "Work Experience",f"{exp_count} entr{'y' if exp_count==1 else 'ies'}"),
            ("b", "← Back",         ""),
        ]

        for key, label, detail in options:
            detail_str = f"  {C.GRAY}{detail}{C.RESET}" if detail else ""
            print(f"  {C.CYAN}[{key}]{C.RESET}  {label}{detail_str}")

        print()
        choice = prompt("Choose section to edit").lower()

        if choice == "1":
            edit_personal(data)
        elif choice == "2":
            edit_skills(data)
        elif choice == "3":
            edit_education(data)
        elif choice == "4":
            edit_projects(data)
        elif choice == "5":
            edit_experience(data)
        elif choice == "b":
            break
        else:
            warn("Invalid option. Please try again.")
            pause()


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────

def main_menu(data: dict):
    """Display the main menu and route user choices."""
    while True:
        clear()
        banner()

        p = data.get("personal", {})
        name = p.get("full_name")
        theme_id = data.get("theme", "light_minimal")
        theme_info = THEMES.get(theme_id, {})

        if name:
            print(f"  Portfolio for: {C.BOLD}{C.WHITE}{name}{C.RESET}")
            print(f"  Theme        : {theme_info.get('icon', '')} {theme_info.get('label', theme_id)}")
            hr()
        else:
            print(f"  {C.YELLOW}No portfolio data found. Start by creating a new one!{C.RESET}")
            hr()

        print(f"""
  {C.CYAN}[1]{C.RESET}  Create / Edit Portfolio Data
  {C.CYAN}[2]{C.RESET}  Choose / Change Theme
  {C.CYAN}[3]{C.RESET}  Preview Saved Data
  {C.CYAN}[4]{C.RESET}  Generate Portfolio Website  ← {C.GREEN}builds HTML{C.RESET}
  {C.CYAN}[q]{C.RESET}  Exit
""")

        choice = prompt("Choose an option").lower()

        if choice == "1":
            edit_menu(data)
        elif choice == "2":
            choose_theme(data)
        elif choice == "3":
            preview_data(data)
        elif choice == "4":
            run_generate(data)
        elif choice in ("q", "quit", "exit"):
            clear()
            print(f"\n  {C.CYAN}Thanks for using Portfolio Generator!{C.RESET}")
            print(f"  {C.GRAY}Your data is saved in data.json{C.RESET}\n")
            sys.exit(0)
        else:
            warn("Invalid option. Please enter 1, 2, 3, 4, or q.")
            pause()


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

def main():
    """Main entry point — load data and launch the menu."""
    try:
        data = load_data()
        main_menu(data)
    except KeyboardInterrupt:
        print(f"\n\n  {C.GRAY}Goodbye!{C.RESET}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
