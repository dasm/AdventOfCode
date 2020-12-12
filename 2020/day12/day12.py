#!/usr/bin/env python3
import sys

def load_data(filename):
    with open(filename) as file_:
        return file_.readlines()

DIRECTIONS = {
    "N": lambda x, y, value: (x+value, y),
    "S": lambda x, y, value: (x-value, y),
    "E": lambda x, y, value: (x, y+value),
    "W": lambda x, y, value: (x, y-value),
}

class Ship:
    def __init__(self):
        self.direction = 'E'
        self.x = 0
        self.y = 0
        self.waypoint_x = 1
        self.waypoint_y = 10

    def action(self, value):
        direction, value = value[0], int(value[1:])
        if direction == "F":
            func = DIRECTIONS[self.direction]
            self.x, self.y = func(self.x, self.y, value)

        elif direction in ("L", "R"):
            ORDER = {
                "L": ["N", "W", "S", "E"],
                "R": ["S", "W", "N", "E"],
            }
            order = ORDER[direction]
            index = order.index(self.direction)

            value = int(((value/90) + index) % len(order))
            self.direction = order[value]

        elif direction in ("N", "S", "E", "W"):
            func = DIRECTIONS[direction]
            self.x, self.y = func(self.x, self.y, value)

    def distance(self):
        return abs(self.x) + abs(self.y)

class Ship2(Ship):
    def action(self, value):
        direction, value = value[0], int(value[1:])

        if direction == "F":
            self.x = self.x + value*self.waypoint_x
            self.y = self.y + value*self.waypoint_y
        elif direction in ("L", "R"):
            ORDER = {
                "L": lambda x, y: (y, -x),
                "R": lambda x, y: (-y, x)
            }
            func = ORDER[direction]
            value = int(value/90) % 360
            for _ in range(value):
                self.waypoint_x, self.waypoint_y = func(self.waypoint_x, self.waypoint_y)

        elif direction in ("N", "S", "E", "W"):
            func = DIRECTIONS[direction]
            self.waypoint_x, self.waypoint_y = func(self.waypoint_x, self.waypoint_y, value)


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    ship = Ship()
    for d in data:
        ship.action(d)
    print("part1", ship.distance())

    ship = Ship2()
    for d in data:
        ship.action(d)
    print("part2", ship.distance())
