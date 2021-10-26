import random

def simulate_election(probability_A_wins):
    """
    Returns a winning candidate for an individual election run.
    """
    if random.random() < probability_A_wins:
        return "A"
    else:
        return "B"


def count_candidate_wins():
    """
    Counts the number of times each candidate wins
    in each of the three regions.
    """
    nr_of_elections = 10_000
    # List probability that A wins in each region
    regions = [0.87, 0.65, 0.17]
    candidateA_count = [0, 0, 0]
    candidateB_count = [0, 0, 0]

    for election in range(nr_of_elections):
        for count in range(0, 3):
            if simulate_election(regions[count]) == "A":
                candidateA_count[count] += 1
            else:
                candidateB_count[count] += 1

    print(f"candidateA_count: {candidateA_count}")
    print(f"candidateB_count: {candidateB_count}")
    return sum(candidateA_count)

def calculate_percentage():
    """
    Percentage of times A wins across the three regions
    within the given nr of elections (10_000).
    """
    total_a_wins = count_candidate_wins()
    percentage_a_wins = (10_000 / total_a_wins) * 100
    return f"Candidate A wins {round(percentage_a_wins, 2)}% of the time"

print(calculate_percentage())

"""
Left to do: "assume that a candidate wins the election if
they win in at least two of the three regions."
"""