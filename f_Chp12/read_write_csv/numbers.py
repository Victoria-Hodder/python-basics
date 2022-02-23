from pathlib import Path
import csv

numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

file_path = Path.home() / "Documents" / "numbers.csv"

with file_path.open(mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(numbers)

numbers = []
with file_path.open(mode='r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        number = [int(value) for value in row]
        numbers.append(number)

print(numbers)
