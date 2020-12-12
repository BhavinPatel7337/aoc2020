from sys import path

grid, adjacent = {}, {}
directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
with open(path[0] + '/input.txt') as f:
    for y, row in enumerate(f):
        for x, state in enumerate(row.strip()):
            grid[x, y] = state
            if state != '.':
                adjacent[x, y] = [(x + dx, y + dy) for dx, dy in directions]

def find_visible(x, y, dx, dy):
    i, j = 1, 1
    while grid.get((x + dx * i, y + dy * j)) == '.':
        i += 1
        j += 1
    if (x + dx * i, y + dy * j) in grid:
        return x + dx * i, y + dy * j

visible = dict(((x, y), [find_visible(x, y, dx, dy) for dx, dy in directions]) for x, y in adjacent)

def iterate(grid, neighbours, tolerance):
    new_grid = {}
    for x, y in grid:
        if grid[x, y] == 'L' and sum(grid.get(i) == '#' for i in neighbours[x, y]) == 0:
            new_grid[x, y] = '#'
        elif grid[x, y] == '#' and sum(grid.get(i) == '#' for i in neighbours[x, y]) > tolerance:
            new_grid[x, y] = 'L'
        else:
            new_grid[x, y] = grid[x, y]
    return new_grid

def solve(part, grid):
    params = {1: (adjacent, 3), 2: (visible, 4)}
    while grid != (g := iterate(grid, *(params[part]))):
            grid = g
    return sum(i == '#' for i in grid.values())

print(solve(1, grid.copy()))
print(solve(2, grid.copy()))