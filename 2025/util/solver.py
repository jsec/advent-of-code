from abc import ABC, abstractmethod


class Solver(ABC):
    @abstractmethod
    def solve_part_1(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def solve_part_2(self) -> int:
        raise NotImplementedError


def solve(solver: Solver) -> None:
    p1 = solver.solve_part_1()
    p2 = solver.solve_part_2()

    print("[PART 1] - ", p1)
    print("[PART 2] - ", p2)
