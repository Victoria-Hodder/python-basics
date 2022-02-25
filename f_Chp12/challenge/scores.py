import csv
from pathlib import Path

high_scores = Path.home() / "Documents" / "high_scores.csv"
scores = Path.home() / "workspace" / "python-basics" / "f_Chp12" / "challenge" / "scores.csv"

scores_dict = {}

def process_row(row):
    row['score'] = int(row['score'])
    return row

scores_list = []
with scores.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        scores_list.append(process_row(row))

# Do something to find max scores here?

# This only returns the highest score in the whole list
max_score = max([item['score'] for item in scores_list])
print(max_score)

for item in scores_list:
    for key, value in item.items():
        print(f"{key}: {value}")

# Create a new list 'high_scores'
# Add the items to the list where each unique name has a highest score

# renaming 'score' key to 'high_score'
for item in scores_list:
    item['high_score'] = item['score']
    del item['score']

with high_scores.open(mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "high_score"])
    writer.writeheader()
    writer.writerows(scores_list)
