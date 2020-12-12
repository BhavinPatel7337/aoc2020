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
        return [(x + dx * i, y + dy * j)]
    else:
        return []

visible = {}
for x, y in grid:
    if grid[x, y] != '.':
        lst = []
        for dx, dy in directions:
            lst += find_visible(x, y, dx, dy)
        visible[x, y] = lst

def iterate(grid):
    new_grid = {}
    for x, y in grid:
        if grid[x, y] == 'L' and sum(grid.get(i) == '#' for i in visible[x, y]) == 0:
            new_grid[x, y] = '#'
        elif grid[x, y] == '#' and sum(grid.get(i) == '#' for i in visible[x, y]) > 4:
            new_grid[x, y] = 'L'
        else:
            new_grid[x, y] = grid[x, y]
    return new_grid

while grid != iterate(grid):
    grid = iterate(grid)

print(sum(i == '#' for i in grid.values()))