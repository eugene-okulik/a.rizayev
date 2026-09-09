import random

salary = int(input("What's your salary? "))
is_bonus = random.choice((True, False))
total = salary

if is_bonus:
    total += random.randint(100, 1000)

print(f"{salary}, {is_bonus} - '${total}'")
