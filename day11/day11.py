from sys import path

with open(path[0] + '/input.txt') as f:
    grid = [line.strip() for line in f]

max_x, max_y = len(grid[0]) - 1, len(grid) - 1

def print_grid(grid):
    for y in grid:
        print(''.join(y))
    input('\n')

def list_adjacent(grid, x, y, max_x, max_y):
    lst = []
    if x != 0:
        lst.append(grid[y][x - 1])
    if x != max_x:
        lst.append(grid[y][x + 1])
    if y != 0:
        lst.append(grid[y - 1][x])
    if y != max_y:
        lst.append(grid[y + 1][x])
    if x != 0 and y != 0:
        lst.append(grid[y - 1][x - 1])
    if x != 0 and y != max_y:
        lst.append(grid[y + 1][x - 1])
    if x != max_x and y != 0:
        lst.append(grid[y - 1][x + 1])
    if x != max_x and y != max_y:
        lst.append(grid[y + 1][x + 1])
    return lst

def check_visible(grid, x, y, max_x, max_y):
    occupied = 0
    i = x
    while i > 0:
        if grid[y][i - 1] != '.':
            occupied += grid[y][i - 1] == '#'
            break
        i -= 1
    
    j = y
    while j > 0:
        if grid[j - 1][x] != '.':
            occupied += grid[j - 1][x] == '#'
            break
        j -= 1
    
    i = x
    while i < max_x:
        if grid[y][i + 1] != '.':
            occupied += grid[y][i + 1] == '#'
            break
        i += 1
    
    j = y
    while j < max_y:
        if grid[j + 1][x] != '.':
            occupied += grid[j + 1][x] == '#'
            break
        j += 1
    
    i = x
    j = y
    while i > 0 and j > 0:
        if grid[j - 1][i - 1] != '.':
            occupied += grid[j - 1][i - 1] == '#'
            break
        i -= 1
        j -= 1
    
    i = x
    j = y
    while i < max_x and j > 0:
        if grid[j - 1][i + 1] != '.':
            occupied += grid[j - 1][i + 1] == '#'
            break
        i += 1
        j -= 1
    
    i = x
    j = y
    while i > 0 and j < max_y:
        if grid[j + 1][i - 1] != '.':
            occupied += grid[j + 1][i - 1] == '#'
            break
        i -= 1
        j += 1
    
    i = x
    j = y
    while i < max_x and j < max_y:
        if grid[j + 1][i + 1] != '.':
            occupied += grid[j + 1][i + 1] == '#'
            break
        i += 1
        j += 1

    return occupied

def check_adjacent(grid, x, y, max_x, max_y):
    return sum(i == '#' for i in list_adjacent(grid, x, y, max_x, max_y))

def iterate(grid):
    new_grid = []
    for y in range(max_y + 1):
        new_grid.append([])
        for x in range(max_x + 1):
            if grid[y][x] == 'L' and check_visible(grid, x, y, max_x, max_y) == 0:
                new_grid[y].append('#')
            elif grid[y][x] == '#' and check_visible(grid, x, y, max_x, max_y) > 4:
                new_grid[y].append('L')
            else:
                new_grid[y].append(grid[y][x])
    return new_grid

#print_grid(grid)
while grid != iterate(grid):
    grid = iterate(grid)
    #print_grid(grid)

print(sum(sum(x == '#' for x in y) for y in grid))