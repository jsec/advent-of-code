from functools import reduce

from util.input import get_split_input


def lookup(start, mapping):
    for m in mapping.split("\n")[1:]:
        dst, src, ln = map(int, m.split())
        delta = start - src
        if delta in range(ln):
            return dst + delta
    else:
        return start


def part1(data: list[str]) -> int:
    seeds, *mappings = data
    seeds = map(int, seeds.split()[1:])

    return min(reduce(lookup, mappings, int(s)) for s in seeds)


def part2(data: list[str]):
    seeds, *maps = data

    seeds = [int(seed) for seed in seeds.split()[1:]]
    maps = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps]

    locations = []
    for i in range(0, len(seeds), 2):
        ranges = [[seeds[i], seeds[i + 1] + seeds[i]]]
        results = []
        for _map in maps:
            while ranges:
                start_range, end_range = ranges.pop()
                for target, start_map, r in _map:
                    end_map = start_map + r
                    offset = target - start_map
                    if end_map <= start_range or end_range <= start_map:
                        continue
                    if start_range < start_map:
                        ranges.append([start_range, start_map])
                        start_range = start_map
                    if end_map < end_range:
                        ranges.append([end_map, end_range])
                        end_range = end_map
                    results.append([start_range + offset, end_range + offset])
                    break
                else:
                    results.append([start_range, end_range])
            ranges = results
            results = []
        locations += ranges
    print(min(loc[0] for loc in locations))


data = get_split_input("\n\n")

print("P1:", part1(data))
print("P2:", part2(data))
