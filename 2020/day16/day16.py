#!/usr/bin/env python3
import re
import sys

def load_data(filename):
    result = {}
    with open(filename) as file_:
        data = file_.read()
        config, ticket, nearby = data.split('\n\n')
        config = config.split('\n')
        title_configs = []
        for line in config:
            title, values = line.split(':')
            values = [(int(a), int(b)) for a, b in re.findall('(\d+)\-(\d+)', values)]
            result[title] = values
            title_configs.extend(values)

        result['configs'] = title_configs

        _, values = ticket.split('\n')
        result['ticket'] = [int(v) for v in values.split(',')]
        nearby = nearby.strip().split('\n')
        result['nearby'] = [[int(v) for v in val.split(',')] for val in nearby[1:]]
    return result

def check_values(data, values):
    error_rate = []
    invalid_tickets = []
    for index, value in enumerate(values):
        for el in value:
            if not any([start<=el<=end for start, end in data]):
                error_rate.append(el)
                invalid_tickets.append(index)

    valid_tickets = [t for idx, t in enumerate(values) if idx not in invalid_tickets]
    return error_rate, valid_tickets

def part1(data):
    error_rate, _ = check_values(data['configs'], data['nearby'])
    return sum(error_rate)

if __name__ == '__main__':
    filename = sys.argv[1]
    data = load_data(filename)
    answer = part1(data)
    print('part1', answer)
    _, valid_tickets = check_values(data['configs'], data['nearby'])
