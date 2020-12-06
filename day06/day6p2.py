#!/usr/bin/python3
# Day 6, Part 2 of Advent of Code 2020
# Records questions to which *every* party in a group answers "yes"

def main():
    sum = 0
    survey = set()
    newgroup = True
    for line in open("input.txt"):
        letters = sorted(line.strip("\n"))
        newletters = set()
        if not letters:  # letters = sorted(line.strip) returns an empty set for blank lines, which is bool False
            sum += len(survey)
            print("Overlap: {} of size {} - sum: {}".format(sorted(survey), len(survey), sum))
            survey = set()
            newgroup = True
        elif newgroup:
            for char in letters:
                survey.add(char)
            newgroup = False
        else:
            for char in letters:
                newletters.add(char)
            survey = survey.intersection(newletters)
            newgroup = False
    print(sum)
    return   


if __name__ == '__main__':
    main()
