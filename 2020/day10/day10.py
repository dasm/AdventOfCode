#!/usr/bin/env python3
from collections import defaultdict
import sys


def load_data(filename):
    with open(filename) as file_:
        output = file_.readlines()

    output = map(int, output)
    output = sorted(output)
    output.insert(0, 0)
    output.append(output[-1]+3)
    return output


def part1(data):
    joltages = defaultdict(int)
    for prev, curr in zip(data, data[1:]):
        joltages[curr-prev] += 1
    return joltages[1] * joltages[3]

def part2(data):
    total = {value: 0 for value in data}
    total[0] = 1

    for a in data:
        for i in range(1, 4):
            if a-i in total:
                total[a] += total[a-i]
    return total[data[-1]]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: day10.py <data>")

    filename = sys.argv[1]
    output = load_data(filename)
    part1 = part1(output)
    print('part1', part1)
    part2 = part2(output)
    print('part2', part2)
