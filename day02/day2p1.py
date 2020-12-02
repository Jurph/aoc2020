#!/usr/bin/python3
# Day 2, Part 1 of Advent of Code 2020

# Sketch in a generic class for holding the input
class Problem():
    def __init__(self, filename):
        rows = []
        with open(filename, "r") as file:
            for line in file:
                rows.append(line.rstrip())
        self.rows = rows
        return

class Entry():
    def __init__(self, row):
        elements = row.split(" ")
        self.quantity_string = elements[0]
        self.target_character = elements[1].rstrip(":")
        self.password = elements[2]
        minmax = self.quantity_string.split("-")
        self.minimum = int(minmax[0])
        self.maximum = int(minmax[1])
        self.policy = "{} should contain {} - {} instances of character \"{}\"; detected {}.".format(self.password, self.minimum, self.maximum, self.target_character, self.password.count(self.target_character))
        return

    def isvalid(self):
        qty = self.password.count(self.target_character)
        if (qty >= self.minimum and qty <= self.maximum):
            return True
        else:
            return False

def main():
    valid = 0
    p = Problem('input.txt')
    for row in p.rows:
        e = Entry(row)
        if e.isvalid():
            valid += 1
        else:
            pass
    print("Found {} valid passwords.".format(valid))
    return

if __name__ == "__main__":
    main()