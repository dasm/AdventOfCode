#!/usr/bin/env python3
import sys

def load_data(filename):
    with open(filename) as file_:
        return file_.readlines()

OP = {"*": lambda x, y: x*y, "+": lambda x, y: x+y}
def reverse_polish_notation(line):
    queue = []
    stack = []

    line = line.replace("(", "( ").replace(")", " )").split()

    for el in line:
        if el not in ("*", "+", ")", "("):
            queue.append(int(el))
        elif el == '(':
            stack.append(el)
        elif el == ')':
            while stack and stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != "(":
                queue.append(stack.pop())
            stack.append(el)
    while stack:
        queue.append(stack.pop())
    return queue

def compute(rpn):
    index = 0
    while rpn:
        try:
            key = rpn[index+1]
        except:
            return rpn[0]
        if key in ("*", "+"):
            a, b = rpn[index-1], rpn[index]
            func = OP[key]
            result = func(a, b)
            rpn[index-1] = result
            rpn.pop(index+1)
            rpn.pop(index)
            index = 0
        index += 1

def part1(data):
    results = []
    for line in data:
        rpn = reverse_polish_notation(line)
        result = compute(rpn)
        results.append(result)
    return sum(results)

COMP = {"+":2, "*":1}
def mod_reverse_polish_notation(line):
    queue = []
    stack = []

    line = line.replace("(", "( ").replace(")", " )").split()

    for el in line:
        if el not in ("*", "+", ")", "("):
            queue.append(int(el))
        elif el == '(':
            stack.append(el)
        elif el == ')':
            while stack and stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != "(":
                tmp = stack[-1]
                if COMP[tmp] < COMP[el]:
                    break
                tmp = stack.pop()
                queue.append(tmp)
            stack.append(el)
    while stack:
        queue.append(stack.pop())
    return queue

def part2(data):
    results = []
    for line in data:
        rpn = mod_reverse_polish_notation(line)
        result = compute(rpn)
        results.append(result)
    return sum(results)


if __name__ == '__main__':
    filename = sys.argv[1]
    data = load_data(filename)
    print("part1", part1(data))
    print("part2", part2(data))
