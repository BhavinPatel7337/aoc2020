from sys import path

active = set()
with open(path[0] + '/input.txt') as f:
    for y, row in enumerate(f):
        for x, state in enumerate(row.strip()):
            if state == '#': 
                active.add((x, y, 0, 0))
initial_size = (x + 1, y + 1)

directions = [(x, y, z, w) for x in range(-1, 2)
                for y in range(-1, 2)
                for z in range(-1, 2)
                for w in range(-1, 2)
                if any([x != 0, y != 0, z != 0, w != 0])]

def iterate(active, wrange, cycle):
    global initial_size
    new_active = set()
    for w in wrange:
        for z in range(-cycle, cycle + 1):
            for y in range(-cycle, initial_size[1] + cycle):
                for x in range(-cycle, initial_size[0] + cycle):
                    neighbours = [(x + dx, y + dy, z + dz, w + dw) for dx, dy, dz, dw in directions]
                    active_neighbours = sum(i in active for i in neighbours)
                    if active_neighbours == 3 or ((x, y, z, w) in active and active_neighbours == 2):
                        new_active.add((x, y, z, w))
    return new_active

part1 = active.copy()
part2 = active.copy()
for i in range(1, 7):
    part1 = iterate(part1, range(1), i)
    part2 = iterate(part2, range(-i, i + 1), i)
print(len(part1))
print(len(part2))