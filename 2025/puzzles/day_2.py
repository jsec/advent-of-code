from re import match
from typing import override
from util.input import Input
from util.solver import Solver


class Day2(Solver):
    ranges: list[tuple[int, int]]

    def __init__(self) -> None:
        self.ranges = []

        input = Input(2).split_by_delimiter(",")
        for i in input:
            [x, y] = i.strip().split("-")
            self.ranges.append((int(x), int(y)))

    @override
    def solve_part_1(self) -> int:
        result = 0

        for low, high in self.ranges:
            for value in range(low, high + 1):
                string = str(value)
                length = len(string)
                if length % 2 != 0:
                    continue

                q, r = divmod(length, 2)
                first, second = string[: q + r], string[q + r :]
                if first == second:
                    result += value

        return result

    @override
    def solve_part_2(self) -> int:
        result = 0

        for low, high in self.ranges:
            for value in range(low, high + 1):
                if match(r"^(\d+)\1+$", str(value)):
                    result += value

        return result
