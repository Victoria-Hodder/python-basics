
# while True:
#     try: 
#         some_input = int(input("Enter an int: "))
#         print("Thank you!")
#         break
#     except ValueError:
#         print("That is not an int. Try again.")

"""
Write a program that asks the user to input a string and an integer
(n), then displays the character at index n in the string.
Use error handling to make sure the program doesn’t crash
if the user enters something other than an integer or if the index
is out of bounds. The program should display a different message
depending on which error occurs.

"""
user_str = input("Enter a string: ")

try:
    user_idx = int(input("Enter an integer: "))
    print(f"The letter at index {user_idx} is '{user_str[user_idx]}'")
except ValueError:
    print("You must enter an integer")
except IndexError:
    print("Index out of bounds")
