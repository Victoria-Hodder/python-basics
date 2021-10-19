""" Exercise 8.8 """
import random

def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

def flips_to_get_both():
    """ 
    Flip coins until both heads and tails appear and return the 
    number of required flips 
    """
    # Initiate a counter to count number of heads/tails
    heads_count = 0
    tails_count = 0

    # Loop until both heads and tails are at least 1
    while heads_count < 1 or tails_count < 1:
        # Execute the function and add to relevant counts
        if coin_flip() == "heads":
            heads_count += 1
        else:
            tails_count += 1

    # Count flips needed until both heads and tails are present
    if heads_count >= 1 and tails_count >= 1:
        flips_needed = heads_count + tails_count
        return flips_needed


def average_num_flips():
    """ Average the number of flips needed in a certain number of trials """

    # Set the number of trials
    num_trials = 10_000
    # Set an empty counter to collect the number of flips
    total_num_flips = 0

    # Iterate through the num_trials and add to the counter
    for trial in range(num_trials):
        total_num_flips += flips_to_get_both()

    # Calculate the average
    average = total_num_flips / num_trials
    return average

print(average_num_flips())
