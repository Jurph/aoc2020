#!/usr/bin/python3
# Day 2, Part 1 of Advent of Code 2020

# Generic class for holding the input
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
        self.quantity_string, self.target_character, self.password = row.replace(':', '').split(" ")
        self.minimum, self.maximum = map(int, self.quantity_string.split("-"))
        # "policy" allows us to access "Entry.policy" for an entry and print its status 
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