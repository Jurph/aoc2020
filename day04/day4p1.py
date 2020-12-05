#!/usr/bin/python3
# Day 4, Part 1 of Advent of Code 2020


# Nathan's elegant answer - what's going on here? 
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def isValid(passport):
    return required.intersection(passport) == required

if __name__ == '__main__':
    valid = 0
    passport = dict()
    for line in open("input.txt"):
        parts = dict(part.split(':') for part in line.split())
        if not parts:
            if isValid(passport):
                valid += 1
            passport = dict()
        else:
            passport.update(parts)
        

    if isValid(passport):
        valid += 1

    print(valid)


# JR's broken version - why not work think go?
# Input class
class Problem():
    def __init__(self, filename):
        with open(filename, "r") as file:
            for line in file:
                parts = dict(part.split(':') for part in line.split())
                if not parts:
                    if isValid(passport):
                        valid += 1
                        passport = dict()
                else:
                    passport.update(parts)
                return

    def condense(self, list):
        entry = 0
        denselist = []
        for row in list:
            if row in ["\n", "\r\n", ""]:
                entry += 1
            else:
                denselist[entry] += row
                print("Added \"{}\" to row".format(denselist[entry]))
        return denselist

class Passport():
    def __init__(self, row=str):
        return

    def istree(self, character=chr):
        return

    
def main():
    p = Problem('input.txt')
    return

if __name__ == "__main__":
    main()