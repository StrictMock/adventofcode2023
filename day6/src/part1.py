from common.utils import run


def solve(items: list[str]):
    time_to_distance = dict(zip([int(x) for x in items[0].split(" ") if x.isnumeric()],
                                [int(x) for x in items[1].split(" ") if x.isnumeric()]))

    result = 1

    for time, record_distance in time_to_distance.items():
        number_of_ways_to_win = 0
        for speed in range(0, time):
            distance = speed * (time - speed)
            if distance > record_distance:
                number_of_ways_to_win += 1
        result *= number_of_ways_to_win

    return result


if __name__ == '__main__':
    run(solve)
