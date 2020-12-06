#!/usr/bin/env python3

with open("input") as file_:
    lines = file_.read()

groups = lines.split("\n\n")

suma = 0
for group in groups:
    group = group.replace("\n", "")
    group = set(group)
    suma += len(group)

print(suma)

suma = 0
for group in groups:
    group = group.split()
    result = set(group[0]).intersection(*group)
    suma += len(result)

print(suma)
