from typing import override
from util.grid import Grid
from util.solver import Solver
from util.input import Input


class Day4(Solver):
    input: list[list[str]]
    grid: Grid

    def __init__(self) -> None:
        self.input = Input(4).parse_as_grid()
        self.grid = Grid(self.input)

    def plot(self):
        result = 0
        rolls: list[tuple[int, int]] = []

        for ix, row in enumerate(self.grid.data):
            for iy, value in enumerate(row):
                if value != "@":
                    continue

                adjacent_rolls = list(
                    filter(
                        lambda n: self.grid.at(n[0], n[1]) == "@",
                        self.grid.neighbors(ix, iy),
                    )
                )

                if len(adjacent_rolls) < 4:
                    result += 1
                    rolls.append((ix, iy))

        for roll in rolls:
            self.grid.set(roll[0], roll[1], "x")

        return result

    @override
    def solve_part_1(self) -> int:
        return self.plot()

    @override
    def solve_part_2(self) -> int:
        self.grid = Grid(self.input)
        result = 0

        while True:
            count = self.plot()

            if count == 0:
                break

            result += count

        return result
