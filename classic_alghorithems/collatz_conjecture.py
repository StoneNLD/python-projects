#!/usr/bin/env python 
import argparse

parser = argparse.ArgumentParser(description='Find the number of steps it takes to reach one using collatz conjecture')
parser.add_argument('number', type=int, help='The number to count the amount of steps on')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()
number = args.number

x = number
count_even = 0
count_odd = 0

while x > 1:
    if x % 2 == 0:
        count_even += 1
        x = x / 2
    else:
        count_odd += 1
        x = x * 3 + 1
print(f"Amount of Even loops is {count_even}")
print(f"Amount of Odd loops is {count_odd}")
