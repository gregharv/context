from pathlib import Path

_dir = Path(__file__).parent

def get(name="default"):
    return (_dir / f"{name}.md").read_text()
