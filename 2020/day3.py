answer = []

# right 1, down 1
with open('input/day3.txt', 'r') as puzzle_input:
    toboggan = 0
    trees = 0
    for line in puzzle_input:
        line = line.strip()
        if line[toboggan] == '#':
            trees += 1
        toboggan = (toboggan + 1) % len(line)

answer.append(trees)

# right 3, down 1
with open('input/day3.txt', 'r') as puzzle_input:
    toboggan = 0
    trees = 0
    for line in puzzle_input:
        line = line.strip()
        if line[toboggan] == '#':
            trees += 1
        toboggan = (toboggan + 3) % len(line)

answer.append(trees)

# right 5, down 1
with open('input/day3.txt', 'r') as puzzle_input:
    toboggan = 0
    trees = 0
    for line in puzzle_input:
        line = line.strip()
        if line[toboggan] == '#':
            trees += 1
        toboggan = (toboggan + 5) % len(line)

answer.append(trees)

# right 7, down 1
with open('input/day3.txt', 'r') as puzzle_input:
    toboggan = 0
    trees = 0
    for line in puzzle_input:
        line = line.strip()
        if line[toboggan] == '#':
            trees += 1
        toboggan = (toboggan + 7) % len(line)

answer.append(trees)

# right 1, down 2
with open('input/day3.txt', 'r') as puzzle_input:
    toboggan = 0
    trees = 0
    line_count = 0
    for line in puzzle_input:
        if line_count % 2 == 1:
            line_count += 1
            continue
        line = line.strip()
        if line[toboggan] == '#':
            trees += 1
        toboggan = (toboggan + 1) % len(line)
        line_count += 1

answer.append(trees)

print(answer)

multiplied = 1
for tree in answer:
    multiplied *= tree
print("Answer is:", multiplied)