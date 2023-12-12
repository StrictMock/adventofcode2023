from common.utils import run


def parse_map(maps: list[str], map_name: str) -> list[list[int]]:
    begin_index = maps.index(map_name) + 1
    end_index = maps.index("", begin_index) if "" in maps[begin_index:] else len(maps)

    result = []

    for line in maps[begin_index:end_index]:
        data = [int(x) for x in line.split(" ") if x.isdigit()]
        result.append(data)
    return result


def solve(items: list[str]):
    seeds = [int(x) for x in items[0].split(" ") if x.isdigit()]
    maps = [parse_map(items, "seed-to-soil map:"), parse_map(items, "soil-to-fertilizer map:"),
            parse_map(items, "fertilizer-to-water map:"), parse_map(items, "water-to-light map:"),
            parse_map(items, "light-to-temperature map:"), parse_map(items, "temperature-to-humidity map:"),
            parse_map(items, "humidity-to-location map:")]

    reversed_maps = reversed(maps)

    seeds_ranges = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]

    location = 0

    while True:
        temp = location

        for m in reversed_maps:
            for mapping in m:
                if temp in range(mapping[0], mapping[0] + mapping[2]):
                    difference = temp - mapping[0]
                    temp = mapping[1] + difference
                    break

        for seeds_range in seeds_ranges:
            if temp in range(seeds_range[0], seeds_range[1] + 1):
                return location

        location += 1


if __name__ == '__main__':
    run(solve)
