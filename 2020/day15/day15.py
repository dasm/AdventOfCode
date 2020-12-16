#!/usr/bin/env python3
def part1(data, year):
    mem = {d: idx for idx, d in enumerate(data)}
    spoken = 0; idx = len(data)
    while idx < year:
        new_spoken = 0
        if spoken in mem:
            new_spoken = idx - mem.get(spoken)
        mem[spoken] = idx
        spoken = new_spoken
        idx += 1
    return {v: k for k, v in mem.items()}[year-1]

if __name__ == '__main__':
    input_ = [0,14,6,20,1,4]
    answer = part1(input_, 2020)
    print('part1', answer)

    answer = part1(input_, 30000000)
    print('part2', answer)
