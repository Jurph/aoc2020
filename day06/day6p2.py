#!/usr/bin/python3
# Day 6, Part 2 of Advent of Code 2020
# Must not record a yes from *any* party, but instead an answer from *every* party.

def main():
    questions = 0
    newletters = set()
    questionnaire = set()
    newgroup = True
    for line in open("testdata.txt"):
        letters = sorted(line.strip("\n"))
        if not letters: # blank line
            questions += len(questionnaire)
            print("ended a group - sum is {}".format(questions))
            questionnaire = set()
            newletters = set()
            newgroup = True
        elif newgroup:
            for char in letters:
                questionnaire.add(char)
            newgroup = False
        else:
            for char in letters:
                newletters.add(char)
            questionnaire = questionnaire.intersection(newletters)
            newgroup = False

        print("Questionnaire answer {} has length {} - sum is currently {}".format(questionnaire, len(questionnaire), questions))
    print(questions)
    return   


if __name__ == '__main__':
    main()
