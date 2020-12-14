from sys import path
import re

with open(path[0] + '/input.txt') as f:
    program = [re.match(r'(mask|mem\[(\d+)\]) = ([\dX]+)', x).groups() for x in f]

def apply_mask(x, mask, unchanged):
    return ''.join([i if mask[n] == unchanged else mask[n] for n, i in enumerate(x)])

def get_combinations(floating):
    if len(floating) > 1:
        results = floating[0:1]
        for i in get_combinations(floating[1:]):
            results += [i, floating[0] + i]
        return results
    else:
        return floating

def run(program, version):
    mask = ''
    mem = {}
    for command in program:
        if command[0] == 'mask':
            mask = command[2]
        else:
            if version == 1:
                x = '{0:036b}'.format(int(command[2]))
                x = int(apply_mask(x, mask, 'X'), 2)
                mem[command[1]] = x
            elif version == 2:
                x = '{0:036b}'.format(int(command[1]))
                x = apply_mask(x, mask, '0')
                floating = [2 ** (35 - i) for i, c in enumerate(x) if c == 'X']
                x = int(x.replace('X', '0'), 2)
                addresses = [x] + [x + i for i in get_combinations(floating)]
                for a in addresses:
                    mem[a] = int(command[2])
    return sum([x for x in mem.values()])

print(run(program, 1))
print(run(program, 2))