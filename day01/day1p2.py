#!/usr/bin/python3
# Day 1, Part 2 of Advent of Code 2020
import time

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
    while (2 * frontways[0]) + backways[0] > goal:
        backways.remove(backways[0])
        frontways.remove(frontways[-1])
    for firstnumber in frontways:
        for secondnumber in frontways:
            for thirdnumber in backways: 
                if firstnumber + secondnumber + thirdnumber == goal:
                    print("Found {}, {}, and {} which sum to {}.".format(firstnumber, secondnumber, thirdnumber, goal))
                    print("Product is {}.".format(firstnumber * secondnumber * thirdnumber))
                    return
    return

if __name__ == "__main__":
    total = 0
    for _ in range(1000):
        tic = time.perf_counter()
        main()
        toc = time.perf_counter()
        elapsed = toc - tic 
        total += elapsed
    print("Main() executed in an average of {:.6f} seconds".format(total/1000))