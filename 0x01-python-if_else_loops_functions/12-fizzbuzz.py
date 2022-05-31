#!/usr/bin/env python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end="")
        elif i % 5 == 0:
            print("Buzz", end="")
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end="")
        else:
            print(f"{i:d}", end="")
        print(" ", end="")
