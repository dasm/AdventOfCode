#!/usr/bin/env python3
from collections import defaultdict

def part1(data, year):
    mem = defaultdict(list)
    for idx, d in enumerate(data):
        mem[d].append(idx)

    value = 0
    idx += 1
    mem[value].append(idx)
    idx += 1

    while idx < year+1:
        if idx == year:
            return value
        values = mem.get(value, [0, 0])
        try:
            value = values[-1] - values[-2]
        except IndexError:
            value = 0
        mem[value].append(idx)
        idx += 1


if __name__ == '__main__':
    #sample = [0,3,6]
    #print('part1', part1(sample, 2020))
    #sample = [1,3,2]
    #print('part1', part1(sample, 2020))
    #sample = [2,1,3]
    #print('part1', part1(sample, 2020))
    #sample = [1,2,3]
    #print('part1', part1(sample, 2020))
    #sample = [2,3,1]
    #print('part1', part1(sample, 2020))
    #sample = [3,2,1]
    #print('part1', part1(sample, 2020))
    #sample = [3,1,2]
    #print('part1', part1(sample, 2020))
    input_ = [0,14,6,20,1,4]
    print('part1', part1(input_, 2020))
    #sample = [0,3,6]
    #print('part2', part1(sample, 30000000))
    #sample = [1,3,2]
    #print('part2', part1(sample, 30000000))
    #sample = [2,1,3]
    #print('part2', part1(sample, 30000000))
    #sample = [1,2,3]
    #print('part2', part1(sample, 30000000))
    #sample = [2,3,1]
    #print('part2', part1(sample, 30000000))
    #sample = [3,2,1]
    #print('part2', part1(sample, 30000000))
    #sample = [3,1,2]
    #print('part2', part1(sample, 30000000))
    input_ = [0,14,6,20,1,4]
    print('part2', part1(input_, 30000000))
