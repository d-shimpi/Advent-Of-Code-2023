import re

# Part 1
input_file = open('day1_1_input.txt', 'r')
lines = input_file.readlines()

sum = 0

for line in lines:
    digits = re.findall(r'\d', line)
    first_digit = digits[0]
    last_digit = digits[len(digits) - 1]
    sum = sum + int(first_digit + last_digit)

print("Part 1 Answer:")
print(sum)

def convertToDigit(input):
    num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    if input.isdigit(): 
        return input
    else:
        return str(num_dict[input])

sum = 0
# Part Two
for line in lines:
    first_digit = re.search(r'\d|one|two|three|four|five|six|seven|eight|nine', line).group()
    last_digit = re.search(r'(?s:.*)(\d|one|two|three|four|five|six|seven|eight|nine)', line).group(1)
    first_digit = convertToDigit(first_digit)
    last_digit = convertToDigit(last_digit)
    digit = first_digit + last_digit
    sum = sum + int(digit)

print("Part 2 Answer:")
print(sum)