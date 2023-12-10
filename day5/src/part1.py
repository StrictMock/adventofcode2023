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

    locations = []
    for seed in seeds:
        temp = seed
        for m in maps:
            for mapping in m:
                if temp in range(mapping[1], mapping[1] + mapping[2]):
                    difference = temp - mapping[1]
                    temp = mapping[0] + difference
                    break

        locations.append(temp)

    return sorted(locations)[0]


if __name__ == '__main__':
    run(solve)
