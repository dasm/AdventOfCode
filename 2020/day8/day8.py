#!/usr/bin/env python3

with open("input") as file_:
    opcodes = file_.readlines()

def part1():
    acc = 0

    index = 0
    list_of_indexes = []

    while index < len(opcodes):
        if index in list_of_indexes:
            print('acc', acc)
            print(list_of_indexes)
            break
        list_of_indexes.append(index)

        opcode = opcodes[index]
        code, step = opcode.split()

        order = -1 if step.startswith('-') else 1
        step = int(step[1:])
        value = order * step

        if code == 'nop':
            pass
        if code == 'acc':
            acc += value
        if code == 'jmp':
            index += value
            continue

        index += 1

opcodes = ["nop +0",
"acc +1",
"jmp +4",
"acc +3",
"jmp -3",
"acc -99",
"acc +1",
"jmp -4",
"acc +6",
]


def _part2():
    acc = 0

    index = 0
    list_of_indexes = []

    while index < len(opcodes):
        if index in list_of_indexes:
            print('broke', acc)
            break
        list_of_indexes.append(index)

        opcode = opcodes[index]
        code, step = opcode.split()

        order = -1 if step.startswith('-') else 1
        step = int(step[1:])
        value = order * step

        if code == 'nop':
            pass
        if code == 'acc':
            acc += value
        if code == 'jmp':
            index += value
            continue

        index += 1
    print("finished", acc)

part1()
