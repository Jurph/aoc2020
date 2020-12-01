#!/usr/bin/python3
# Day 1, Part 1 of Advent of Code 2020

# Sketch in a generic class for holding the input
class Problem():
    def __init__(self, filename):
        strings = []
        integers = []
        with open(filename, "r") as file:
            for line in file:
                strings.append(line)
                integers.append(int(line))
        self.strings = strings
        self.integers = integers
        return

def main():
    goal = 2020
    p = Problem('input.txt')
    frontways = sorted(p.integers, reverse=False)
    backways = sorted(p.integers, reverse=True)
    for firstnumber in frontways:
        for secondnumber in frontways:
            for thirdnumber in backways: 
                if firstnumber + secondnumber + thirdnumber == goal:
                    print("Found {}, {}, and {} which sum to {}.".format(firstnumber, secondnumber, thirdnumber, goal))
                    print("Product is {}.".format(firstnumber * secondnumber * thirdnumber))
                    return
    return

if __name__ == "__main__":
    main()