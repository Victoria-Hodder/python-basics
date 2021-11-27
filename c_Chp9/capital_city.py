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

while user_input.title() != capital:
    if user_input.lower() == 'exit':
        print(f"The correct answer is {capital}")
        print("Better luck next time!")
        break
    
    print("Nope, try again")
    user_input = input(f"What is the capital of {state}? ")

if user_input.title() == capital:
    print("Yay, correct answer!")
