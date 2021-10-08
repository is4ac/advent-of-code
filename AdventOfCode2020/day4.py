passports = []

with open('input/day4.txt', 'r') as puzzle_file:
    passport = {}
    for line in puzzle_file:
        # end of a passport
        if line == "\n":
            passports.append(passport)
            passport = {}
            continue

        # add any key-value pairs
        pairs = line.split(" ")
        # clean
        pairs = [pair.strip() for pair in pairs]

        # add each pair to dict
        for pair in pairs:
            keyvalue = pair.split(":")
            passport[keyvalue[0]] = keyvalue[1]

passports.append(passport)


def validation(key, passport):
    value = passport[key]
    if key == 'byr':
        try:
            if 1920 <= int(value) <= 2002:
                return True
        except ValueError:
            return False
    elif key == 'iyr':
        try:
            if 2010 <= int(value) <= 2020:
                return True
        except ValueError:
            return False
    elif key == 'eyr':
        try:
            if 2020 <= int(value) <= 2030:
                return True
        except ValueError:
            return False
    elif key == 'hgt':
        try:
            number = int(value[:-2])
            measurement = value[-2:]
            if measurement == 'cm':
                if 150 <= number <= 193:
                    return True
            elif measurement == 'in':
                if 59 <= number <= 76:
                    return True
        except ValueError:
            return False
    elif key == 'hcl':
        validchars = '0123456789abcdef'
        if value[0] == "#":
            for val in value[1:]:
                if val not in validchars:
                    return False
            return True
    elif key == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value in colors:
            return True
    elif key == 'pid':
        validchars = '0123456789'
        if len(value) == 9:
            for val in value:
                if val not in validchars:
                    return False
            return True

    return False


# validation
def valid(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in required:
        if key not in passport:
            return False
        else:
            if not validation(key, passport):
                return False
    return True


correct = 0
for book in passports:
    if valid(book):
        correct += 1

print("Answer is:", correct)
