#!/usr/local/env python

my_file = open('xmen.txt', 'w+')
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops',
    'Bishop',
    'Nightcrawler',
])
my_file = open('xmen.txt', 'r')
print(my_file.read())
my_file.close()

#or better, auto close opened file.
with open('xmen.txt', 'w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler\n',
    ])

my_file = open('xmen.txt', 'r')
with my_file:
    print(my_file.read())