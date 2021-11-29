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

user_input = input(f"What is the capital of {state}? ").lower()

while user_input != capital.lower():
    if user_input == 'exit':
        print(f"The correct answer is {capital}")
        print("Better luck next time!")
        break
    print("Nope, try again")
    user_input = input(f"What is the capital of {state}? ").lower()

if user_input == capital.lower():
    print("Yay, correct answer!")
