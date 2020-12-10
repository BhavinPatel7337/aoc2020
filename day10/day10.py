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
    f = lambda x: sum(differences[i:i + x] == [1] * x for i in range(len(differences)))
    n = 1
    l = []
    while f(n + 1):
        n += 1
    while n > 1:
        r = list(range(len(l) + 1, 1, -1))
        x = f(n) - sum([x * y for x,y in zip(l, r)])
        l.append(x)
        n -= 1
    return l

rl = run_lengths(differences)
tr = [tribonacci(i) for i in range(3,3 + len(rl))][::-1]
product = 1
for i in [(x ** y) for x, y in zip(tr, rl)]:
    product *= i
print(product)