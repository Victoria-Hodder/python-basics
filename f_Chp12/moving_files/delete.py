
"""
Moving, renaming and deleting
First create.py and search.py needs to be run
"""

import pathlib

new_dir = pathlib.Path.home() / "new_directory"
# new_dir.mkdir(exist_ok=True)

source = new_dir / "file1.txt"
destination = new_dir / "folder_a" / "file1.txt"

## Only move file if it doesn't exist in destination
if not destination.exists():
    source.replace(destination)

source = new_dir / "folder_c"
destination = new_dir / "folder_d"
# source.replace(destination)

## Deleting a file
file_path3 = new_dir / "program1.py"
# file_path3.unlink(missing_ok=True)

# for path in new_dir.iterdir():
#     print(path)

## Deleting a directory
folder_d = new_dir / "folder_d"

# for path in folder_d.iterdir():
#     path.unlink(missing_ok=True)
#
# folder_d.rmdir()

## To delete directory with contents
folder_a = new_dir / "folder_a"
# shutil.rmtree(folder_a)

# print(folder_a.exists())
# print(list(new_dir.rglob("image*.*")))
