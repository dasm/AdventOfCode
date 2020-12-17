#!/usr/bin/env python3
from collections import defaultdict
import sys

def load_data(filename):
    with open(filename) as file_:
        directions = file_.read().strip()
    return directions

DIRECTIONS = {
    "v": lambda x, y: (x, y+1),
    ">": lambda x, y: (x+1, y),
    "<": lambda x, y: (x-1, y),
    "^": lambda x, y: (x, y-1),
}

def part1(data):
    houses = defaultdict(list)
    x = y = 0
    houses[(x, y)].append(0)
    for index, direction in enumerate(data):
        func = DIRECTIONS[direction]
        x, y = func(x, y)
        houses[(x, y)].append(index)
    return len(houses)

def part2(data):
    houses = defaultdict(list)
    sx = sy = rx = ry = 0
    houses[(0, 0)].append(0)
    for index, direction in enumerate(data):
        func = DIRECTIONS[direction]
        if index%2 == 0:
            sx, sy = func(sx, sy)
            houses[(sx, sy)].append(index)
        else:
            rx, ry = func(rx, ry)
            houses[(rx, ry)].append(index)
    return len(houses)

if __name__ == '__main__':
    filename = sys.argv[1]
    data = load_data(filename)
    print('part1', part1(data))
    print('part2', part2(data))
