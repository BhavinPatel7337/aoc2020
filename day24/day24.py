from sys import path
import re

with open(path[0] + '/input.txt') as f:
    tiles = [re.findall(r'[sn]?[ew]', x) for x in f]

directions = {
    'e': (1, 0),
    'ne': (1, 1),
    'nw': (0, 1),
    'w': (-1, 0),
    'sw': (-1, -1),
    'se': (0, -1)
}
#     nw(0,1)     ne(1,1)
# w(-1,0)     o(0,0)      e(1,0)
#     sw(-1,-1)   se(0,-1)

black = {}
for ti in tiles:
    t = (0,0)
    for i in ti:
        d = directions[i]
        t = (t[0] + d[0], t[1] + d[1])
    black[t] = black.get(t, False) ^ True

print(sum(black.values()))

def minmax():
    x, y = zip(*black)
    return min(x), max(x), min(y), max(y)

def adjacent(x, y):
    return sum(black.get((x + d[0], y + d[1]), False) for d in directions.values())

min_x, max_x, min_y, max_y = minmax()

def flip():
    new_black = {}
    min_x, max_x, min_y, max_y = minmax()
    for y in range(min_y - 2, max_y + 2):
        for x in range(min_x - 2, max_x + 2):
            current = black.get((x, y), False)
            if current and (adjacent(x, y) == 0 or adjacent(x, y) > 2):
                new_black[x, y] = False
            elif not current and (adjacent(x, y) == 2):
                new_black[x, y] = True
            else:
                new_black[x, y] = current
    return new_black

for _ in range(100):
    black  = flip()

print(sum(black.values()))