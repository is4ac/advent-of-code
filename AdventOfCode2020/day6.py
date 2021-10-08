counts = 0

with open('input/day6.txt', 'r') as puzzle_input:
    questions = set()
    for line in puzzle_input:
        # end of a group
        if line == "\n" or line == "":
            counts += len(questions)
            questions = set()
            continue

        line = line.strip()
        for letter in line:
            questions.add(letter)


counts += len(questions)

print('Answer is:', counts)

# Part 2
counts = 0
with open('input/day6.txt', 'r') as puzzle_input:
    questions = set()
    start = True
    for line in puzzle_input:
        # end of a group
        if line == "\n" or line == "":
            counts += len(questions)
            questions = set()
            start = True
            continue

        line = line.strip()
        # for first person:
        if len(questions) == 0 and start:
            start = False
            for letter in line:
                questions.add(letter)
        # for all others
        else:
            to_remove = []
            for letter in questions:
                if letter not in line:
                    to_remove.append(letter)
            for letter in to_remove:
                questions.remove(letter)

counts += len(questions)

print('Answer is:', counts)
