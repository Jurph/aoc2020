#!/usr/bin/python3
# Day 4, Part 2 of Advent of Code 2020

# Adapting Nathan's elegant answer - what's going on here? 

class Passport(object):
    def __init__(self, passport=dict):
        self.data = passport
        self.uid = self.data['pid']
        self.birth = self.data['byr']
        self.expire = self.data['eyr']
        self.issue = self.data['iyr']
        self.height = self.data['hgt']
        self.hair = self.data['hcl']
        self.eyes = self.data['ecl']
        return

def isOnList(self, values=list):
    if self in values:
        return True
    else:
        return False

def isColorString(self):
    if not isinstance(self, str):
        return False
    elif len(self) != 7:
        return False
    elif self[0] != "#":
        return False
    else: 
        hexes = self[1:6]
        try:
            value = int(hexes.unhexlify())
            return True
        except:
            return False
        
def isYearBetween(self, min=int, max=int):
    try:
        converted = int(self) 
    except:
        return False
    finally:
        if converted >= min and converted <= max:
            return True
        else:
            return False
    return

def isComplete(passport):
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return required.intersection(passport) == required

def main(): 
    complete = 0
    passport = dict()
    for line in open("input.txt"):
        parts = dict(part.split(':') for part in line.split())
        if not parts:
            if isComplete(passport):
                complete += 1
            passport = dict()
        else:
            passport.update(parts)

    if isComplete(passport):
        complete += 1

    eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    

if __name__ == '__main__':
    main()