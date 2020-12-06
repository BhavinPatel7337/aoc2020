from sys import path

with open(path[0] + '/input.txt') as f:
    passes = [int(x.translate(str.maketrans('FBLR', '0101')), 2) for x in f]

print(max(passes))
print(set(range(min(passes), max(passes))) - set(passes))