from pathlib import Path
import csv

people = [
    {"name": "Veronica", "age": 29},
    {"name": "Audrey", "age": 32},
    {"name": "Sam", "age": 24},
]

file_path = Path.home() / "Documents" / "people.csv"

# file = file_path.open(mode="w", encoding="utf-8", newline="")
# writer = csv.DictWriter(file, fieldnames=["name", "age"])
# writer.writeheader()
# writer.writerows(people)
# file.close()

with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(people)
