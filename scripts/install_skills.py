#!/usr/bin/env python3
"""
Install skills into the local environment.
"""
import argparse
import importlib.util
import os
import sys
from pathlib import Path


def install_skill(skill_name: str) -> bool:
    """Install a skill by creating a symlink in the skills/ directory."""
    skill_path = Path(f"skills/{skill_name}.py")
    if not skill_path.exists():
        print(f"Skill {skill_name} not found.")
        return False
    
    # Add skills/ to Python path
    skills_dir = Path("skills").resolve()
    if str(skills_dir) not in sys.path:
        sys.path.append(str(skills_dir))
    
    print(f"Skill {skill_name} installed successfully.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Install skills for local-agent-skills.")
    parser.add_argument("--skill", required=True, help="Skill name to install.")
    args = parser.parse_args()
    
    if not install_skill(args.skill):
        sys.exit(1)


if __name__ == "__main__":
    main()