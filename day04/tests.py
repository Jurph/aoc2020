#!/usr/bin/python3
# Unit tests for day 4

from day4p2 import CompletePassport
import unittest

class TestValidityCheckers(unittest.TestCase):
    def setUp(self):
        passport = dict()
        validexample = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f"
        parts = dict(part.split(':') for part in validexample.split())
        passport.update(parts)
        self.v = CompletePassport(passport)
        return

    def test_pids(self):
        self.assertTrue(self.v.isNineDigitInt(self.v.pid))
        self.assertTrue(self.v.isNineDigitInt('012345678'))
        self.assertTrue(self.v.isNineDigitInt('000000001'))
        self.assertTrue(self.v.isNineDigitInt('999999999'))
        self.assertFalse(self.v.isNineDigitInt('0123456789'))
        self.assertFalse(self.v.isNineDigitInt('01234567'))
        self.assertFalse(self.v.isNineDigitInt('01234567a'))
        self.assertFalse(self.v.isNineDigitInt('0x0123456'))
        self.assertFalse(self.v.isNineDigitInt('000000000'))
        self.assertFalse(self.v.isNineDigitInt('-00000001'))
        return

    def test_dates(self):
        floor = 2000
        ceiling = 3000
        self.assertTrue(self.v.isYearBetween(self.v.birth, 1920, 2002))
        self.assertTrue(self.v.isYearBetween(self.v.issue, 2010, 2020))
        self.assertTrue(self.v.isYearBetween(self.v.expire, 2020, 2030))
        self.assertTrue(self.v.isYearBetween(floor, floor, ceiling))
        self.assertTrue(self.v.isYearBetween(ceiling, floor, ceiling))
        self.assertFalse(self.v.isYearBetween(str(floor-1), floor, ceiling))
        self.assertFalse(self.v.isYearBetween(str(ceiling+1), floor, ceiling))
        self.assertFalse(self.v.isYearBetween(str(floor-0.001), floor, ceiling))
        self.assertFalse(self.v.isYearBetween(str(ceiling+0.001), floor, ceiling))
        return
    
    def test_hexcolors(self):
        self.assertTrue(self.v.isColorString(self.v.hair))
        self.assertTrue(self.v.isColorString('#000000'))
        self.assertTrue(self.v.isColorString('#aabbcc'))
        self.assertFalse(self.v.isColorString('#0x03aa'))
        return        

if __name__ == '__main__':
    unittest.main()