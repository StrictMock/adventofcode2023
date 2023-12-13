from day6.src.part1 import solve


def test():
    input = """Time:      7  15   30
Distance:  9  40  200"""

    assert solve(input.splitlines()) == 288
