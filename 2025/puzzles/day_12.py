from typing import override

from util.input import Input
from util.solver import Solver


class Day12(Solver):
    shape_sizes: list[int]
    regions: list[tuple[int, int, list[int]]]

    def __init__(self) -> None:
        blocks = Input(12).split_by_delimiter("\n\n")

        self.shape_sizes = [block.count("#") for block in blocks[:-1]]
        self.regions = []

        for line in blocks[-1].splitlines():
            dims, counts = line.split(": ")
            width, length = map(int, dims.split("x"))
            self.regions.append((width, length, list(map(int, counts.split()))))

    @override
    def solve_part_1(self) -> int:
        result = 0

        for width, length, counts in self.regions:
            if (width // 3) * (length // 3) >= sum(counts):
                result += 1
            elif sum(c * s for c, s in zip(counts, self.shape_sizes)) <= width * length:
                raise Exception(f"Region {width}x{length} needs a packing search")

        return result

    @override
    def solve_part_2(self) -> int:
        return 0
