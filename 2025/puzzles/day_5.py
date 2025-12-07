from typing import NamedTuple, override
from util.input import Input
from util.solver import Solver
from intervaltree import IntervalTree  # pyright: ignore[reportMissingTypeStubs]


class Range(NamedTuple):
    min: int
    max: int


class Day5(Solver):
    ranges: list[Range]
    ingredients: list[int]

    def __init__(self) -> None:
        self.ranges = []

        ranges, ingredients = Input(5).split_by_delimiter("\n\n")
        ranges = ranges.split("\n")
        self.ingredients = [int(x) for x in ingredients.strip().split("\n")]

        for range in ranges:
            min, max = range.strip().split("-")
            self.ranges.append(Range(int(min), int(max) + 1))

    @override
    def solve_part_1(self) -> int:
        result = 0

        for ingredient in self.ingredients:
            if any(
                range.min <= ingredient and range.max >= ingredient
                for range in self.ranges
            ):
                result += 1

        return result

    @override
    def solve_part_2(self) -> int:
        tree = IntervalTree.from_tuples(self.ranges)
        tree.merge_overlaps()

        return sum([r.end - r.begin for r in tree.items()])
