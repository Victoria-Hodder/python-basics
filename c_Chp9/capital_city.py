import random

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta'
}

state, capital = random.choice(list(capitals.items()))

user_input = input(f"What is the capital of {state}? ")

if user_input != capital:
    print("Nope, try again")
else:
    print("Yay, correct answer!")
