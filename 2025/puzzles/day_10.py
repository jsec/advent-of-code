import re
from functools import cache
from itertools import combinations
from math import inf
from typing import override

from util.input import Input
from util.solver import Solver


class Day10(Solver):
    input: list[str]

    def __init__(self) -> None:
        self.input = Input(10).parse_as_lines()

    def parse_line(self, line: str):
        state_match = re.search(r"\[(.*?)\]", line)
        button_match = re.findall(r"\((\d+(?:,\d+)*)\)", line)
        joltage_match = re.search(r"\{([\d,]+)\}", line)

        desired_state = [c == "#" for c in state_match.group(1)] if state_match else []
        buttons = [list(map(int, b.split(","))) for b in button_match]

        joltages = (
            list(map(int, joltage_match.group(1).split(","))) if joltage_match else []
        )

        return desired_state, buttons, joltages

    def fewest_light_presses(self, desired_state: list[bool], buttons: list[list[int]]):
        for presses in range(len(buttons) + 1):
            for combo in combinations(buttons, presses):
                state = [False] * len(desired_state)
                for button in combo:
                    for light in button:
                        state[light] = not state[light]

                if state == desired_state:
                    return presses

        return 0

    def fewest_joltage_presses(self, buttons: list[list[int]], joltages: list[int]):
        patterns: list[tuple[list[int], int]] = []
        for presses in range(len(buttons) + 1):
            for combo in combinations(buttons, presses):
                added = [0] * len(joltages)
                for button in combo:
                    for counter in button:
                        added[counter] += 1
                patterns.append((added, presses))

        @cache
        def solve(target: tuple[int, ...]) -> float:
            if not any(target):
                return 0

            best = inf
            for added, presses in patterns:
                agg = zip(added, target)
                if all(a <= t and a % 2 == t % 2 for a, t in agg):
                    half = tuple((t - a) // 2 for a, t in agg)
                    best = min(best, presses + 2 * solve(half))

            return best

        return int(solve(tuple(joltages)))

    @override
    def solve_part_1(self) -> int:
        result = 0

        for line in self.input:
            desired_state, buttons, _ = self.parse_line(line)
            result += self.fewest_light_presses(desired_state, buttons)

        return result

    @override
    def solve_part_2(self) -> int:
        result = 0

        for line in self.input:
            _, buttons, joltages = self.parse_line(line)
            result += self.fewest_joltage_presses(buttons, joltages)

        return result
