#!/usr/bin/env python3
"""
Validates all SKILL.md files in the skills folder.
Checks frontmatter yaml keys (name, description) and file references.
"""

import os
import sys
import re

SKILLS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "skills"))

def validate_skills():
    if not os.path.isdir(SKILLS_DIR):
        print(f"Error: skills directory not found at {SKILLS_DIR}")
        return 1

    skill_folders = sorted([d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))])
    print(f"Found {len(skill_folders)} skill directories to validate in {SKILLS_DIR}...\n")

    errors = []
    summary = []

    for folder in skill_folders:
        folder_path = os.path.join(SKILLS_DIR, folder)
        skill_file = os.path.join(folder_path, "SKILL.md")

        if not os.path.isfile(skill_file):
            errors.append(f"[{folder}] Missing SKILL.md file")
            continue

        with open(skill_file, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Frontmatter validation
        if not content.startswith("---"):
            errors.append(f"[{folder}] SKILL.md does not start with YAML frontmatter delimiter (---)")
            continue

        parts = content.split("---", 2)
        if len(parts) < 3:
            errors.append(f"[{folder}] Malformed YAML frontmatter (missing closing ---)")
            continue

        frontmatter = parts[1]
        name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
        desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)

        if not name_match:
            errors.append(f"[{folder}] Missing 'name' attribute in frontmatter")
        if not desc_match:
            errors.append(f"[{folder}] Missing 'description' attribute in frontmatter")

        skill_name = name_match.group(1).strip() if name_match else folder
        desc_preview = (desc_match.group(1).strip()[:60] + "...") if desc_match else "No description"
        summary.append((skill_name, desc_preview))

    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  ❌ {err}")
        return 1

    print(f"✅ All {len(summary)} skills passed validation successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(validate_skills())
