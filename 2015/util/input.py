import os

def get_input() -> str:
    with open(os.environ["AOC_INPUT"]) as file:
        return file.read().strip()


def get_input_lines() -> list[str]:
    with open(os.environ["AOC_INPUT"]) as file:
        return [line.strip() for line in file.readlines()]


def get_split_input(delimiter: str) -> list[str]:
    with open(os.environ["AOC_INPUT"]) as file:
        return file.read().split(delimiter)
