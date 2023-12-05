import re
from common.utils import run


def is_valid(revealed_cube):
    if revealed_cube[-1] == 'red':
        return int(revealed_cube[-2]) <= 12
    if revealed_cube[-1] == 'green':
        return int(revealed_cube[-2]) <= 13
    if revealed_cube[-1] == 'blue':
        return int(revealed_cube[-2]) <= 14


def are_all_valid(revealed_cubes):
    for cube in revealed_cubes:
        if not is_valid(cube):
            return False
    return True


def solve(items: list[str]):
    result = 0
    for item in items:
        splitted = item.split(':')
        game_number = int(splitted[0].split("Game ")[-1])
        revealed_cubes = [x.split(' ')[-2:] for x in re.split(';|,', splitted[-1])]
        if are_all_valid(revealed_cubes):
            result += game_number

    return result


if __name__ == '__main__':
    run(solve)
