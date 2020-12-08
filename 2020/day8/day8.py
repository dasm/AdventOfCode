#!/usr/bin/env python3

with open("input") as file_:
    opcodes = file_.readlines()

def part1(opcodes):
    acc = 0

    index = 0
    visited = set()

    while True:
        if index in visited:
            return acc, False
        if index >= len(opcodes):
            return acc, True

        visited.add(index)

        opcode = opcodes[index]
        code, step = opcode.split()

        value = int(step)

        if code == 'nop':
            index += 1
        if code == 'acc':
            acc += value
            index += 1
        if code == 'jmp':
            index += value

    return acc, True

print(part1(opcodes)[0])

def swap(opcodes, index):
    if 'nop' in opcodes[index]:
        opcodes[index] = opcodes[index].replace('nop', 'jmp')
    elif 'jmp' in opcodes[index]:
        opcodes[index] = opcodes[index].replace('jmp', 'nop')
    else:
        opcodes = []
    return opcodes

def compute(opcodes):
    for index in range(len(opcodes)):
        new_opcodes = swap(opcodes[:], index)
        if not new_opcodes:
            continue
        result, ended = part1(new_opcodes)
        if ended:
            return result

    return "Oh no"

print(compute(opcodes))
