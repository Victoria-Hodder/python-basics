"""
1. Write a function called roll() that uses randint() to simulate rolling
a fair die by returning a random integer between 1 and 6 .

"""

import random

def roll():
    return random.randint(1,6)


"""
2. Write a program that simulates ten thousand rolls of a fair die and
displays the average number rolled.

"""

num_throws = 10_000
total = 0

for n in range(num_throws):
    total += roll()

avg_num = total / num_throws
print(f"The average num of {num_throws} throws is {avg_num}")
