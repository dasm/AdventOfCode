#!/usr/bin/env python3

directions = {
    "F": lambda x, y: (x, int(x+(y-x)/2)),
    "B": lambda x, y: (int(x+(y-x)/2), y),
    "L": lambda x, y: (x, int(x+(y-x)/2)),
    "R": lambda x, y: (int(x+(y-x)/2), y),
}

def get_pos(boarding_pass, end):
    start = 0
    for letter in boarding_pass:
        f = directions[letter]
        start, end = f(start, end)
    return list(range(128))[start:end][0]

def main(boarding_pass):
    column = get_pos(boarding_pass[:-3], 128)
    row = get_pos(boarding_pass[-3:], 8)
    pass_id = column * 8 + row
    return column, row, pass_id

with open("input") as file_:
    seats = {}
    pass_ids = []
    for line in file_.readlines():
        column, row, pass_id = main(line.strip())
        curr_column = seats.get(column)
        if not curr_column:
            seats[column] = [row]
        else:
            seats[column].append(row)
        pass_ids.append(pass_id)

print(max(pass_ids))
for column, row in sorted(seats.items()):
    if len(row) < 8:
        print(column, row)

col = 72
row = 3
pass_id = 72*8 + 3
print(pass_ids.index(pass_id-1))
print(pass_ids.index(pass_id+1))
print(pass_id)
