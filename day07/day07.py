from sys import path
import re

with open(path[0] + '/input.txt') as f:
    rules = dict((y[0], re.findall(r'(\d+) (\w+ \w+) bag', y[1])) for x in f if (y := x.split(' bags contain ')))

def parent_bags(rules, colour):
    return [k for k, v in rules.items() if any(i[1] == colour for i in v)]

checklist = ['shiny gold']
baglist = set()
while checklist:
    if (c := checklist.pop()) not in baglist:
        checklist += parent_bags(rules, c)
        baglist.add(c)

print(len(baglist - {'shiny gold'}))

def count_child_bags(rules, colour):
    return 1 + sum(int(i[0]) * count_child_bags(rules, i[1]) for i in rules[colour])

print(count_child_bags(rules, 'shiny gold') - 1)