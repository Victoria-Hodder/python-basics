""" Review exercises """

import pathlib
import shutil

home = pathlib.Path.home()

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
