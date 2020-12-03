#!/usr/bin/env python3

with open('input') as file_:
    lines = file_.readlines()


def slope(start_x, start_y):
    columns = len(lines[0]) - 1
    rows = len(lines)

    pos_x = start_x
    pos_y = start_y

    trees = 0

    while pos_y < rows:
        element = lines[pos_y][pos_x]
        if element == '#':
            trees += 1

        pos_y += start_y
        pos_x += start_x
        pos_x %= columns

    print(trees)
    return trees

a = slope(1, 1)
b = slope(3, 1)
c = slope(5, 1)
d = slope(7, 1)
e = slope(1, 2)
print(a*b*c*d*e)
