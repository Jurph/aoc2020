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
        print("Ingested {} rows.".format(len(rows)))
        return

class Row():
    def __init__(self, row=str):
        self.row = row
        self.width = len(self.row)
        terrain = []
        for item in self.row:
            terrain.append(self.istree(item))
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

def checkslope(rows, columns):
    slope = columns # slope is defined as N columns rightward to move for each downward step 
    trees = 0 
    p = Problem('input.txt')
    column = 0
    for row in p.rows:
        r = Row(row)
        if r.terrain[(column)]:
            print("Hit a tree at column {} of {}".format(column, r.width))
            trees += 1
        else:
            pass
        print(row)
        print("Column: {} // Width: {} // Trees: {}".format(column, r.width, trees))
        column = (column + slope) % (r.width)
    return trees
    
def main():
    rows = 1
    columns = 3
    trees = checkslope(rows, columns)
    print("Found {} trees going downhill with slope {}:{}.".format(trees, columns, rows))
    return

if __name__ == "__main__":
    main()