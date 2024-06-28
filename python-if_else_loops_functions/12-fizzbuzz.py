#!/usr/bin/python3
for i in range(1, 101):
    if i % 3 == 0:
        print('Fizz ', end="")
        #code for multiples of three
    elif i % 5 == 0:
        print('Buzz ', end="")
        #code for multiples of five
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz ', end="")
        #code for multiples of three and five
    else:
        print('{} '.format(i), end="")
