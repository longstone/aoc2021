import sys

filename = "input/day01.txt"
sallyUp = 0
with open(filename) as file:
    old = sys.maxsize
    for line in file:
        if int(old) < int(line):
            sallyUp += 1
        old = line
print(sallyUp)