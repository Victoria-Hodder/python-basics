# create a function for probability A wins

import random

def region(probability_A_wins):
    if random.random() < probability_A_wins:
        return "A wins"
    else:
        return "B wins"

print(region(0.87))
print(region(0.65))
print(region(0.17))
