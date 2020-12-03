#!/usr/bin/python3
# Day 3, Part 1 of Advent of Code 2020

import math
import timeit

# Input class
class Problem():
    def __init__(self, filename):
        rows = []
        with open(filename, "r") as file:
            for line in file:
                rows.append(line.rstrip())
        self.rows = rows
        return

class Row():
    def __init__(self, row=list):
        self.row = row
        self.width = len(self.row)
        terrain = []
        for index, item in enumerate(self.row):
            terrain[index] = self.istree(item)
        self.terrain = terrain 
        return

    def istree(self, character=chr):
        if character == ".":
            return False
        elif character == "#":
            return True
        else:
            print("Found a \"{}\" parsing the row".format(character))
            return False
        return


def main():
    slope = 3 # slope is defined as N columns rightward to move for each downward step 
    trees = 0 
    p = Problem('input.txt')
    column = 1
    for row in p.rows:
        r = Row(row)
        if r.terrain[column]:
            trees += 1
        else:
            pass
        column = (column + slope) % (r.width)
    print("Found {} trees going downhill.".format(trees))
    return

if __name__ == "__main__":
    main()