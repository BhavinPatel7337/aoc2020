from sys import path

with open(path[0] + '/input.txt') as f:
    directions = [(x[0], int(x[1:])) for x in f]

def move(d, pos):
    switch = {
        'N': (pos[0], pos[1] + d[1]),
        'S': (pos[0], pos[1] - d[1]),
        'E': (pos[0] + d[1], pos[1]),
        'W': (pos[0] - d[1], pos[1])
    }
    return switch[d[0]]

def turn(d, pos):
    switch = {
        ('L', 90): (-pos[1], pos[0]),
        ('R', 270): (-pos[1], pos[0]),
        ('R', 90): (pos[1], -pos[0]),
        ('L', 270): (pos[1], -pos[0]),
        ('L', 180): (-pos[0], -pos[1]),
        ('R', 180): (-pos[0], -pos[1])
    }
    return switch[d]
    
p, o = (0, 0), (1, 0)
for d in directions:
    if d[0] == 'F':
        p = (p[0] + o[0] * d[1], p[1] + o[1] * d[1])
    elif d[0] in 'LR':
        o = turn(d, o)
    else:
        p = move(d, p)
print(abs(p[0]) + abs(p[1]))

sp, wp = (0, 0), (10, 1)
for d in directions:
    if d[0] == 'F':
        sp = (sp[0] + wp[0] * d[1], sp[1] + wp[1] * d[1])
    elif d[0] in 'LR':
        wp = turn(d, wp)
    else:
        wp = move(d, wp)
print(abs(sp[0]) + abs(sp[1]))