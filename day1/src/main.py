import re


def parse_input():
    with open("input.txt", 'r') as fin:
        return fin.read().splitlines()


def solve(items):
    result = 0
    for item in items:
        match = re.findall(r'\d', item)
        number = int("{}{}".format(match[0], match[-1]))
        result += number
    return result


if __name__ == '__main__':
    lines = parse_input()
    sum_of_numbers = solve(lines)
    print(sum_of_numbers)

