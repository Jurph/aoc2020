#!/usr/bin/python3
# Day 2, Part 2 of Advent of Code 2020
# Change in policy - now "min" and "max" are positional

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
        positions = self.quantity_string.split("-")
        self.firstposition = int(positions[0])
        self.secondposition = int(positions[1])
        return

    def isvalid(self):
        # Exactly one of the cases must be met, so we return false if both are
        if self.password[self.firstposition-1] == self.target_character and self.password[self.secondposition-1] == self.target_character:
            # print("{} has a \"{}\" at position {} and {}    : INVALID".format(self.password, self.target_character, self.firstposition, self.secondposition))
            return False
        elif self.password[self.firstposition-1] == self.target_character and self.password[self.secondposition-1] != self.target_character:
            # print("{} has a \"{}\" at position {} but not {}: VALID".format(self.password, self.target_character, self.firstposition, self.secondposition))
            return True
        elif self.password[self.firstposition-1] != self.target_character and self.password[self.secondposition-1] == self.target_character:
            # print("{} has a \"{}\" at position {} but not {}: VALID".format(self.password, self.target_character, self.secondposition, self.firstposition))
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