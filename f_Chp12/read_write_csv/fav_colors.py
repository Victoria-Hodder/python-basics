import csv
from pathlib import Path

favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]

file_path = Path.home() / "Documents" / "favorite_colors.csv"

with file_path.open(mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "favorite_color"])
    writer.writeheader()
    writer.writerows(favorite_colors)

favorite_colors_list = []
with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        favorite_colors_list.append(row)

print(favorite_colors_list)
