from common.utils import run
from collections import defaultdict


def append_adjacent_asterisks(items: list[str], row_number: int, col_number: int, adjacent_asterisks: set[tuple[int, int]]):
    previous_row = items[max(0, row_number - 1)]
    current_row = items[row_number]
    next_row = items[min(len(items) - 1, row_number + 1)]

    previous_col_number = max(0, col_number - 1)
    next_col_number = min(len(current_row), col_number + 2)

    for i in range(previous_col_number, next_col_number):
        if previous_row[i] == '*':
            adjacent_asterisks.add((i, max(0, row_number - 1)))
        if current_row[i] == '*':
            adjacent_asterisks.add((i, row_number))
        if next_row[i] == '*':
            adjacent_asterisks.add((i, min(len(items) - 1, row_number + 1)))


def solve(items: list[str]):
    result = 0

    asterisk_to_gears = defaultdict(list)

    for row_number in range(0, len(items)):
        current_row = items[row_number]

        number_chars = []
        adjacent_asterisks = set()

        for col_number in range(0, len(current_row)):
            current_char = current_row[col_number]

            if current_char.isdigit():
                number_chars.append(current_char)
                append_adjacent_asterisks(items, row_number, col_number, adjacent_asterisks)

            if not current_char.isdigit() or (col_number == len(current_row) - 1):
                if len(number_chars) > 0 and len(adjacent_asterisks) > 0:
                    for asterisk in adjacent_asterisks:
                        asterisk_to_gears[asterisk].append(int("".join(number_chars)))

                number_chars.clear()
                adjacent_asterisks.clear()

    for gear in asterisk_to_gears.values():
        if len(gear) == 2:
            result += gear[0] * gear[1]

    return result


if __name__ == '__main__':
    run(solve)
