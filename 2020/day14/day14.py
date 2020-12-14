#!/usr/bin/env python3
from collections import defaultdict
import re
import sys

def load_data(filename):
    with open(filename) as file_:
        data = file_.read()
        data = data.split('mask = ')
    masks = {}
    for d in data:
        if not d:
            continue
        mapping = []
        mask, memory = d[:36], d[36:]
        for address, value in re.findall("mem\[(\d+)\] = (\d+)", memory):
            mapping.append((int(address), int(value)))
        masks[mask] = mapping
    print(masks)
    return masks

def bitfield(value):
    return format(value, 'b').zfill(36)

def apply_mask(mask, value):
    values = zip(mask[::-1], bitfield(value)[::-1])
    return list(values)

def part1(data):
    memory = {}
    for mask, mem in data.items():
        for address, value in mem:
            values = apply_mask(mask, value)
            result = 0
            for index, (m, v) in enumerate(values):
                multiply = v if m == 'X' else m
                result += (2**index)*int(multiply)
            memory[address] = result
    return sum(memory.values())


if __name__ == '__main__':
    filename = sys.argv[1]
    data = load_data(filename)
    print("part1", part1(data))
