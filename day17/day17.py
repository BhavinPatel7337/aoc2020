from sys import path

grid, adjacent = {}, {}
directions = [(x, y, z, w) for x in range(-1, 2)
                for y in range(-1, 2)
                for z in range(-1, 2)
                for w in range(-1, 2)
                if any([x != 0, y != 0, z != 0, w != 0])]

with open(path[0] + '/input.txt') as f:
    for y, row in enumerate(f):
        for x, state in enumerate(row.strip()):
            grid[x, y, 0, 0] = state
            adjacent[x, y, 0, 0] = [(x + dx, y + dy, dz, dw) for dx, dy, dz, dw in directions]
max_x, max_y, max_z = x, y, 0

def iterate(grid):
    global max_x, max_y, max_z
    max_x += 1
    max_y += 1
    max_z += 1
    new_grid = {}
    for w in range(-max_z, max_z + 1):
        for z in range(-max_z, max_z + 1):
            for y in range(-max_z, max_y + max_z + 1):
                for x in range(-max_z, max_x + max_z + 1):
                    if (x, y, z, w) not in grid:
                        adjacent[x, y, z, w] = [(x + dx, y + dy, z + dz, w + dw) for dx, dy, dz, dw in directions]
                    cube = grid.get((x, y, z, w), '.')
                    if cube == '#' and sum(grid.get(i) == '#' for i in adjacent[x, y, z, w]) not in [2, 3]:
                        new_grid[x, y, z, w] = '.'
                    elif cube == '.' and sum(grid.get(i) == '#' for i in adjacent[x, y, z, w]) == 3:
                        new_grid[x, y, z, w] = '#'
                    else:
                        new_grid[x, y, z, w] = cube
    return new_grid

for i in range(6):
    grid = iterate(grid)
print(sum(i == '#' for i in grid.values()))