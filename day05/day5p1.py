#!/usr/bin/python3
# Day 5, Part 1 & 2 of Advent of Code 2020

class Problem():
    def __init__(self, filename):
        strings = []
        with open(filename, "r") as file:
            for line in file:
                strings.append(line)
        self.strings = strings
        return

class Entry():
    def __init__(self, boardingstring):
        self.binstring = boardingstring.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1").rstrip("\n")
        self.value = int(self.binstring, 2)
        self.row = int(self.binstring[:7], 2)
        self.column = int(self.binstring[7:], 2)
        return

def main():
    p = Problem('input.txt')
    seatids = []
    for s in p.strings:
        e = Entry(s)
        seatids.append(e.value)
    print("Highest seat number is {}".format(max(seatids)))
    manifest = sorted(seatids)
    for seat in manifest:
        if (seat+1) not in manifest and (seat+1) < max(seatids):
            print("Your seat must be seat number {}".format(seat+1))
        else:
            pass
    return

if __name__ == "__main__":
    main()