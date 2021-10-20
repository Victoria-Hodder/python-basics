# create a function for probability A wins

import random

def election(probability_A_wins):
    if random.random() < probability_A_wins:
        return "A wins"
    else:
        return "B wins"

# print(election(0.87))
# print(election(0.65))
# print(election(0.17))

no_of_elections = 10_000
region1 = 0.87
region2 = 0.65
region3 = 0.17

candidateA_count = 0
candidateB_count = 0

for i in range(no_of_elections):
    if election(region1) == "A wins":
        candidateA_count += 1
    else:
        candidateB_count += 1

print(f"candidateA_count: {candidateA_count}")
print(f"candidateB_count: {candidateB_count}")

percentage = (candidateA_count / 10_000) * 100

print(f"Percentage A wins: {round(percentage, 2)}")
