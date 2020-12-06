#!/usr/bin/python3
# Day 6, Part 1 of Advent of Code 2020
# Counts the total number of unique questions for which any person in a group answered "yes"

def main():
    sum = 0
    survey = set()
    for line in open("input.txt"):
        letters = sorted(line.strip("\n"))
        if not letters: # blank line
            sum += len(survey)
            survey = set()
        else:
            for char in letters:
                survey.add(char)
            print("Questionnaire answer {} has length {} - sum is currently {}".format(survey, len(survey), sum))
    print(sum)
    return   


if __name__ == '__main__':
    main()
