from sys import path
import re

with open(path[0] +"/input.txt") as f:
    passwords = [re.match(r'(\d+)\-(\d+) (\w): (\w+)', x).groups() for x in f]

print(sum(int(p[0]) <= p[3].count(p[2]) <= int(p[1]) for p in passwords))
print(sum((p[3][int(p[0]) - 1] == p[2]) ^ (p[3][int(p[1]) - 1] == p[2]) for p in passwords))