""" Write a programme which generates poetry"""

import random

def choose_a_or_an(word):
    if word[0] == "a" or word[0] == "e" or word[0] == "i" \
        or word[0] == "o" or word[0] == "u":
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

random_noun_1 = random.choice(nouns)
random_noun_2 = random.choice(nouns)
random_noun_3 = random.choice(nouns)

random_verb_1 = random.choice(verbs)
random_verb_2 = random.choice(verbs)
random_verb_3 = random.choice(verbs)

random_adjective_1 = random.choice(adjectives)
random_adjective_2 = random.choice(adjectives)
random_adjective_3 = random.choice(adjectives)

random_adverb = random.choice(adverbs)

random_preposition_1 = random.choice(prepositions)
random_preposition_2 = random.choice(prepositions)


print(f"{choose_a_or_an(random_adjective_1)} {random_noun_1}")

print()

print(f"{choose_a_or_an(random_adjective_1)} {random_noun_1} {random_verb_1} \
{random_preposition_1} the {random_adjective_2} {random_noun_2}")

print(f"{random_adverb}, the {random_noun_1} {random_verb_2}")

print(f"the {random_noun_2} {random_verb_3} {random_preposition_2} \
{choose_a_or_an(random_adjective_3).lower()} {random_noun_3}")
