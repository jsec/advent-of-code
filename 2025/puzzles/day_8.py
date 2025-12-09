from collections import defaultdict
from itertools import combinations
from math import sqrt
from typing import override
from util.solver import Solver
from util.input import Input


def distance_3d(first, second):
    return sqrt(
        pow(first[0] - second[0], 2)
        + pow(first[1] - second[1], 2)
        + pow(first[2] - second[2], 2)
    )


class Day8(Solver):
    def get_input(self):
        input = [
            tuple(map(int, (line.strip().split(","))))
            for line in Input(8).parse_as_lines()
        ]

        combos = combinations(input, 2)
        boxes = [(i, j, distance_3d(i, j)) for i, j in combos]

        return sorted(boxes, key=lambda b: b[2])

    def run(self, p2=False):
        boxes = self.get_input()

        if not p2:
            boxes = boxes[:1000]

        point_map = {}
        network_map = defaultdict(set)
        next_id = 0

        for first, second, _ in boxes:
            if first not in point_map and second not in point_map:
                point_map[first] = next_id
                point_map[second] = next_id
                network_map[next_id] |= {first, second}
                next_id += 1
            elif first in point_map and second in point_map:
                if point_map[first] == point_map[second]:
                    continue
                else:
                    old_id = point_map[second]

                    for point in network_map[point_map[second]]:
                        point_map[point] = point_map[first]

                    network_map[point_map[first]] |= network_map[old_id]
                    del network_map[old_id]
            elif first in point_map:
                point_map[second] = point_map[first]
                network_map[point_map[first]].add(second)
            else:
                point_map[first] = point_map[second]
                network_map[point_map[second]].add(first)

            if p2:
                if len(network_map) == 1 and len(network_map[point_map[first]]) == 1000:
                    return first[0] * second[0]

        networks = sorted(network_map.values(), key=lambda n: len(n), reverse=True)
        return len(networks[0]) * len(networks[1]) * len(networks[2])

    @override
    def solve_part_1(self) -> int:
        return self.run()

    @override
    def solve_part_2(self) -> int:
        return self.run(True)
