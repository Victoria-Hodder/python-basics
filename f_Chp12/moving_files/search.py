"""
Searching for files/directories
First create.py needs to be run
"""

import pathlib

new_dir = pathlib.Path.home() / "new_directory"
new_dir.mkdir(exist_ok=True)

# for path in new_dir.glob('*.txt'):
#     print(path)

paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png",
    ]

for path in paths:
    path.touch()

for path in new_dir.rglob('*.py'):
    print(path)

