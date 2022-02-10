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
# print(file_path.exists())
# print(file_path.anchor)
# print(file_path.parent.name)


"""
Accessing file path components
"""

# for directory in new_text.parents:
#     print(directory)


"""
Creating files and directories
"""

new_dir = pathlib.Path.home() / "new_directory"
# new_dir.mkdir(exist_ok=True)

file_path = new_dir / "file1.txt"
# file_path.touch()

nested_dir = new_dir / "folder_a" / "folder_b"
# nested_dir.mkdir(parents=True, exist_ok=True)

file_path2 = new_dir / "folder_c" / "file2.txt"
# file_path2.parent.mkdir(exist_ok=True)
# file_path2.touch()


"""
Searching for files/directories
"""

# for path in new_dir.glob('*.txt'):
#     print(path)

paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png",
]

# for path in paths:
#     path.touch()

# for path in new_dir.rglob('*.py'):
#     print(path)


"""
Moving, renaming and deleting
"""

source = new_dir / "file1.txt"
destination = new_dir / "folder_a" / "file1.txt"

## Only move file if it doesn't exist in destination
# if not destination.exists():
#     source.replace(destination)

source = new_dir / "folder_c"
destination = new_dir / "folder_d"
# source.replace(destination)

## Deleting a file
file_path3 = new_dir / "program1.py"
file_path3.unlink(missing_ok=True)

# for path in new_dir.iterdir():
#     print(path)

## Deleting a directory
folder_d = new_dir / "folder_d"

# for path in folder_d.iterdir():
#     path.unlink(missing_ok=True)

# folder_d.rmdir()

## To delete directory with contents
folder_a = new_dir / "folder_a"
# shutil.rmtree(folder_a)

# print(folder_a.exists())
# print(list(new_dir.rglob("image*.*")))

""" Review exercises """

my_dir = home / "my_folder"
my_dir.mkdir(exist_ok=True)

my_paths = [
    my_dir / "file1.txt",
    my_dir / "file2.txt",
    my_dir / "image1.png"
]

# for path in my_paths:
#     path.touch()

img_dir = my_dir / "Images"
# img_dir.mkdir(exist_ok=True)

source = my_dir / "image1.png"
destination = my_dir / "Images" / "image1.png"
# source.replace(destination)

file1 = my_dir / "file1.txt"
# file1.unlink()

# shutil.rmtree(my_dir)
