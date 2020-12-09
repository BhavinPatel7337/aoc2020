from sys import path

with open(path[0] + '/input.txt') as f:
    data = [int(x) for x in f]

def is_valid(lst, tgt):
    for i in lst:
        if tgt - i in lst:
            return True
    return False

def find_invalid(data, preamble):
    for n, i in enumerate(data):
        if not is_valid(data[n - preamble:n], i) and n > preamble:
            return i

invalid = find_invalid(data, 25)
print(invalid)

for n, i in enumerate(data):
    x, y = 0, 0
    while x < invalid:
        x += data[n + y]
        y += 1
    if x == invalid and y > 1:
        print(min(data[n:n + y]) + max(data[n:n + y]))