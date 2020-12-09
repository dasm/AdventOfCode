#!/usr/bin/env python3

with open("input") as file_:
    numbers = file_.readlines()
    numbers = list(map(int, numbers))

def func(preamble):
    index = preamble
    while index < len(numbers):
        next_value = numbers[index]

        sorted_numbers = numbers[index-preamble:index]
        sorted_numbers = sorted(sorted_numbers)

        start, end = 0, preamble-1
        while start < end:
            value = sorted_numbers[start] + sorted_numbers[end]
            if value == next_value:
                break
            elif value < next_value:
                start += 1
            elif value > next_value:
                end -= 1
        else:
            return next_value
        index += 1

answer = func(25)
print('part1', answer)

def func2(answer):
    start, end = 0, 1
    value = numbers[start] + numbers[end]
    while start < end:
        if value == answer:
            result = numbers[start:end]
            result = sorted(result)
            return result[0] + result[-1]
        elif value > answer:
            start += 1
            value -= numbers[start-1]
        elif value < answer:
            end += 1
            value += numbers[end]
    else:
        print("Oh no")

answer = func2(answer)
print('part2', answer)
