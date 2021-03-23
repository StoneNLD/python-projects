#!/usr/bin/env python
import argparse
from math import pi as p

parser = argparse.ArgumentParser(description='Find pi to the Nth digit')
parser.add_argument('--limit', '-l', type=int, help='the Nth digit')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()
limit = args.limit

if limit:
    # +2 because pi starts with "3." We want the limit starting at the decimals.
    f = limit + 2
    p_str = str(p)
    print(p_str[:f])
else:
    print(p)
  
