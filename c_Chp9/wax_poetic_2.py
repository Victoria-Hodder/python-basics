"""
Wax poetic with functions
Based on given answer in Real Python:
https://github.com/realpython/python-basics-exercises/blob/master/ch09-lists-tuples-and-dictionaries/5-challenge-wax-poetic.py
"""

import random

nouns = ["fossil",
         "horse",
         "aardvark",
         "judge",
         "chef",
         "mango",
         "extrovert",
         "gorilla"]

verbs = ["kicks",
         "jingles",
         "bounces",
         "slurps",
         "meows",
         "explodes",
         "curdles"]

adjectives = ["furry",
              "balding",
              "incredulous",
              "fragrant",
              "exuberant",
              "glistening"]

prepositions = ["against",
                "after",
                "into",
                "beneath",
                "upon",
                "for",
                "in",
                "like",
                "over",
                "within"]

adverbs = ["curiously",
           "extravagantly",
           "tantalizingly",
           "furiously",
           "sensuously"]


def choose_article(word):
    """
    Decides if a word is preceded by "a" or "an" depending on
    the first letter of the word
    """
    if word[0] in ["a", "e", "i", "o", "u"]:
        return f"An {word}"
    else:
        return f"A {word}"

def make_poem():
    """ Generate a poem with random words """

    # Pull random nouns
    noun_1 = random.choice(nouns)
    noun_2 = random.choice(nouns)
    noun_3 = random.choice(nouns)

    while noun_1 == noun_2:
        noun_2 = random.choice(nouns)
    while noun_1 == noun_3 or noun_2 == noun_3:
        noun_3 = random.choice(nouns)

    # Pull random verbs
    verb_1 = random.choice(verbs)
    verb_2 = random.choice(verbs)
    verb_3 = random.choice(verbs)

    while verb_1 == verb_2:
        verb_2 = random.choice(verbs)
    while verb_1 == verb_3 or verb_2 == verb_3:
        verb_3 = random.choice(verbs)

    # Pull random adjectives
    adj_1 = random.choice(adjectives)
    adj_2 = random.choice(adjectives)
    adj_3 = random.choice(adjectives)

    while adj_1 == adj_2:
        adj_2 = random.choice(adjectives)
    while adj_1 == adj_3 or adj_2 == adj_3:
        adj_3 = random.choice(adjectives)

    # Pull random prepositions
    prep_1 = random.choice(prepositions)
    prep_2 = random.choice(prepositions)

    while prep_1 == prep_2:
        prep_2 = random.choice(prepositions)

    # Pull a random adverb
    adverb = random.choice(adverbs)

    # Use random words to create a poem
    poem = (
            f"{choose_article(adj_1)} {noun_1}\n\n"
            f"{choose_article(adj_1)} {noun_1} {verb_1} {prep_1} the {adj_2} {noun_2}\n"
            f"{adverb}, the {noun_1} {verb_2}\n"
            f"the {noun_2} {verb_3} {prep_2} {choose_article(adj_3).lower()} {noun_3}"
    )

    return poem

poem = make_poem()
print(poem)
