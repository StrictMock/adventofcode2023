from common.utils import run


def solve(items: list[str]):
    time = int("".join([x for x in items[0].split(" ") if x.isnumeric()]))
    record_distance = int("".join([x for x in items[1].split(" ") if x.isnumeric()]))

    result = 0

    for speed in range(0, time):
        distance = speed * (time - speed)
        if distance > record_distance:
            result += 1

    return result


if __name__ == '__main__':
    run(solve)
