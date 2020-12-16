from sys import path
import re

fields = {}
with open(path[0] + '/input.txt') as f:
    while (line := f.readline()):
        if (m := re.match(r'([\w ]+): (\d+\-\d+) or (\d+\-\d+)', line)):
            fields[m.group(1)] = (m.group(2).split('-'), m.group(3).split('-'))
        elif 'your ticket:' in line:
            your_ticket = [int(x) for x in f.readline().split(',')]
        elif 'nearby tickets:' in line:
            nearby = [[int(x) for x in y.split(',')] for y in f.readlines()]

def check_valid(field, ranges):
    return any(int(r[0]) <= field <= int(r[1]) for r in ranges)

possible_locations = {field: set(range(len(your_ticket))) for field in fields}
invalid_nums = []
for ticket in nearby:
    invalid_ticket = False
    for num in ticket:
        if not any(check_valid(num, ranges) for ranges in fields.values()):
            invalid_nums.append(num)
            invalid_ticket = True
    if not invalid_ticket:
        for i, num in enumerate(ticket):
            for field, ranges in fields.items():
                if not check_valid(num, ranges):
                    possible_locations[field].remove(i)
print(sum(invalid_nums))

done = False
while not done:
    done = True
    for field in fields:
        if len(possible_locations[field]) == 1:
            for field2 in fields:
                if field != field2:
                    possible_locations[field2] -= possible_locations[field]
        else:
            done = False
product = 1
for field, (location,) in possible_locations.items():
    if 'departure' in field:
        product *= your_ticket[location]
print(product)