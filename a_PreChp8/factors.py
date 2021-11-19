user_input = int(input("Enter a positive number: "))

if user_input > 0:
    for num in range(1, user_input + 1):
        if user_input % num == 0:
            print(f"{num} is a factor of {user_input}")
else:
    print("That is not a positive number")
