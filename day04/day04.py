from sys import path
import re

with open(path[0] + '/input.txt') as f:
    passports = [dict(re.findall(r'(byr|iyr|pid|cid|eyr|hcl|ecl|hgt):([^\s]+)(?:\s|$)', i)) for i in re.split('\n\n', f.read())]

valid = {
    'byr': r'^(19[2-9]\d|200[0-2])$',
    'iyr': r'^20(1\d|20)$',
    'eyr': r'^20(2\d|30)$',
    'hgt': r'^(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$',
    'hcl': r'^#[a-f\d]{6}$',
    'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid': r'^\d{9}$'
}

print(sum(all(k in p for k in valid.keys()) for p in passports))
print(sum(all(re.match(valid[k], p.get(k, '')) for k in valid.keys()) for p in passports))