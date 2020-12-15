starting = [20,9,11,0,1,2]
history = dict([(x, n + 1) for n, x in enumerate(starting)])
last = starting[-1]
for n in range(len(starting), 30000001):
    x = n - history.get(last, n)
    history[last] = n
    if n in [2020, 30000000]:
        print(last)
    last = x