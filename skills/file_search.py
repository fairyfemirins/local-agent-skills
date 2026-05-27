"""
Local-first file search skill for AI agents.
"""
import argparse
import json
import os
import re
from pathlib import Path
from typing import List, Dict


def search_files(
    pattern: str, 
    target: str = "content", 
    path: str = ".", 
    file_glob: str = "*", 
    limit: int = 50,
) -> List[Dict[str, str]]:
    """
    Search files by content or name.
    
    Args:
        pattern: Regex pattern to search for.
        target: 'content' or 'files'.
        path: Directory to search in.
        file_glob: File glob pattern (e.g., '*.py').
        limit: Max results to return.
    
    Returns:
        List of matches with file path and line number (if content search).
    """
    matches = []
    path = str(Path(path).resolve())
    
    if target == "files":
        for file in Path(path).glob(file_glob):
            if file.is_file() and re.search(pattern, file.name):
                matches.append({"file": str(file)})
                if len(matches) >= limit:
                    break
    else:
        for file in Path(path).glob(file_glob):
            if file.is_file():
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        for i, line in enumerate(f, 1):
                            if re.search(pattern, line):
                                matches.append({
                                    "file": str(file),
                                    "line": i,
                                    "content": line.strip(),
                                })
                                if len(matches) >= limit:
                                    break
                    if len(matches) >= limit:
                        break
                except (UnicodeDecodeError, PermissionError):
                    continue
    
    return matches


def main():
    parser = argparse.ArgumentParser(description="Local-first file search skill.")
    parser.add_argument("--pattern", required=True, help="Regex pattern to search for.")
    parser.add_argument("--target", default="content", choices=["content", "files"], help="Search target.")
    parser.add_argument("--path", default=".", help="Directory to search in.")
    parser.add_argument("--file-glob", default="*", help="File glob pattern.")
    parser.add_argument("--limit", type=int, default=50, help="Max results to return.")
    args = parser.parse_args()
    
    results = search_files(
        pattern=args.pattern,
        target=args.target,
        path=args.path,
        file_glob=args.file_glob,
        limit=args.limit,
    )
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()