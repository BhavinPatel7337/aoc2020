from sys import path
import re

with open(path[0] + '/input.txt') as f:
    tiles = {int(x[0]): x[1].split() for x in re.findall(r'Tile (\d+):\n(.+?)(\n\n|$)', f.read(), re.S)}

def rotate(tile):
    return [''.join(x) for x in zip(*tile[::-1])]

def flip(tile):
    return [x[::-1] for x in tile]

def trim(tile):
    return [x[1:-1] for x in tile[1:-1]]

def find_right(tid, orientation, flipped):
    right = (orientation - 1 + 2 * flipped) % 4
    for bid, binfo in borders[tid].items():
        if binfo[0] == right:
            return bid, (orientation + binfo[1] - binfo[0] + 2 + 2 * binfo[2]) % 4, binfo[2] ^ flipped
    return None

def find_below(tid, orientation, flipped):
    below = (orientation + 2) % 4
    for bid, binfo in borders[tid].items():
        if binfo[0] == below:
            return bid, (orientation + binfo[1] - binfo[0] + 2) % 4, binfo[2] ^ flipped
    return None

def find_sea_monster(image):
    sea_monster = [(0, 0), (-18, 1), (-13, 1), (-12, 1), (-7, 1), (-6, 1), (-1, 1), (0, 1), (1, 1), (-17, 2), (-14, 2), (-11, 2), (-8, 2), (-5, 2), (-2, 2)]
    occupied = set()
    for attempt in range(8):
        for j, row in enumerate(image):
            for i, pixel in enumerate(row):
                if i > 18 and i < len(row) - 1 and j < len(image) - 3 and pixel == '#':
                    if all(image[j + s[1]][i + s[0]] == '#' for s in sea_monster):
                        occupied |= set((i + s[0], j + s[1]) for s in sea_monster)
        image = rotate(image)
        if attempt == 3:
            image = flip(image)
    return occupied

rotations = {tid: [tile, rotate(tile), rotate(rotate(tile)), rotate(rotate(rotate(tile)))] for tid, tile in tiles.items()}
borders, corners = {}, []
for x, r1 in rotations.items():
    borders[x] = {}
    for i, t1 in enumerate(r1):
        for y, r2 in rotations.items():
            for j, t2 in enumerate(r2):
                if t1[0] == t2[0][::-1]:
                    borders[x][y] = (i, j, False)
                elif t1[0] == t2[0] and t1 != t2:
                    borders[x][y] = (i, j, True)
    if len(borders[x]) == 2:
        corners.append(x)

product = 1
for c in corners:
    if find_right(c, 0, 0) and find_below(c, 0, 0):
        start = (c, 0, False)
    product *= c
print(product)

current, orientation, flipped = start
row = [''] * 10
image = []
for i in range(len(tiles)):
    tile = rotations[current][orientation]
    if flipped:
        tile = flip(tile)
    row = [''.join(x) for x in zip(row, trim(tile))]
    if (right := find_right(current, orientation, flipped)):
        current, orientation, flipped = right
    else:
        if (start := find_below(*start)):
            current, orientation, flipped = start
        image += row
        row = [''] * 10

print(sum(sum(x == '#' for x in y) for y in image) - len(find_sea_monster(image)))