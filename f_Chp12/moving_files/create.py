"""
Creating files and directories
Run this file first
"""

import pathlib

new_dir = pathlib.Path.home() / "new_directory"
new_dir.mkdir(exist_ok=True)

file_path = new_dir / "file1.txt"
file_path.touch()

nested_dir = new_dir / "folder_a" / "folder_b"
nested_dir.mkdir(parents=True, exist_ok=True)

file_path2 = new_dir / "folder_c" / "file2.txt"
file_path2.parent.mkdir(exist_ok=True)
file_path2.touch()

