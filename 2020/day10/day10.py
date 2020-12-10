#!/usr/bin/env python3
import sys

def load_data(filename):
    with open(filename) as file_:
        output = file_.readlines()

    output = map(int, output)
    return sorted(output)

def count_jolts(data):
    diff_1 = 0
    diff_2 = 0
    diff_3 = 0

    value = 0
    index = 0
    while index < len(data):
        next_value = data[index]
        tmp_value = next_value - value
        if tmp_value not in [1, 2, 3]:
            print("Oh no")
            return None

        if tmp_value == 1: diff_1 += 1
        if tmp_value == 2: diff_2 += 1
        if tmp_value == 3: diff_3 += 1

        value = data[index]
        index += 1

    # extra 3 jolts at the end
    diff_3 += 1
    print(diff_1, diff_2, diff_3)
    return diff_1 * diff_3

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: day10.py <data>")

    filename = sys.argv[1]
    output = load_data(filename)
    part1 = count_jolts(output)
    print('part1', part1)
