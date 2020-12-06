from sys import path

with open(path[0] + '/input.txt') as f:
    answers = f.read().split('\n\n')

print(sum(len(set(x) - {'\n'}) for x in answers))
print(sum(len(set.intersection(*(set(y) for y in x.split()))) for x in answers))