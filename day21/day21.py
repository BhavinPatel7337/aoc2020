from sys import path
import re

with open(path[0] + '/input.txt') as f:
    foods = [(set(x.split()), set(y.split(', '))) for x, y in re.findall(r'([\w ]+) \(contains ([\w ,]+)\)', f.read())]

allergens = {}
for f in foods:
    for a in f[1]:
        if a not in allergens:
            allergens[a] = f[0].copy()
        allergens[a] &= f[0]

for a, i in allergens.items():
    if len(i) == 1:
        for a2 in allergens:
            if a2 != a:
                allergens[a2] -= i

print(len([x for l in [list(y[0]) for y in foods] for x in l if x not in set.union(*(allergens.values()))]))
print(','.join([allergens[a].pop() for a in sorted(allergens)]))