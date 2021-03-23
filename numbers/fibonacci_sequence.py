#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Generate Fibonaci sequence untill given number')
parser.add_argument('number', type=int, help='Given max number of fibonacci sequence')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()
number = args.number

def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

for index, fibonacci_number in zip(range(number), fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))