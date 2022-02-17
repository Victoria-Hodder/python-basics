""" Reading data from file """
from pathlib import Path

path = Path.home() / "Documents" / "hello.txt"

# with path.open(mode='a', encoding='utf-8') as file:
#     file.write('\nHere is some more coffee')

lines_of_text = [
    "And for me, now as then, it is too much \n",
    "There is too much world \n"
]

with path.open(mode='w', encoding='utf-8') as file:
    file.writelines(lines_of_text)

with path.open(mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line, end="")

new_path = Path.home() / "Documents" / "new_file.txt"
with new_path.open(mode='w', encoding='utf-8') as file:
    file.write("It is windy today")

path = Path.home() / "Documents" / "new_folder" / "new_file.txt"

path.parent.mkdir(parents=True)
with path.open(mode='w', encoding='utf-8') as file:
    file.write("I love the wind")
