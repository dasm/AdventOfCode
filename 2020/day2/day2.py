#!/usr/bin/env python3


def parse1(line):
    number, letter, password = line.split()
    start, end = number.split('-')
    letter = letter.rstrip(":")
    number_of_letters = password.count(letter)
    if int(start) <= number_of_letters <= int(end):
        return 1
    else:
        return 0

def parse(line):
    number, letter, password = line.split()
    start, end = number.split('-')
    start = int(start) - 1
    end = int(end) - 1
    letter = letter.rstrip(":")

    if ((password[start] == letter and password[end] != letter) or
            (password[end] == letter and password[start] != letter)):
        return 1
    else:
        return 0


answer = 0
with open('input') as file_:
    for line in file_.readlines():
        answer += parse(line)

print(answer)
