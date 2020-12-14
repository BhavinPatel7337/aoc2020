from sys import path

with open(path[0] + '/input.txt') as f:
    earliest = int(f.readline())
    schedule = [int(x) if x != 'x' else x for x in f.readline().split(',')]

arrivals = [(earliest // x + 1) * x - earliest if x != 'x' else earliest for x in schedule]
part1 = arrivals.index(min(arrivals))
print(arrivals[part1] * int(schedule[part1]))

product = 1
for x in schedule:
    if x != 'x':
        product *= x

def solve(p, divisor):
    # Solve for x where p * x = 1 mod divisor
    d = 1
    p -= p // divisor * divisor
    while d % p != 0:
        d += divisor
    return d // p

part2 = 0
for i, divisor in enumerate(schedule):
    if divisor != 'x':
        dividend = divisor - i
        if dividend != divisor:
            p = product // divisor
            part2 += p * solve(p, divisor) * dividend

print(part2 % product)