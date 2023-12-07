import re
from common.utils import run


def solve(items: list[str]):
    result = 0
    for item in items:
        splitted = item.split(':')

        revealed_cubes = {}
        for x in re.split(';|,', splitted[-1]):
            cube_data = x.split(' ')
            revealed_cubes[cube_data[-1]] = max(revealed_cubes.get(cube_data[-1], 0), int(cube_data[-2]))

        multiplied_values = 1
        for v in revealed_cubes.values():
            multiplied_values *= v

        result += multiplied_values
    return result


if __name__ == '__main__':
    run(solve)
