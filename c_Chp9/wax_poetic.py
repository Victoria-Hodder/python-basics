""" Write a programme which generates poetry"""

import random

def choose_article(word):
    """
    Decides if a word is preceded by "a" or "an" depending on
    the first letter of the word
    """
    if word[0] in ["a", "e", "i", "o", "u"]:
        return f"An {word}"
    else:
        return f"A {word}"

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

""" Assign random words """
noun_1 = random.choice(nouns)
noun_2 = random.choice(nouns)
noun_3 = random.choice(nouns)

verb_1 = random.choice(verbs)
verb_2 = random.choice(verbs)
verb_3 = random.choice(verbs)

adj_1 = random.choice(adjectives)
adj_2 = random.choice(adjectives)
adj_3 = random.choice(adjectives)

adverb = random.choice(adverbs)

prep_1 = random.choice(prepositions)
prep_2 = random.choice(prepositions)

""" Print poem to the console """
print(f"{choose_article(adj_1)} {noun_1}")

print()

print(f"{choose_article(adj_1)} {noun_1} {verb_1} \
{prep_1} the {adj_2} {noun_2}")

print(f"{adverb}, the {noun_1} {verb_2}")

print(f"the {noun_2} {verb_3} {prep_2} \
{choose_article(adj_3).lower()} {noun_3}")
