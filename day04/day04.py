from sys import path
import re

with open(path[0] + '/input.txt') as f:
    batch = re.split('\n\n', f.read())

valid = {
    'byr': r'^(19[2-9]\d|200[0-2])$',
    'iyr': r'^20(1\d|20)$',
    'eyr': r'^20(2\d|30)$',
    'hgt': r'^(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$',
    'hcl': r'^#[a-f\d]{6}$',
    'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid': r'^\d{9}$'
}

c, v = 0, 0
for i in batch:
    fields = ['byr', 'iyr', 'pid', 'eyr', 'hcl', 'ecl', 'hgt']
    passport = dict(re.findall(r'(byr|iyr|pid|cid|eyr|hcl|ecl|hgt):([^\s]+)(?:\s|$)', i))
    c += all(k in passport for k in fields)
    v += all(re.match(valid[k], passport.get(k, '')) for k in fields)

print(c)
print(v)