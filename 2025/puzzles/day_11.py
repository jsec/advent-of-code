from typing import override
from util.solver import Solver
from util.input import Input
from functools import cache


class Day11(Solver):
    nodes: dict[str, list[str]]

    def __init__(self) -> None:
        self.nodes = dict()
        input = Input(11).parse_as_lines()

        for line in input:
            node, connections = line.split(":")
            self.nodes[node] = connections.strip().split()

    @cache
    def traverse(self, node: str, dac: bool, fft: bool):
        match node:
            case "out":
                return 1 if (dac and fft) else 0
            case "dac":
                dac = True
            case "fft":
                fft = True
            case _:
                pass

        return sum(self.traverse(conn, dac, fft) for conn in self.nodes[node])

    @override
    def solve_part_1(self) -> int:
        return self.traverse("you", True, True)

    @override
    def solve_part_2(self) -> int:
        return self.traverse("svr", False, False)
