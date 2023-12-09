import re
from common.utils import run


def should_be_added(items: list[str], row_number: int, col_number: int):
    previous_row = items[max(0, row_number - 1)]
    current_row = items[row_number]
    next_row = items[min(len(items) - 1, row_number + 1)]

    previous_col_number = max(0, col_number - 1)
    next_col_number = min(len(current_row), col_number + 2)

    for i in range(previous_col_number, next_col_number):
        if not previous_row[i].isdigit() and previous_row[i] != '.':
            return True
        if not current_row[i].isdigit() and current_row[i] != '.':
            return True
        if not next_row[i].isdigit() and next_row[i] != '.':
            return True
    return False


def solve(items: list[str]):
    result = 0
    for row_number in range(0, len(items)):
        current_row = items[row_number]

        number_chars = []
        should_add_to_result = []

        for col_number in range(0, len(current_row)):
            current_char = current_row[col_number]

            if current_char.isdigit():
                number_chars.append(current_char)
                should_add_to_result.append(should_be_added(items, row_number, col_number))

            if not current_char.isdigit() or (col_number == len(current_row) - 1):
                if len(number_chars) > 0 and any(should_add_to_result):
                    result += int("".join(number_chars))
                number_chars.clear()
                should_add_to_result.clear()

    return result


if __name__ == '__main__':
    run(solve)
