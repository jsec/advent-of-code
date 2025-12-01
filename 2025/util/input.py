class Input:
    input: str

    def __init__(self, day: int) -> None:
        self.input = self.read_file(day)

    def read_file(self, day: int) -> str:
        with open(f"inputs/day_{day}.txt") as file:
            return file.read()

    def parse_as_lines(self) -> list[str]:
        return self.input.splitlines()

    def parse_as_grid(self) -> list[list[str]]:
        return [[char for char in line] for line in self.parse_as_lines()]

    def parse_as_number_grid(self) -> list[list[int]]:
        return [[int(char) for char in line] for line in self.parse_as_lines()]
