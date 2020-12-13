#!/usr/bin/env python3
import sys

def load_data(filename):
    with open(filename) as file_:
        time, bus_ids = file_.readlines()
    time = int(time)
    bus_ids = bus_ids.split(',')
    return time, bus_ids

def minutes_until(time, bus_id):
    return bus_id, (bus_id-time%bus_id)

def part1(current_time, bus_ids):
    bus_ids = [int(x) for x in bus_ids if x != 'x']
    results = []
    for bus_id in bus_ids:
        bus_id, time_left = minutes_until(current_time, bus_id)
        results.append((time_left, bus_id))
    results = sorted(results, key=lambda x: x[0])
    result = results[0][0] * results[0][1]
    return result

def part2(bus_ids):
    bus_ids = [(index, int(bus_id)) for index, bus_id in enumerate(bus_ids)
               if bus_id != 'x']
    index = 0
    start_time, start_value = bus_ids[0]
    while True:
        if index % 100 == 0:
            pass
            #print(start_time)
        for time, value in bus_ids[1:]:
            if (start_time+time)%value != 0:
                break
        else:
            break
        index += 1
        start_time = start_value * index

    return start_time

def part2(bus_ids):
    bus_ids = [(index, int(bus_id)) for index, bus_id in enumerate(bus_ids)
               if bus_id != 'x']
    step = 1
    n = 1
    iterations = 0
    for i, b in bus_ids:
        c = n
        while True:
            iterations += 1
            c += step
            if (c+i)%b == 0:
                n = c
                break
        step *= b
    print('iterations', iterations)
    return n

if __name__ == '__main__':
    filename = sys.argv[1]
    time, bus_ids = load_data(filename)
    result = part1(time, bus_ids)
    print('part1', result)
    result = part2(bus_ids)
    print("part2", result)
