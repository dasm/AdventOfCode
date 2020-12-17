#!/usr/bin/env python3
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
    return masks

def apply_mask(mask, value):
    values = zip(mask, format(value, 'b').zfill(36))
    return list(values)

def part1(data):
    memory = {}
    for mask, mem in data.items():
        for address, value in mem:
            values = apply_mask(mask, value)
            result = ''.join([v if m=="X" else m for (m, v) in values])
            memory[address] = int(result, 2)
    return sum(memory.values())

def mutate_addresses(address):
    if not "X" in address:
        return [address]
    index = address.index("X")
    a0 = address[:index] + "0" + address[index+1:]
    a1 = address[:index] + "1" + address[index+1:]
    return mutate_addresses(a0) + mutate_addresses(a1)

def part2(data):
    memory = {}
    for mask, mem in data.items():
        for address, value in mem:
            values = apply_mask(mask, address)
            result = ''.join([m if m=="X" else str(int(m) or int(v)) for (m, v) in values])
            addresses = mutate_addresses(result)
            for address in addresses:
                memory[address] = value
    return sum(memory.values())

if __name__ == '__main__':
    filename = sys.argv[1]
    data = load_data(filename)
    print("part1", part1(data))
    print('part2', part2(data))
