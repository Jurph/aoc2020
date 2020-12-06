#!/usr/bin/python3
# Day 6, Part 2 of Advent of Code 2020
# Must not record a yes from *any* party, but instead an answer from *every* party.

def main():
    questions = 0
    questionnaire = set()
    newgroup = True
    for line in open("input.txt"):
        letters = sorted(line.strip("\n"))
        newletters = set()
        if not letters: # blank line
            questions += len(questionnaire)
            print("Overlap: {} of size {} - sum: {}".format(sorted(questionnaire), len(questionnaire), questions))
            questionnaire = set()
            newletters = set()
            newgroup = True
        elif newgroup:
            newletters = set()
            for char in letters:
                questionnaire.add(char)
            newgroup = False
        else:
            for char in letters:
                newletters.add(char)
            questionnaire = questionnaire.intersection(newletters)
            newgroup = False

    print(questions)
    return   


if __name__ == '__main__':
    main()
