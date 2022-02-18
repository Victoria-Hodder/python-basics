from pathlib import Path
import csv

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
]

file_path = Path.home() / "Documents" / "daily_temps.csv"

file = file_path.open(mode='w', encoding='utf-8', newline='')

# csv writer object
writer = csv.writer(file)

for temp_list in daily_temperatures:
    writer.writerow(temp_list)

file.close()

""" Same code but shorter """

with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(daily_temperatures)
