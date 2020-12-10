from sys import path

with open(path[0] + '/input.txt') as f:
    adapters = [int(x) for x in f]

adapters.sort()
differences = [adapters[0]] + [i - adapters[n - 1] for n, i in enumerate(adapters) if n != 0] + [3]
print(differences.count(1) * differences.count(3))

def tribonacci(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

def run_lengths(differences):
    i, n, d = 0, 0, {}
    while i < len(differences):
        if differences[i] == 1:
            n += 1
            if n not in d:
                d[n] = 0
        else:
            if n > 1:
                d[n] += 1
            n = 0
        i += 1
    return [d[n] for n in sorted(d)][1:]

rl = run_lengths(differences)
tr = [tribonacci(i) for i in range(3,3 + len(rl))]
product = 1
for i in [(x ** y) for x, y in zip(tr, rl)]:
    product *= i
print(product)