x = 5
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print("Sorry, you can't divide by 0.")

ages = {"Alice": 22, "Bob": 27}

name = input("Who do you want to look up? ")

print(f"{name} is {ages[name]} years old.")


