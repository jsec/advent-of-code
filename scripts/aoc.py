"""Run or create Advent of Code solutions.

Usage:
    aoc.py day YEAR DAY              Run YEAR/day_NN.*, downloading its input first if needed.
    aoc.py new YEAR DAY [--lang ts]  Create YEAR/day_NN.{py,ts} from templates/.
"""

import os
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path

from aocd import get_data
from aocd.exceptions import AocdError

REPO_ROOT = Path(__file__).resolve().parent.parent
INPUTS_DIR = REPO_ROOT / "inputs"
TEMPLATES_DIR = REPO_ROOT / "templates"

RUNNERS: dict[str, list[str]] = {
    ".py": [sys.executable],
    ".ts": ["pnpm", "tsx"],
    ".js": ["pnpm", "tsx"],
}


class AocError(Exception):
    """An error that ``main`` prints as a one-line message instead of a traceback."""


def day_name(day: int) -> str:
    """Return a day's file name without the extension, e.g. ``day_05`` for day 5."""
    return f"day_{day:02}"


def existing_solutions(year: int, day: int) -> list[Path]:
    """Return every solution file for a day, in any language."""
    return sorted((REPO_ROOT / str(year)).glob(f"{day_name(day)}.*"))


def find_solution(year: int, day: int) -> Path:
    """Return the one solution file for a day.

    Raises:
        AocError: If the day has no solution file, or more than one.
    """
    solutions = existing_solutions(year, day)
    if not solutions:
        raise AocError(f"no solution file for {year}/{day_name(day)}")
    if len(solutions) > 1:
        names = ", ".join(path.name for path in solutions)
        raise AocError(f"{year}/{day_name(day)} has more than one solution file: {names}")
    return solutions[0]


def ensure_input(year: int, day: int) -> Path:
    """Return the path to a day's puzzle input, downloading it if missing.

    If the download fails, for example because the session cookie is invalid or the
    puzzle is not unlocked yet, no input file is created.
    """
    input_path = INPUTS_DIR / str(year) / f"{day_name(day)}.txt"
    if not input_path.exists():
        try:
            data = get_data(day=day, year=year)
        except AocdError as error:
            raise AocError(f"could not download {year}/{day_name(day)} input: {error}") from error
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.write_text(data)
    return input_path


def run_day(year: int, day: int) -> int:
    """Run a day's solution with ``AOC_INPUT`` set to its input file's path, and return its exit code.

    Raises:
        AocError: If the day has no solution file, more than one, or one whose extension has no entry in ``RUNNERS``.
    """
    solution = find_solution(year, day)
    runner = RUNNERS.get(solution.suffix)
    if runner is None:
        raise AocError(f"no runner for {solution.suffix} files")

    input_path = ensure_input(year, day)
    completed = subprocess.run(
        [*runner, str(solution)],
        cwd=REPO_ROOT,
        env={**os.environ, "AOC_INPUT": str(input_path)},
        check=False,
    )
    return completed.returncode


def new_day(year: int, day: int, lang: str) -> Path:
    """Create a day's solution file from ``templates/day.<lang>`` and return its path.

    Raises:
        AocError: If the day already has a solution file in any language.
    """
    existing = existing_solutions(year, day)
    if existing:
        raise AocError(f"{existing[0].relative_to(REPO_ROOT)} already exists")

    template = (TEMPLATES_DIR / f"day.{lang}").read_text()
    solution = REPO_ROOT / str(year) / f"{day_name(day)}.{lang}"
    solution.parent.mkdir(exist_ok=True)
    solution.write_text(template.replace("__DAY__", str(day)))
    return solution


def build_parser() -> ArgumentParser:
    """Build the parser for the ``day`` and ``new`` subcommands."""
    puzzle_args = ArgumentParser(add_help=False)
    puzzle_args.add_argument("year", type=int)
    puzzle_args.add_argument("day", type=int)

    parser = ArgumentParser(description="Run or create Advent of Code solutions.")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("day", parents=[puzzle_args], help="run a day's solution")
    new_command = commands.add_parser("new", parents=[puzzle_args], help="create a day from a template")
    new_command.add_argument("--lang", choices=["py", "ts"], default="py")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse arguments, run the chosen command, and return the exit code."""
    args = build_parser().parse_args(argv)
    try:
        if args.command == "day":
            return run_day(args.year, args.day)
        solution = new_day(args.year, args.day, args.lang)
    except AocError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"created {solution.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
