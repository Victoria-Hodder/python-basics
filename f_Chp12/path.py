import pathlib
import shutil

"""Logging the home/current working directory"""

home = pathlib.Path.home()
# print(home)
# print(pathlib.Path.cwd())

"""
Creating a path
Note: this does not create the file itself, only the path
"""

file_path = home / "my_folder" / "my_file.txt"
print(file_path.exists())
# print(file_path.anchor)
# print(file_path.parent.name)


"""
Accessing file path components
"""

for directory in file_path.parents:
    print(directory)
