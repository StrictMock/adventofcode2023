import re
from common.utils import run


def solve(items: list[str]):
    result = 0

    for card in items:
        scores = card.split(": ")[-1]
        winning_numbers = [int(x) for x in scores.split(" | ")[0].split(" ") if x]
        my_numbers = [int(x) for x in scores.split(" | ")[-1].split(" ") if x]

        matched_numbers_count = len(set(winning_numbers).intersection(set(my_numbers)))
        if matched_numbers_count > 0:
            result += 2**(matched_numbers_count - 1)

    return result


if __name__ == '__main__':
    run(solve)
