from collections import defaultdict
from typing import override
from util.solver import Solver
from util.input import Input

Beams = dict[int, int]


class Day7(Solver):
    rows: list[str]
    start: int

    def __init__(self) -> None:
        input = Input(7).parse_as_lines()
        self.start = input.pop(0).index("S")
        self.rows = [row for row in input if "^" in row]

    def traverse(self):
        result = 0
        beams: Beams = {self.start: 1}

        for row in self.rows:
            next: Beams = defaultdict(int)

            for idx, count in beams.items():
                if row[idx] == "^":
                    result += 1
                    next[idx - 1] += count
                    next[idx + 1] += count
                else:
                    next[idx] += count

            beams = next

        return result, beams

    @override
    def solve_part_1(self) -> int:
        result, _ = self.traverse()
        return result

    @override
    def solve_part_2(self) -> int:
        _, beams = self.traverse()
        result = sum(beams[idx] for idx in beams)
        return result
