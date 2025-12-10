from itertools import combinations, compress, starmap
from typing import override
from util.solver import Solver
from util.input import Input
from shapely import Polygon, box


class Day9(Solver):
    tiles: list[tuple[int, int]]

    def __init__(self) -> None:
        input = Input(9).parse_as_lines()
        self.tiles = [tuple(map(int, line.split(","))) for line in input]

    @override
    def solve_part_1(self) -> int:
        areas: list[int] = []

        for a, b in combinations(self.tiles, 2):
            if a[0] == b[0] or a[1] == b[1]:
                continue

            area = (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)
            areas.append(area)

        return max(areas)

    @override
    def solve_part_2(self) -> int:
        boxes = [
            (min(a, c), min(b, d), max(a, c), max(b, d))
            for (a, b), (c, d) in combinations(self.tiles, 2)
        ]

        areas = [(c - a + 1) * (d - b + 1) for (a, b, c, d) in boxes]

        p = Polygon(self.tiles)
        valid_areas = compress(areas, map(p.contains, starmap(box, boxes)))
        return max(valid_areas)
