#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -1 * number
    neg_number = -1 * (number % 10)
    if neg_number < 6 and neg_number != 0:
        print(f"Last digit of {number * -1} is {neg_number} and is less than 6 and not 0")
else:
    last_digit = number % 10
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    if last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    if last_digit < 6 and last_digit != 0:
        print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
