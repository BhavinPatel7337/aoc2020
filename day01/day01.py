from sys import path

with open(path[0] + '/input.txt') as f:
    expenses = [int(x) for x in f]

for i in expenses:
    if 2020 - i in expenses:
        print(i * (2020 - i))
        break

for i in expenses:
    for j in expenses:
        if 2020 - i - j in expenses:
            print(i *  j * (2020 - i - j))
            exit()