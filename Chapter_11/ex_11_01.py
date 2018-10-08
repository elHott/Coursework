print('Exercise 11 01')
fname = input('Enter the file name: ')
if len(fname) < 1: fname = 'regex_sum_42.txt'
hand = open(fname)
# print(hand)


import re
numlist = list()
count = 0

for line in hand:
    line = line.rstrip()
#    print(line)
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0 : continue
    for n in stuff:
        num = int(n)
        numlist.append(num)
        count = count + 1
#    print(stuff)

print('Sum is: ', sum(numlist))
print('Count is: ', count)
