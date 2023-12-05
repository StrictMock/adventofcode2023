def parse_input():
    with open("input.txt", 'r') as fin:
        return fin.read().splitlines()


def run(solve_func):
    lines = parse_input()
    result = solve_func(lines)
    print(result)
