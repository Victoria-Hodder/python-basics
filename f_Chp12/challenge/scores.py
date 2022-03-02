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

user_scores = {}

for item in scores_list:
    if item['name'] not in user_scores:
        user_scores[item['name']] = [] # emtpy list to add one by one the scores
    user_scores[item['name']].append(item['score'])
    # print(user_scores)

# print(user_scores)

# high_scores as a dict: {"Victoria": 45, "Meili": 56}
# high_scores = {}
# for name in user_scores:
#     high_scores[name] = max(user_scores[name])

# high_scores as a list of dicts:
# [{"name": "Victoria", "high_score": 142}, {"name": "Meili", "high_score": 62}]
high_scores = []
for name, scores in user_scores.items():
    high_scores.append({"name": name, "high_score": max(scores)})

print(high_scores)

# renaming 'score' key to 'high_score'
# for item in high_scores:
#     item['high_score'] = item['score']
#     del item['score']

# with high_scores.open(mode='w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames = ["name", "high_score"])
#     writer.writeheader()
#     writer.writerows(scores_list)
