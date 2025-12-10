from itertools import combinations
from typing import override
from util.solver import Solver
from util.input import Input


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
        return 0
