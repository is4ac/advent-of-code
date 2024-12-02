# Part 1

correct = 0
with open('input/day2.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        # parse input
        split1 = line.split("-")
        minimum = int(split1[0])
        split2 = split1[1].split(" ")
        maximum = int(split2[0])
        letter = split2[1][0]
        password = split2[2]

        # now check to see if valid
        if minimum <= password.count(letter) <= maximum:
            correct += 1

print("Answer is:", correct)

# Part 2
correct = 0
with open('input/day2.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        # parse input
        split1 = line.split("-")
        index1 = int(split1[0])
        split2 = split1[1].split(" ")
        index2 = int(split2[0])
        letter = split2[1][0]
        password = split2[2]

        # now check to see if valid
        flag = False
        if password[index1-1] == letter:
            flag = not flag
        if password[index2-1] == letter:
            flag = not flag

        if flag:
            correct += 1

print("Answer to part 2 is:", correct)

