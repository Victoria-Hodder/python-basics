from pathlib import Path

path = Path.home() / "Documents" / "hello.txt"
path.touch()
file = path.open(mode='r', encoding='utf-8')
file.close()
