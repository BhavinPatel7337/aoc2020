from sys import path

with open(path[0] + '/input.txt') as f:
    program = [(x[:3], int(x[4:])) for x in f]

def run(program):
    acc = 0
    pc = 0
    executed = set()
    while pc not in executed and pc < len(program):
        executed.add(pc)
        if program[pc][0] == 'acc':
            acc += program[pc][1]
        if program[pc][0] == 'jmp':
            pc += program[pc][1]
        else:
            pc += 1
    return acc, pc

print(run(program)[0])

for n, i in enumerate(program):
    if i[0] == 'jmp' or i[0] == 'nop':
        new_program = program.copy()
        new_program[n] = (i[0].translate(str.maketrans('jmno', 'nojm')), i[1])
        result = run(new_program)
        if (result[1]) == len(program):
            print(result[0])