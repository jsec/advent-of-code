from abc import ABC, abstractmethod


class Solver(ABC):
    def solve(self):
        p1 = self.solve_part_1()
        p2 = self.solve_part_2()

        print("[PART 1] - ", p1)
        print("[PART 2] - ", p2)

    @abstractmethod
    def solve_part_1(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def solve_part_2(self) -> int:
        raise NotImplementedError
