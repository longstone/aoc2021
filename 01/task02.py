import sys

filename = "input/day01.txt"
sallyUp = 0
lines = map(lambda x: int(x),open(filename, "r").readlines() )
for x in range(3, len(lines)):
    if lines[x - 3] + lines[x - 2] + lines[x - 1] < lines[x - 2] + lines[x - 1] + lines[x]:
        sallyUp += 1

print sallyUp
