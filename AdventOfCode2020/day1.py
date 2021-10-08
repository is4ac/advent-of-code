nums = []
with open('input/day1puzzle1.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        nums.append(int(line.strip()))

# confirm input
print(nums)

# start algorithm
# use a set of complements to figure out which pair adds up to 2020
complement = set()
for number in nums:
    if 2020 - number in complement:
        print(number, 2020-number)
        print("The answer is:", number * (2020 - number))
    else:
        complement.add(number)

print("Puzzle part 2:")

# use a dictionary of sets to figure out what trio adds up to 2020
complement2 = {}
for number in nums:
    complement2[number] = set()

for i, number in enumerate(nums):
    for number2 in nums[i+1:]:
        if (2020 - number - number2) in complement2[number]:
            print(number, number2, (2020-number-number2))
            print("The answer is:", number * number2 * (2020 - number - number2))
            quit()
        else:
            complement2[number].add(number2)