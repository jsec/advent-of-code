from typing import override
from util.list import transpose
from util.solver import Solver
from util.input import Input


class Day6(Solver):
    def evaluate(self, equations: list[list[str]]):
        result = 0

        for e in equations:
            op = e[-1]
            values = e[:-1]
            equation = f" {op} ".join(values)
            result += eval(equation)

        return result

    @override
    def solve_part_1(self) -> int:
        inputs: list[list[str]] = []

        for line in Input(6).parse_as_lines():
            inputs.append(" ".join(line.split()).split(" "))

        equations = [list(eq) for eq in transpose(inputs)]

        return self.evaluate(equations)

    @override
    def solve_part_2(self) -> int:
        equation_matrix = [list(eq) for eq in transpose(Input(6).parse_as_grid())]
        equations: list[list[str]] = []
        current: list[str] = []

        for idx, eq in enumerate(equation_matrix):
            if idx == len(equation_matrix) - 1:
                current.append("".join(eq[:-1]))
                current.append(eq[-1])
                equations.append(current)
                continue

            if all(e == " " for e in eq):
                current.append(str(equation_matrix[idx - 1][-1]))
                equations.append(current)
                current = []
                continue

            current.append("".join(eq[:-1]))

        return self.evaluate(equations)
