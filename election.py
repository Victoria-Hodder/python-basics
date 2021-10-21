import random

def election(probability_A_wins):
    if random.random() < probability_A_wins:
        return "A wins"
    else:
        return "B wins"

nr_of_elections = 10_000
regions = [0.87, 0.65, 0.17]
candidateA_count = [0, 0, 0]
candidateB_count = [0, 0, 0]

for i in range(nr_of_elections):
    for count in range(0, 3):
        if election(regions[count]) == "A wins":
            candidateA_count[count] += 1
        else:
            candidateB_count[count] += 1

print(f"candidateA_count: {candidateA_count}")
print(f"candidateB_count: {candidateB_count}")
