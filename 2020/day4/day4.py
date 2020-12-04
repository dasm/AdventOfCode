#!/usr/bin/env python3

import re

with open("input") as file_:
    lines = file_.read()


def hgt(value):
    value, height = value[:-2], value[-2:]
    if not value:
        return False

    value = int(value)
    h = {
        "in": lambda x: 59<=x<=76,
        "cm": lambda x: 150<=x<=193,
    }
    val = h.get(height, False)
    if val:
        return val(value)
    return False


validation = dict(
    byr=lambda x: 1920<=int(x)<=2002,
    iyr=lambda x: 2010<=int(x)<=2020,
    eyr=lambda x: 2020<=int(x)<=2030,
    hgt=hgt,
    hcl=lambda x: bool(re.match("#[0-9a-f]{6}", x)),
    ecl=lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    pid=lambda x: bool(re.match("[0-9]{9}", x)),
    cid=lambda x: False,
)


def one():
    passports = []
    valid = 0
    for index, line in enumerate(lines.split("\n\n")):
        line = line.replace("\n", " ").split()

        if len(line) < 7:
            continue

        passport_dict = {}
        valid_fields = 0
        for data in line:
            field, value = data.split(":")
            func = validation.get(field)
            if func(value):
                valid_fields += 1
                passport_dict[field] = value
            else:
                print(index, valid_fields)
                break

        if valid_fields == 7:
            passports.append(passport_dict)
            valid += 1

    print("No more than 259")
    print(len(passports))

one()
