from sys import path
import re

with open(path[0] + '/input.txt') as f:
    x = f.read()
    rules = dict(re.findall(r'(\d+): ([\d\w \|"]+)', x))
    messages =  re.findall(r'^(\w+)$', x, re.M)

def get_rule(i):
    if rules[i].startswith('"'):
        return rules[i][1:-1]
    else:
        rules[i] = '"(' + re.sub(r'\d+', lambda x: get_rule(x.group()), rules[i]).replace(' ', '') + ')"'
        return rules[i][1:-1]

r = get_rule('0')
print(sum(bool(re.fullmatch(r, m)) for m in messages))

rules['0'] = '8 11'
rules['8'] = rules['8'][:-1] + '+"'
rules['11'] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31'
r = get_rule('0')
print(sum(bool(re.fullmatch(r, m)) for m in messages))