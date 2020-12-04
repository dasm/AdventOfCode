#!/usr/bin/env python3

with open("input") as file_:
    dimensions = file_.readlines()

def one():
    result = 0
    ribbon = 0
    for dimension in dimensions:
        length, width, height = sorted(map(int, dimension.strip().split("x")))

        lw = 2*length*width
        wh = 2*width*height
        hl = 2*height*length

        result += (lw+wh+hl + min(lw, wh, hl)/2)
        ribbon += (length+length+width+width + length*width*height)

    print(result)
    print(ribbon)

one()
