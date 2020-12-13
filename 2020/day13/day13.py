#!/usr/bin/env python3
import sys

def load_data(filename):
    with open(filename) as file_:
        time, bus_ids = file_.readlines()
    time = int(time)
    bus_ids = [int(x) for x in bus_ids.split(',') if x != 'x']
    return time, bus_ids

def minutes_until(time, bus_id):
    return bus_id, (bus_id-time%bus_id)

def part1(current_time, bus_ids):
    results = []
    for bus_id in bus_ids:
        bus_id, time_left = minutes_until(current_time, bus_id)
        results.append((time_left, bus_id))
    results = sorted(results, key=lambda x: x[0])
    result = results[0][0] * results[0][1]
    return result


if __name__ == '__main__':
    filename = sys.argv[1]
    time, bus_ids = load_data(filename)
    result = part1(time, bus_ids)
    print('part1', result)
