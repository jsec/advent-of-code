from aocd import get_data


class Input:
    input: str

    def __init__(self, day: int, input: str | None) -> None:
        if input is None:
            self.input = get_data(day=day, year=2025)
        else:
            self.input = input

    def parse_as_lines(self) -> list[str]:
        return self.input.splitlines()

    def parse_as_grid(self) -> list[list[str]]:
        return [[char for char in line] for line in self.parse_as_lines()]

    def parse_as_number_grid(self) -> list[list[int]]:
        return [[int(char) for char in line] for line in self.parse_as_lines()]
