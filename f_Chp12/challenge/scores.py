import csv
from pathlib import Path

high_scores = Path.home() / "Documents" / "high_scores.csv"
scores = Path.home() / "workspace" / "python-basics" / "f_Chp12" / "challenge" / "scores.csv"

scores_dict = {}

# Make score value an integer
def process_row(row):
    row['score'] = int(row['score'])
    return row

scores_list = []
with scores.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # print(process_row(row))
        scores_list.append(process_row(row))

# print(scores_list)

# Do something to find max scores here?
user_scores = {}

for item in scores_list:
    if item['name'] not in user_scores:
        user_scores[item['name']] = [] # emtpy list to add one by one the scores

print(user_scores)

# here add the score in the list of that name
# you could also keeping only the max score instead of making a scores list and then doing max to them

# renaming 'score' key to 'high_score'
for item in scores_list:
    item['high_score'] = item['score']
    del item['score']

with high_scores.open(mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "high_score"])
    writer.writeheader()
    writer.writerows(scores_list)
