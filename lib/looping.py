#!/usr/bin/env python3

def happy_new_year():
    n = 10
    while n > 0:
        print(n)
        n -= 1
        print("Happy New Year!")
    

def square_integers(int_list):
    sq_list = []
    for num in int_list:
        sq = num * num
        sq_list.append(sq)
    return sq_list
        

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

