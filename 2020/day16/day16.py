#!/usr/bin/env python3
from collections import defaultdict
import copy
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

def retrieve_order(indexes_dict):
    sorted_dict = {}
    while indexes_dict:
        for index, titles in indexes_dict.items():
            if len(titles) == 1:
                title = titles[0]
                sorted_dict[title] = index
                break
        _ = indexes_dict.pop(index)
        copy_indexes = copy.deepcopy(indexes_dict)
        for index, titles in copy_indexes.items():
            if title in titles:
                titles.remove(title)
                indexes_dict[index] = titles
    return sorted_dict


def part2(tickets, titles_dict, ticket):
    locations = []
    tickets = list(zip(*tickets))
    locations = defaultdict(list)
    indexes = defaultdict(list)
    for title, config in titles_dict.items():
        first, second = config
        start1, end1 = first
        start2, end2 = second

        for index, values in enumerate(tickets):
            if all([bool(start1<=v<=end1 or start2<=v<=end2) for v in values]):
                indexes[index].append(title)

    answer = []
    results = retrieve_order(indexes)
    for title, index in results.items():
        if title.startswith("departure"):
            answer.append(ticket[index])

    result = 1
    for el in answer:
        result *= el
    return result

if __name__ == '__main__':
    filename = sys.argv[1]
    data = load_data(filename)
    answer = part1(data)
    print('part1', answer)
    _, tickets = check_values(data['configs'], data['nearby'])
    tickets.append(data['ticket'])
    _ = data.pop('configs')
    _ = data.pop('nearby')
    ticket = data.pop('ticket')
    answer = part2(tickets, data, ticket)
    print('part2', answer)
