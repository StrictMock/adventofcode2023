from common.utils import run


def parse_map(maps: list[str], map_name: str) -> dict[int, int]:
    begin_index = maps.index(map_name) + 1
    end_index = maps.index("", begin_index) if "" in maps[begin_index:] else len(maps)

    result = {}

    for line in maps[begin_index:end_index]:
        data = [int(x) for x in line.split(" ") if x.isdigit()]
        destination_begin = data[0]
        source_begin = data[1]
        length = data[2]

        for i in range(0, length):
            result[source_begin + i] = destination_begin + i
    return result


def solve(items: list[str]):
    seeds = [int(x) for x in items[0].split(" ") if x.isdigit()]
    maps = [parse_map(items, "seed-to-soil map:"), parse_map(items, "soil-to-fertilizer map:"),
            parse_map(items, "fertilizer-to-water map:"), parse_map(items, "water-to-light map:"),
            parse_map(items, "light-to-temperature map:"), parse_map(items, "temperature-to-humidity map:"),
            parse_map(items, "humidity-to-location map:")]

    locations = set()
    for seed in seeds:
        temp = seed
        for m in maps:
            temp = m.get(temp, temp)
        locations.add(temp)

    return list(locations)[0]


if __name__ == '__main__':
    run(solve)
