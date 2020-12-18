from sys import path

with open(path[0] + '/input.txt') as f:
    homework = [x.strip() for x in f]

def tokenise(expression):
    tokenised = []
    current = ''
    i, brackets = 0, 0
    while i < len(expression):
        brackets += expression[i] == '('
        brackets -= expression[i] == ')'
        if brackets > 0 or expression[i] != ' ':
            current += expression[i]
        else:
            tokenised.append(current)
            current = ''
        i += 1
    tokenised.append(current)
    return tokenised

def evaluate(tokenised, precedence):
    if len(tokenised) == 1:
        if tokenised[0].isdigit():
            return int(tokenised[0])
        elif tokenised[0].startswith('('):
            return evaluate(tokenise(tokenised[0][1:-1]), precedence)
    value = evaluate([tokenised[0]], precedence)
    operation = ''
    new_tokenised = []
    while tokenised:
        i, tokenised = tokenised[0], tokenised[1:]
        if i in '+*':
            operation = i
        else:
            if operation == '+':
                value += evaluate([i], precedence)
            elif operation == '*':
                if precedence == 'same':
                    value *= evaluate([i], precedence)
                else:
                    new_tokenised += [str(value), operation]
                    value = evaluate([i], precedence)
    new_tokenised.append(str(value))
    return evaluate(new_tokenised, 'same')

print(sum(evaluate(tokenise(expression), 'same') for expression in homework))
print(sum(evaluate(tokenise(expression), 'add') for expression in homework))