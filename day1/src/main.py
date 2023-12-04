import re


def parse_input():
    with open("input.txt", 'r') as fin:
        return fin.read().splitlines()


def parse_number(number):
    num_as_word = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    return num_as_word.get(number, number)


def solve(items):
    result = 0
    for item in items:
        match = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', item)
        number = int("{}{}".format(parse_number(match[0]), parse_number(match[-1])))
        result += number
    return result


if __name__ == '__main__':
    lines = parse_input()
    sum_of_numbers = solve(lines)
    print(sum_of_numbers)

