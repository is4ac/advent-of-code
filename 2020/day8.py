accumulator = 0


def process(commands, line):
    global accumulator

    command = commands[line]
    if command[0] == "nop":
        return line + 1
    elif command[0] == "acc":
        accumulator += command[1]
        return line + 1
    elif command[0] == "jmp":
        return line + command[1]


def parse():
    with open('input/day8.txt', 'r') as puzzle_input:
        commands = puzzle_input.readlines()
        commands = [command.split(" ") for command in commands]
        commands = [(command[0], int(command[1].strip())) for command in commands]

        executed = set()
        to_execute = 0
        while to_execute < len(commands) and to_execute not in executed:
            executed.add(to_execute)
            temp = accumulator
            to_execute = process(commands, to_execute)
            if to_execute in executed:
                # it's done
                print("Answer is:", temp)


def parse2():
    with open('input/day8.txt', 'r') as puzzle_input:
        commands = puzzle_input.readlines()
        commands = [command.split(" ") for command in commands]
        commands = [(command[0], int(command[1].strip())) for command in commands]
        return commands


def next_line(code, line):
    if line >= len(code):
        return line
    elif code[line][0] == "jmp" or code[line][0] == "nop":
        return line
    elif code[line][0] == "acc":
        return next_line(code, line+1)


def swap(code, swap_line):
    modified = code[:]
    if modified[swap_line][0] == "jmp":
        modified[swap_line] = ("nop", modified[swap_line][1])
    elif modified[swap_line][0] == "nop":
        modified[swap_line] = ("jmp", modified[swap_line][1])
    else:
        return swap(code, next_line(code, swap_line+1))

    return modified, next_line(code, swap_line+1)


def solve2(code):
    global accumulator

    swap_line = 0
    infinite = True
    while infinite:
        modified_code, swap_line = swap(code, swap_line)
        infinite = False
        executed = set()
        to_execute = 0
        accumulator = 0
        while to_execute < len(modified_code) and to_execute not in executed:
            executed.add(to_execute)
            to_execute = process(modified_code, to_execute)
            if to_execute in executed:
                # it's done
                infinite = True

    print("Answer is:", accumulator)


# part 1
parse()

# part 2
code = parse2()
solve2(code)
