from sys import argv, exit
from solution import part_one, part_two


def parse_puzzle_input(file: str) -> list:
    """Parse the puzzle input so that each line is an element in a list.
    Then return the list."""
    with open(file) as f:
        return [int(line) for line in f]


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: solution.py <puzzle input file>")
        exit(1)

    input = parse_puzzle_input(argv[1])

    print(
        f"""
    Answers:
    Part one: {part_one(input)}
    Part two: {part_two(input)}
    """
    )
