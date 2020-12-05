#!/usr/bin/python3
# Day 4, Part 2 of Advent of Code 2020

# Adapting Nathan's elegant answer - what's going on here? 
import unittest

class CompletePassport(object):
    def __init__(self, rawpassport=dict):
        self.data = rawpassport
        self.uid = self.data['pid']
        self.issue = self.data['iyr']
        self.expire = self.data['eyr']
        self.birth = self.data['byr']
        self.height = self.data['hgt']
        self.hair = self.data['hcl']
        self.eyes = self.data['ecl']
        return

    def validate(self):
        valideyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        validfields = 0
        validfields += 1 if self.isNineDigitInt(self.uid) else 0
        validfields += 2 if self.isYearBetween(self.issue, 2010, 2020) else 0
        validfields += 4 if self.isYearBetween(self.expire, 2020, 2030) else 0
        validfields += 8 if self.isYearBetween(self.birth, 1920, 2002) else 0
        validfields += 16 if self.isValidHeight(self.height) else 0
        validfields += 32 if self.isColorString(self.hair) else 0 
        validfields += 64 if (self.eyes) in valideyes else 0 
        # print("valid fields: {}".format(bin(validfields)))
        return validfields

    def display(self):
        valideyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        print("PASSPORT ID  : {}    : {}".format(self.uid, self.isNineDigitInt(self.uid)))
        print("ISSUED       : {}    : {}".format(self.issue, self.isYearBetween(self.issue, 2010, 2020)))
        print("EXPIRES      : {}    : {}".format(self.expire, self.isYearBetween(self.expire, 2020, 2030)))
        print("BIRTH YEAR   : {}    : {}".format(self.birth, self.isYearBetween(self.birth, 1920, 2002)))
        print("HEIGHT       : {}    : {}".format(self.height, self.isValidHeight(self.height)))
        print("HAIR COLOR   : {}    : {}".format(self.hair, self.isColorString(self.hair)))
        print("EYE COLOR    : {}    : {}".format(self.eyes, self.eyes in valideyes))

    def isNineDigitInt(self, numstring):
        if len(numstring) != 9:
            # print("UID wrong length: {}".format(numstring))
            return False
        else: 
            pass
        try:
            value = int(numstring)
            if value > 0:
                # print("UID: {}".format(numstring))
                return True
        except:
            return False

    def isColorString(self, hairstring):
        if not isinstance(hairstring, str):
            return False
        elif len(hairstring) != 7:
            return False
        elif hairstring[0] != "#":
            return False
        else: 
            hexes = hairstring[1:6]
            try:
                value = int(hexes, 16)
                # print("allowing hex value: {}".format(hairstring))
                return True
            except:
                return False

    def isValidHeight(self, heightstring):
        validunits = ['in', 'cm']
        if not isinstance(heightstring, str):
            return False
        elif heightstring[-2:] not in validunits:
            # print("invalid height units {} in {}".format(heightstring[-2:], heightstring))
            return False
        else:
            try:
                height = int(heightstring[:-2])
                units = heightstring[-2:]
                if units == 'in' and height >= 59 and height <= 76:
                    return True
                elif units == 'cm' and height >= 150 and height <= 193:
                    return True
                else:
                    # print("Height measurement of {} not valid".format(heightstring))
                    return False
            except:
                return False

    def isYearBetween(self, value, min=int, max=int):
        try:
            converted = int(value) 
        except:
            # print("Not a year: {}".format(value))
            return False
        finally:
            if converted >= min and converted <= max:
                # print("{} is between {} and {}".format(value, min, max))
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
    records = []
    for line in open("input.txt"):
        parts = dict(part.split(':') for part in line.split())
        if not parts:
            if isComplete(passport):
                complete += 1
            passport = dict()
        else:
            passport.update(parts)
        if isComplete(passport):
            p = CompletePassport(passport)
            records.append(p)
            complete += 1

    validrecords = 0
    for r in records:
        print("-----")
        r.display()
        if r.validate() == 127:
            print("OK // VALID")
            validrecords += 1
        else:
            pass
            print("Invalid!")

    print("Found {} valid records.".format(validrecords))
    print("We appear to still be letting some bad records through.")

if __name__ == '__main__':
    main()