def getRow(code):
    rows = list(range(128))

    for letter in code:
        if letter == "F":
            rows = rows[:len(rows)//2]
        elif letter == "B":
            rows = rows[len(rows)//2:]

    return rows[0]


def getColumn(code):
    cols = list(range(8))

    for letter in code:
        if letter == "L":
            cols = cols[:len(cols) // 2]
        elif letter == "R":
            cols = cols[len(cols) // 2:]

    return cols[0]


maxSeat = -1
with open('input/day5.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        row = getRow(line[:7])
        col = getColumn(line[7:])
        seatID = row * 8 + col
        if seatID > maxSeat:
            maxSeat = seatID

print("Answer is:", maxSeat)

# Part 2
seats = set(range(maxSeat+1))
with open('input/day5.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        row = getRow(line[:7])
        col = getColumn(line[7:])
        seatID = row * 8 + col
        seats.remove(seatID)

print(seats)
