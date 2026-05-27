import json
import tempfile
from pathlib import Path

import pytest

from skills.file_search import search_files


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


def test_search_files_content(temp_dir):
    # Create test files
    (temp_dir / "test1.txt").write_text("hello world")
    (temp_dir / "test2.txt").write_text("goodbye world")
    
    # Search for "hello"
    results = search_files("hello", path=str(temp_dir), limit=1)
    assert len(results) == 1
    assert results[0]["file"] == str(temp_dir / "test1.txt")
    assert results[0]["line"] == 1
    assert results[0]["content"] == "hello world"


def test_search_files_name(temp_dir):
    # Create test files
    (temp_dir / "config.json").write_text("{}")
    (temp_dir / "data.json").write_text("{}")
    
    # Search for "config.*"
    results = search_files("config.*", target="files", path=str(temp_dir))
    assert len(results) == 1
    assert results[0]["file"] == str(temp_dir / "config.json")


def test_search_files_limit(temp_dir):
    # Create test files
    for i in range(10):
        (temp_dir / f"test{i}.txt").write_text("hello world")
    
    # Search with limit=5
    results = search_files("hello", path=str(temp_dir), limit=5)
    assert len(results) == 5


def test_search_files_glob(temp_dir):
    # Create test files
    (temp_dir / "test.py").write_text("import os")
    (temp_dir / "test.txt").write_text("hello world")
    
    # Search only Python files
    results = search_files("import", file_glob="*.py", path=str(temp_dir))
    assert len(results) == 1
    assert results[0]["file"] == str(temp_dir / "test.py")