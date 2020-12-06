#!/usr/bin/python3
# Day 3, Part 2 of Advent of Code 2020

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

def checkslope(rowstep=int, columnstep=int):
    slope = columnstep # slope is defined as N columns rightward to move for each downward step 
    trees = 0 
    p = Problem('input.txt')
    column = 0
    numrows = len(p.rows)
    for row in range(0, numrows, rowstep):
        r = Row(p.rows[row])
        if r.terrain[(column)]:
            # print("Hit a tree at column {} of {}".format(column, r.width))
            trees += 1
        else:
            pass
        # print(row)
        # print("Column: {} // Width: {} // Trees: {}".format(column, r.width, trees))
        column = (column + slope) % (r.width)
    return trees
    
def main():
    product = 1
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    for slope in slopes:
        rows, columns = slope[:]
        trees = checkslope(rows, columns)
        print("Found {} trees going downhill with slope {}:{}.".format(trees, columns, rows))
        product *= trees 
        print("Product: {}".format(product))
    return

if __name__ == "__main__":
    main()