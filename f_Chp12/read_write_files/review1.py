from pathlib import Path

path = Path.home() / "Documents" / "starships.txt"

lines_of_text = [
    "Discovery\n",
    "Enterprise\n",
    "Defiant\n",
    "Voyager\n"
]

with path.open(mode='w', encoding='utf-8') as file:
    file.writelines(lines_of_text)

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end="")
