from collections import deque

def parse(str):
    bag = str[:str.find('bags')].strip()
    contains = []
    split = str.split(" ")
    split = split[5:]

    # empty bag
    if split[0] == "other":
        return bag, contains

    contained_bag = split[0] + " " + split[1]
    contains.append(contained_bag)

    while len(split) > 5:
        split = split[4:]
        contained_bag = split[0] + " " + split[1]
        contains.append(contained_bag)

    return bag, contains


def contains_shiny(bag_tree, can_contain_shiny, bag):
    goal = "shiny gold"
    queue = deque(bag_tree[bag])
    visited = set()

    while queue:
        value = queue.popleft()
        if value == goal or value in can_contain_shiny:
            return True

        visited.add(value)
        next_bags = bag_tree[value]
        for item in next_bags:
            if item not in visited:
                queue.append(item)

    return False


can_contain_shiny = set()
bag_tree = {}
bags = []

with open('input/day7.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        bag, contains = parse(line)
        bags.append(bag)
        bag_tree[bag] = contains
        if 'shiny gold' in contains:
            can_contain_shiny.add(bag)

for bag in bags:
    if contains_shiny(bag_tree, can_contain_shiny, bag):
        can_contain_shiny.add(bag)

print("Answer is:", len(can_contain_shiny))

# part 2
def parse2(str):
    bag = str[:str.find('bags')].strip()
    contains = []
    split = str.split(" ")
    split = split[4:]

    # empty bag
    if split[0] == "no":
        return bag, contains

    number = int(split[0])
    contained_bag = split[1] + " " + split[2]
    contains.append((contained_bag, number))

    while len(split) > 5:
        split = split[4:]
        number = int(split[0])
        contained_bag = split[1] + " " + split[2]
        contains.append((contained_bag, number))

    return bag, contains


bag_tree2 = {}
with open('input/day7.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        bag, contains = parse2(line)
        bags.append(bag)
        bag_tree2[bag] = contains


# count bags in shiny gold
def bag_count(bag_tree2, bag):
    # base case
    if len(bag_tree2[bag]) == 0:
        return 0
    # recursive case
    else:
        baglist = bag_tree2[bag]

        count = 0
        for bagname, number in baglist:
            count += number + number * bag_count(bag_tree2, bagname)
        return count


count = bag_count(bag_tree2, 'shiny gold')
print("Answer is:", count)