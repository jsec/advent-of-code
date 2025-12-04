from typing import override
from util.input import Input
from util.solver import Solver


class Day3(Solver):
    banks: list[str]

    def __init__(self) -> None:
        self.banks = Input(3).parse_as_lines()

    def get_joltage(self, bank: str, size: int, result: list[str]) -> int:
        if size == 1:
            result.append(max(bank))
            return int("".join(result))

        next = max(bank[0 : -size + 1])
        idx = bank.index(next)
        result.append(next)

        return self.get_joltage(bank[idx + 1 :], size - 1, result)

    @override
    def solve_part_1(self) -> int:
        result = 0
        for bank in self.banks:
            result += self.get_joltage(bank, 2, [])

        return result

    @override
    def solve_part_2(self) -> int:
        result = 0
        for bank in self.banks:
            result += self.get_joltage(bank, 12, [])

        return result
