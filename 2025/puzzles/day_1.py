from typing import override
from util.input import Input
from util.solver import Solver


class Day1(Solver):
    rotations: list[str]

    def __init__(self) -> None:
        super().__init__()
        self.rotations = Input(1).parse_as_lines()

    def puzzle(self):
        idx = 50
        part1 = 0
        part2 = 0

        for rotation in self.rotations:
            direction = rotation[0]
            amount = int(rotation[1:])

            for _ in range(amount):
                if direction == "R":
                    idx = (idx + 1) % 100
                else:
                    idx = (idx - 1 + 100) % 100

                if idx == 0:
                    part2 += 1

            if idx == 0:
                part1 += 1

        return (part1, part2)

    @override
    def solve_part_1(self) -> int:
        part1, _ = self.puzzle()
        return part1

    @override
    def solve_part_2(self) -> int:
        _, part2 = self.puzzle()
        return part2
