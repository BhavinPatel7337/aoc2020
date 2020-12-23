puzzle_input = '589174263'
part1, prev = {}, int(puzzle_input[-1])
for i in puzzle_input:
    part1[prev] = int(i)
    prev = int(i)
part2 = part1.copy()
for i in range(10, 1000001):
    part2[prev] = i
    prev = i
part2[prev] = int(puzzle_input[0])

def move(cups, current, largest):
    p1 = cups[current]
    p2 = cups[p1]
    p3 = cups[p2]
    destination = current - 1
    while destination in [0, p1, p2, p3]:
        if destination == 0:
            destination = largest
        else:
            destination -= 1
    cups[current] = cups[p3]
    cups[p3] = cups[destination]
    cups[destination] = p1
    return cups[current]

def play(cups, moves, current, largest):
    for _ in range(moves):
        current = move(cups, current, largest)

play(part1, 100, int(puzzle_input[0]), 9)
current, answer = 1, ''
while (current := part1[current]) != 1:
    answer += str(current)
print(answer)

play(part2, 10000000, int(puzzle_input[0]), 1000000)
print(part2[1] * part2[part2[1]])