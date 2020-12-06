#!/usr/bin/python3
# Day 6, Part 1 of Advent of Code 2020

def main():
    questions = 0
    questionnaire = set()
    for line in open("input.txt"):
        letters = sorted(line)
        if not letters:
            questions = len(questionnaire)
            questionnaire = set()
        else:
            for char in letters:
                questionnaire.add(char)
    print(questions)
    return   


if __name__ == '__main__':
    main()
