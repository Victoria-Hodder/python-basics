from pathlib import Path
import csv

employees = [
    ["name","department","salary"],
    ["Lee","Operations","75000.00"],
    ["Jane","Engineering","85000.00"],
    ["Diego","Sales","80000.00"]
]

file_path = Path.home() / "Documents" / "employees.csv"

with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees)

# file = file_path.open(mode="r", encoding="utf-8", newline="")
# reader = csv.DictReader(file)
#
# # print(reader.fieldnames)
#
# for row in reader:
#     print(row)
#
# file.close()

def process_row(row):
    row["salary"] = float(row["salary"])
    return row

with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(process_row(row))
