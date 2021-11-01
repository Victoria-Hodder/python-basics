import random

def simulate_vote(probability_a_wins):
    """
    Randomly returns a winning candidate.
    """
    if random.random() < probability_a_wins:
        return "A"
    else:
        return "B"


def count_candidate_regional_wins():
    """
    Counts the number of times each candidate wins
    in each of the three regions in one election run.

    For simplicity this function only returns a list
    of the count candidate A wins in each region
    """
    # List containing probability that A wins in each region
    regions = [0.87, 0.65, 0.17]
    candidate_a_count = [0, 0, 0]
    candidate_b_count = [0, 0, 0]

    for count in range(0, 3):
        if simulate_vote(regions[count]) == "A":
            candidate_a_count[count] += 1
        else:
            candidate_b_count[count] += 1

    return sum(candidate_a_count)

nr_of_elections = 10_000
total_a_wins = 0
total_b_wins = 0

for election in range(nr_of_elections):
    if count_candidate_regional_wins() >= 2:
        total_a_wins += 1
    else:
        total_b_wins += 1

percentage_a_wins = (total_a_wins / 10_000) * 100
print(f"Candidate A wins {round(percentage_a_wins, 2)}% of the time")
