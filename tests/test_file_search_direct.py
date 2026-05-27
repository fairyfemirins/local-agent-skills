import json
import tempfile
import sys
from pathlib import Path

# Add skills/ to Python path
sys.path.append(str(Path("skills").resolve()))

from file_search import search_files


def test_search_files_content():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        (tmpdir / "test1.txt").write_text("hello world")
        (tmpdir / "test2.txt").write_text("goodbye world")
        
        results = search_files("hello", path=str(tmpdir), limit=1)
        assert len(results) == 1
        assert results[0]["file"] == str(tmpdir / "test1.txt")
        assert results[0]["line"] == 1
        assert results[0]["content"] == "hello world"


def test_search_files_name():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        (tmpdir / "config.json").write_text("{}")
        (tmpdir / "data.json").write_text("{}")
        
        results = search_files("config.*", target="files", path=str(tmpdir))
        assert len(results) == 1
        assert results[0]["file"] == str(tmpdir / "config.json")


def test_search_files_limit():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        for i in range(10):
            (tmpdir / f"test{i}.txt").write_text("hello world")
        
        results = search_files("hello", path=str(tmpdir), limit=5)
        assert len(results) == 5


def test_search_files_glob():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        (tmpdir / "test.py").write_text("import os")
        (tmpdir / "test.txt").write_text("hello world")
        
        results = search_files("import", file_glob="*.py", path=str(tmpdir))
        assert len(results) == 1
        assert results[0]["file"] == str(tmpdir / "test.py")


if __name__ == "__main__":
    test_search_files_content()
    test_search_files_name()
    test_search_files_limit()
    test_search_files_glob()
    print("All tests passed!")