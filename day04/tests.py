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
        self.assertTrue(self.v.isNineDigitInt('000000000'))
        self.assertTrue(self.v.isNineDigitInt('000000001'))
        self.assertTrue(self.v.isNineDigitInt('999999999'))
        self.assertFalse(self.v.isNineDigitInt('01234567'))
        self.assertFalse(self.v.isNineDigitInt('01234567a'))
        self.assertFalse(self.v.isNineDigitInt('0x0123456'))
        self.assertFalse(self.v.isNineDigitInt('-00000001'))
        self.assertFalse(self.v.isNineDigitInt('0123456789'))        
        return

    def test_dates(self):
        floor = 2000
        ceiling = 3000
        self.assertTrue(self.v.isYearBetween(self.v.birth, 1920, 2002))
        self.assertTrue(self.v.isYearBetween(self.v.issue, 2010, 2020))
        self.assertTrue(self.v.isYearBetween(self.v.expire, 2020, 2030))
        self.assertTrue(self.v.isYearBetween(str(floor), floor, ceiling))
        self.assertTrue(self.v.isYearBetween(str(ceiling), floor, ceiling))
        self.assertFalse(self.v.isYearBetween(str(floor-1), floor, ceiling))
        self.assertFalse(self.v.isYearBetween(str(ceiling+1), floor, ceiling))
        self.assertFalse(self.v.isYearBetween(str(floor-0.001), floor, ceiling))
        self.assertFalse(self.v.isYearBetween(str(ceiling+0.001), floor, ceiling))
        return
 
    def test_hexcolors(self):
        self.assertTrue(self.v.isColorString(self.v.hair))
        self.assertTrue(self.v.isColorString('#000000'))
        self.assertTrue(self.v.isColorString('#aabbcc'))
        self.assertTrue(self.v.isColorString('#00bbcc'))
        self.assertFalse(self.v.isColorString('000000'))   # needs leading "#"
        self.assertFalse(self.v.isColorString('aabbcc'))        
        self.assertFalse(self.v.isColorString('#AABBCC'))  # capitals not permitted
        self.assertFalse(self.v.isColorString('#0x03aa'))  # "0x" prefix not okay
        self.assertFalse(self.v.isColorString('#bcdefg'))  # "g" is not valid hex  
        self.assertFalse(self.v.isColorString('#ffffffff'))
        return

    def test_eyecolors(self):
        valideyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        self.assertTrue(self.v.eyes in valideyes)
        self.assertTrue('amb' in valideyes)
        self.assertTrue('blu' in valideyes)
        self.assertTrue('brn' in valideyes)
        self.assertTrue('gry' in valideyes)
        self.assertTrue('grn' in valideyes)
        self.assertTrue('hzl' in valideyes)
        self.assertTrue('oth' in valideyes)
        self.assertFalse('AMB' in valideyes)
        self.assertFalse('zzz' in valideyes)
        self.assertFalse('grt' in valideyes)
        self.assertFalse('xry' in valideyes)
        self.assertFalse('gryy' in valideyes)
        self.assertFalse('green' in valideyes)
        self.assertFalse('amblu' in valideyes)
        self.assertFalse('hzloth' in valideyes)
        self.assertFalse('#ffffff' in valideyes)
        return

    def test_heights(self):
        self.assertTrue(self.v.isValidHeight(self.v.height))
        self.assertTrue(self.v.isValidHeight('59in'))
        self.assertTrue(self.v.isValidHeight('76in'))
        self.assertTrue(self.v.isValidHeight('150cm'))
        self.assertTrue(self.v.isValidHeight('193cm'))
        self.assertFalse(self.v.isValidHeight('194cm'))
        self.assertFalse(self.v.isValidHeight('149cm'))
        self.assertFalse(self.v.isValidHeight('59cm'))
        self.assertFalse(self.v.isValidHeight('76cm'))
        self.assertFalse(self.v.isValidHeight('58in'))
        self.assertFalse(self.v.isValidHeight('77in'))
        self.assertFalse(self.v.isValidHeight('151in'))
        self.assertFalse(self.v.isValidHeight('192in'))
        self.assertFalse(self.v.isValidHeight('59'))
        self.assertFalse(self.v.isValidHeight('95'))
        self.assertFalse(self.v.isValidHeight('cm'))
        self.assertFalse(self.v.isValidHeight('150CM'))
        self.assertFalse(self.v.isValidHeight('151in'))
        return

def main():
    unittest.main()

if __name__ == '__main__':
    main()