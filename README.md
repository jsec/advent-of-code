# Advent of Code 

My collection of solutions for Advent of Code puzzles.

Some of them have been cleaned up and optimized. Some are ugly and convoluted. I use these exercises to experiment with algorithms and languages I need to shake the rust off of, or that I haven't gotten to learn yet, so YMMV as to the quality of the solutions.

## Year (Language) - Stars Received
- 2025 (Python) - 24
- 2024 (TypeScript) - 50
- 2023 (Python) - 50
- 2022 (TypeScript) - 18
- 2021 (JavaScript) - 22
- 2020 (Go) - 11
- 2019 (TypeScript) - 15
- 2018 (JavaScript) - 22
- 2017 (Python) - 26
- 2016 (TypeScript) - 29
- 2015 (Python) - 34

## Running

Setup, once:

```bash
mise install
uv sync
pnpm install
echo "AOC_SESSION=<your adventofcode.com session cookie>" > .env
```

Run a day (downloads its input to `inputs/YYYY/day_NN.txt` the first time):

```bash
mise run day 2024 5
```

Start a new day from a template (`--lang py|ts`, defaults to `py`):

```bash
mise run new 2026 1 --lang ts
```

New days import shared helpers from `lib/py/aoc` (`from aoc import Input, Solver`) or `lib/ts` (`import { getInputLines } from '#lib/input'`).
