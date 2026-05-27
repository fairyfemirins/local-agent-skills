# Skill: file_search

## Description
Local-first file search skill for AI agents. Search files by content or name using regex patterns.

## Requirements
- Python 3.10+
- Dependencies: None

## Usage
```bash
# Install the skill
python scripts/install_skills.py --skill file_search

# Search for "TODO" in Python files
python -m skills.file_search --pattern "TODO" --file-glob "*.py"

# Find files named "config.*"
python -m skills.file_search --pattern "config.*" --target files
```

## Input/Output
- **Input**: CLI arguments (`--pattern`, `--target`, `--path`, `--file-glob`, `--limit`).
- **Output**: JSON array of matches with `file`, `line` (if content search), and `content`.

## Example
```bash
# Search for "import" in Python files
python -m skills.file_search --pattern "import" --file-glob "*.py"
```

## Testing
```bash
# Run tests for this skill
python -m pytest tests/test_file_search.py
```

## License
MIT