"""
Write a function called invest with three parameters: the principal
amount, the annual rate of return, and the number of years to calcu-
late.

The function should then print out the amount of the investment,
rounded to two decimal places, at the end of each year for the
specified number of years.

"""

def invest(amount, rate, years):
    year = 1
    while year <= years:
        amount = amount + (amount * rate)
        print(f"year {year}: ${amount:,.2f}")
        year += 1

amount = float(input("Enter a principle amount: "))
rate = float(input("Enter an anual percentage rate: "))
years = int(input("Enter the number of years: "))

invest(amount, rate, years)