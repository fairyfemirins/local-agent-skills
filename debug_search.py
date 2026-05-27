from skills.file_search import search_files
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    for i in range(10):
        (tmpdir / f"test{i}.txt").write_text("hello world")
    
    results = search_files("hello", path=str(tmpdir), limit=5)
    print(f"Results: {len(results)}")
    print(results)