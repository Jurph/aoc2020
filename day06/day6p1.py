#!/usr/bin/python3
# Day 6, Part 1 of Advent of Code 2020

def main():
    questions = 0
    questionnaire = set()
    for line in open("testdata.txt"):
        letters = sorted(line.strip("\n"))
        if not letters: # blank line
            questions += len(questionnaire)
            questionnaire = set()
        else:
            for char in letters:
                questionnaire.add(char)
            print("Questionnaire answer {} has length {} - sum is currently {}".format(questionnaire, len(questionnaire), questions))
    print(questions)
    return   


if __name__ == '__main__':
    main()
