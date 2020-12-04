#!/usr/bin/env python3

with open('input') as file_:
    brackets = file_.read().strip()

basement = False
floor = 0
for index, letter in enumerate(brackets):
    if not basement and floor < 0:
        basement = True
        print("basement", index)
    if letter == '(':
        floor += 1
    elif letter == ")":
        floor -= 1
    else:
        print("Undefined")

print(floor)
