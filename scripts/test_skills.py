#!/usr/bin/env python3
"""
Run tests for all skills.
"""
import argparse
import subprocess
import sys
from pathlib import Path


def run_tests(skill_name: str | None = None) -> bool:
    """Run tests for a specific skill or all skills."""
    test_dir = Path("tests")
    if skill_name:
        test_file = test_dir / f"test_{skill_name}.py"
        if not test_file.exists():
            print(f"Test file for skill {skill_name} not found.")
            return False
        cmd = ["pytest", str(test_file)]
    else:
        cmd = ["pytest", str(test_dir)]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Run tests for local-agent-skills.")
    parser.add_argument("--skill", help="Skill name to test.")
    args = parser.parse_args()
    
    if not run_tests(args.skill):
        sys.exit(1)


if __name__ == "__main__":
    main()