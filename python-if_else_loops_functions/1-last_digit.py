#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10
message = f"Last digit of {number} is {last_number}"
if last_number > 5:
    message += " and is greater than 5"
elif last_number == 0:
    message += " and is 0"
else:
    message += " and is less than 6 and not 0"
print(message)
