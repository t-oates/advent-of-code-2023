"""Day 1 of the Advent of Code 2023.

See https://adventofcode.com/2023/day/1
"""


import re


def solve(input_file: str, part: int = 1) -> int:
    """Solve day 01."""
    allow_strs = part == 2
    with open(input_file) as f:
        input_lines = f.readlines()
    return get_calibration_val_total(input_lines, allow_strs=allow_strs)


def get_calibration_val_total(input_lines: list[str],
                              allow_strs: bool = False) -> int:
    """Get sum of calibration values from all lines of input."""
    return sum(get_calibration_val(input_line, allow_strs=allow_strs)
               for input_line in input_lines)


def get_calibration_val(input_line: str, allow_strs: bool = False) -> int:
    """Get calibration value from a single line of input data."""

    # Create dict of {number as str: number as int}
    search_strs = {str(i): i for i in range(1, 10)}  # Single digit numbers
    if allow_strs:
        search_strs.update({'one': 1, 'two': 2, 'three': 3,
                            'four': 4, 'five': 5, 'six': 6,
                            'seven': 7, 'eight': 8, 'nine': 9})
    pattern = r'|'.join(search_strs.keys())

    first_num = search_strs[get_first_occurrence(input_line, pattern)]
    last_num = search_strs[get_last_occurrence(input_line, pattern)]

    return int(f'{first_num}{last_num}')


def get_first_occurrence(input_line, pattern):
    """Return first found value in input_line using regex"""
    nums_found = re.findall(pattern, input_line)
    return nums_found[0]


def get_last_occurrence(input_line, pattern):
    """Return last found value in input_line using regex"""
    # Simply search backwards. This takes into account edge cases like
    # 'oneight' that wouldn't work with a simple .findall()
    reversed_input = input_line[::-1]
    reversed_pattern = pattern[::-1]
    return get_first_occurrence(reversed_input, reversed_pattern)[::-1]


if __name__ == '__main__':
    print("Part 1:", solve('inputs/01.txt', part=1))
    print("Part 2:", solve('inputs/01.txt', part=2))
