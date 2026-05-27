# Local Agent Skills

Local-first, autonomous AI agent skill repository with standardized format, testing, and documentation.

## Features
- **Local-first**: No cloud dependencies. Skills run entirely offline.
- **Autonomous**: Skills can be discovered, installed, and tested by AI agents.
- **Standardized**: Skills follow a consistent `SKILL.md` format.
- **Modular**: Add/remove skills without rebuilding the agent.

## Quick Start
```bash
# Clone the repository
git clone https://github.com/fairyfemirins/local-agent-skills.git
cd local-agent-skills

# Install a skill
python3 scripts/install_skills.py --skill file_search

# Run a skill
python3 -m skills.file_search --pattern "TODO" --file-glob "*.py"

# Test a skill
python3 tests/test_file_search_direct.py

# Generate documentation
python3 scripts/generate_docs.py
```

## Skill Format
See [`skills/SKILL_TEMPLATE.md`](skills/SKILL_TEMPLATE.md) for the standardized format.

## License
MIT