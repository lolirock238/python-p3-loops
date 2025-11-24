#!/usr/bin/env python3

def happy_new_year():
    """
    Count down from 10 to 1 using a while loop,
    then print 'Happy New Year!'
    """
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    """
    Return a new list with each integer squared using list comprehension
    """
    return [num ** 2 for num in int_list]


def fizzbuzz():
    """
    Print numbers from 1 to 100, but:
    - Print 'Fizz' for multiples of 3
    - Print 'Buzz' for multiples of 5
    - Print 'FizzBuzz' for multiples of both 3 and 5
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)