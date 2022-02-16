"""
Create a new folder in the practice_files folder called images/ , and
move all image ﬁles to that folder. When you’re done, the new folder
should have four ﬁles in it.
"""

from pathlib import Path

"""
cwd = pathlib.Path.cwd()
img_dir = cwd / "practice_files" / "images"
# img_dir.mkdir(exist_ok=True)

docs_dir = cwd / "practice_files" / "documents"

image1_source = docs_dir / "image1.png"
image1_destination = img_dir / "image1.png"
if not image1_destination.exists():
    image1_source.replace(image1_destination)

image2_source = docs_dir / "more_files" / "image2.gif"
image2_destination = img_dir / "image2.gif"
if not image2_destination.exists():
    image2_source.replace(image2_destination)

image3_source = docs_dir / "files" / "additional files" / "image3.png"
image3_destination = img_dir / "image3.png"
if not image3_destination.exists():
    image3_source.replace(image3_destination)

image4_source = docs_dir / "more_files" / "even_more_files" / "image4.jpg"
image4_destination = img_dir / "image4.png"
if not image4_destination.exists():
    image4_source.replace(image4_destination)
"""

""" More practice moving files for myself """


chp12_dir = (
    Path.home() /
    "workspace" /
    "python-basics" /
    "f_Chp12"
)

# print(chp12_dir)

destination = chp12_dir / "moving_files"

for path in destination.glob('*.py'):
    path.replace(destination / path.name)
