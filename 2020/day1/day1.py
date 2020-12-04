#!/usr/bin/env python3

with open('input') as file_:
    results = file_.readlines()

results = sorted(map(int, results))

def sum_two():
    i = 0
    j = len(results) - 1
    while i <= j:
        suma = results[i] + results[j]
        if suma == 2020:
            print(results[i], results[j], results[i]*results[j])
            break
        elif suma > 2020:
            j -= 1
        elif suma < 2020:
            i += 1
        else:
            print('uknown')

def sum_three():
    max_i = len(results) - 1

    for i in range(max_i - 1):
        left = i + 1
        right = max_i
        while left < right:
            suma = results[i] + results[left] + results[right]

            if suma == 2020:
                print(results[i], results[left], results[right], results[i]*results[left]*results[right])
                break
            elif suma > 2020:
                right -= 1
            else:
                left += 1
sum_two()
sum_three()
