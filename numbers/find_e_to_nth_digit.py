#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Find e to the Nth digit')
parser.add_argument('number', type=float, help='A number (e) to take digits from')
parser.add_argument('--limit', '-l', type=int, help='the Nth digit')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()
number = args.number
limit = args.limit

if limit:
    splitted = str(number).split(".")
    decimals = splitted[1][:limit]
    out = splitted[0] + "." + decimals
    print(float(out))
else:
    print(number)
  
