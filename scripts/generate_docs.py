#!/usr/bin/env python3
"""
Generate documentation for all skills.
"""
import argparse
from pathlib import Path


import sys

def generate_docs(skill_name: str | None = None) -> bool:
    """Generate documentation for a specific skill or all skills."""
    skills_dir = Path("skills")
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)
    
    if skill_name:
        skill_files = [skills_dir / f"{skill_name}.py"]
    else:
        skill_files = list(skills_dir.glob("*.py"))
    
    for skill_file in skill_files:
        skill_name = skill_file.stem
        skill_doc = skills_dir / skill_name / "SKILL.md"
        if not skill_doc.exists():
            print(f"Documentation for skill {skill_name} not found.")
            continue
        
        # Copy SKILL.md to docs/
        target_doc = docs_dir / f"{skill_name}.md"
        target_doc.write_text(skill_doc.read_text())
        print(f"Generated docs for skill {skill_name}.")
    
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate documentation for local-agent-skills.")
    parser.add_argument("--skill", help="Skill name to document.")
    args = parser.parse_args()
    
    if not generate_docs(args.skill):
        sys.exit(1)


if __name__ == "__main__":
    main()