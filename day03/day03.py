from sys import path

with open(path[0] + '/input.txt') as f:
    grid = [x for x in f]

def trees(grid, dx, dy):
    return sum(y[x % (len(grid[0]) - 1)] == '#' for y, x in zip(grid[::dy], list(range(0, dx * len(grid), dx))))

print(trees(grid, 3, 1))
print(trees(grid, 1, 1) * trees(grid, 3, 1) * trees(grid, 5, 1) * trees(grid, 7, 1) * trees(grid, 1, 2))