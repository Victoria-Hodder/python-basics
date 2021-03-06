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

def count_candidate_election_wins():
    """
    Count the number of times each candidate wins in a
    run of 10,000 elections.

    The candidate wins the election if they in at least
    two of the three regions
    """
    nr_of_elections = 10_000
    count_a_wins = 0
    count_b_wins = 0

    for election in range(nr_of_elections):
        if count_candidate_regional_wins() >= 2:
            count_a_wins += 1
        else:
            count_b_wins += 1

    # print(f"candidateA_election_wins: {count_a_wins}")
    # print(f"candidateB_election_wins: {count_b_wins}")
    return count_a_wins


def calculate_percentage():
    """
    Percentage of times A wins across the three regions
    within the given nr of elections (10_000).
    """
    total_a_wins = count_candidate_election_wins()
    percentage_a_wins = (total_a_wins / 10_000) * 100
    return f"Candidate A wins {round(percentage_a_wins, 2)}% of the time"

print(calculate_percentage())
