word = input("Enter a word: ")

if len(word) < 5:
    print("Your input is less than 5 characters long")
elif len(word) > 5:
    print("Your input is greater than 5 characters long")
else:
    print("Your input is 5 chars long")


print("I'm thinking of a number between 1 and 10.")
user_guess = int(input("Guess which one: "))

if user_guess == 3:
    print("You win!")
else:
    print("You lose!")
