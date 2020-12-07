#!/usr/bin/env python3
import re
from collections import defaultdict

with open('input') as file_:
    rules = file_.readlines()

def parse_rules():
    to_contain = defaultdict(list)
    from_contain = defaultdict(list)
    for rule in rules:
        parent_bag, rest = rule.split(' bags contain ')
        for num_bags, child_bag in re.findall(r"(\d+) (.+?) bag", rest):
            to_contain[child_bag].append(parent_bag)
            from_contain[parent_bag].append((child_bag, int(num_bags)))
    return from_contain, to_contain

def find_a_bag(bags_dict):
    discovered = ["shiny gold"]
    visited = set()

    while discovered:
        bag = discovered.pop(0)
        discovered.extend(bags_dict[bag])
        visited.add(bag)
    return len(visited) - 1

def find_num_bags(bags_dict):
    discovered = [('shiny gold', 1)]
    total_bags = 0

    while discovered:
        bag, amount = discovered.pop(0)
        discovered.extend([(x, amount*x_amt) for x, x_amt in bags_dict[bag]])
        total_bags += amount
    return total_bags - 1

from_contain, to_contain = parse_rules()
print(find_a_bag(to_contain))
print(find_num_bags(from_contain))
