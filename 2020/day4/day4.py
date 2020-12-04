#!/usr/bin/env python3
import re


def hgt(value):
    validate = {
        'cm': lambda x: 150<=int(x)<=193,
        'in': lambda x: 59<=int(x)<=76,
    }

    found = re.match('^(\d{2}in)|(\d{3}cm)', value)
    if not found:
        return False

    value, units = value[:-2], value[-2:]
    return validate[units](value)

simple = {
    'byr': lambda x: int(x),
    'iyr': lambda x: int(x),
    'eyr': lambda x: int(x),
    'hgt': True,
    'hcl': True,
    'ecl': True,
    'pid': True,
}

detailed = {
    'byr': lambda x: 1920<=int(x)<=2002,
    'iyr': lambda x: 2010<=int(x)<=2020,
    'eyr': lambda x: 2020<=int(x)<=2030,
    'hgt': hgt,
    'hcl': lambda x: bool(re.match("#[0-9a-f]{6}", x)),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: bool(re.match("^\d{9}$", x)),
}

required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

with open("input") as file_:
    output = file_.read()
    lines = output.split("\n\n")
    lines = [line.replace("\n", " ").split() for line in lines]

simple_passports = []
detailed_passports = []
for line in lines:
    simple_passport = {}
    detailed_passport = {}

    for element in line:
        key, value = element.split(":")
        s = simple.get(key)
        if s:
            simple_passport[key] = value

        d = detailed.get(key)
        if d and d(value):
            detailed_passport[key] = value


    if set(required) <= set(simple_passport.keys()):
        simple_passports.append(simple_passport)
    if set(required) <= set(detailed_passport.keys()):
        detailed_passports.append(detailed_passport)

print(len(simple_passports), len(detailed_passports))
