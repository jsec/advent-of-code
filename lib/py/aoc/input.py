import os


class Input:
    input: str

    def __init__(self) -> None:
        with open(os.environ["AOC_INPUT"]) as file:
            self.input = file.read()

    def parse_as_lines(self) -> list[str]:
        return self.input.splitlines()

    def parse_as_grid(self) -> list[list[str]]:
        return [list(line) for line in self.parse_as_lines()]

    def parse_as_number_grid(self) -> list[list[int]]:
        return [[int(char) for char in line] for line in self.parse_as_lines()]

    def split_by_delimiter(self, delimiter: str) -> list[str]:
        return self.input.split(delimiter)
