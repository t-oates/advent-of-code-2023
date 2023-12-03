import pytest

import day02


with open('tests/inputs/02.txt') as f:
    TEST_INPUT_LINES = f.readlines()


def test_parse_input_line():
    input_line = TEST_INPUT_LINES[0]
    handfuls = [{'blue': 3, 'red': 4},
                {'red': 1, 'green': 2, 'blue': 6},
                {'green': 2}]
    assert day02.parse_input_line(input_line) == handfuls


@pytest.mark.parametrize(
    'input_line, power',
    [(TEST_INPUT_LINES[1], 12),
     (TEST_INPUT_LINES[2], 1560),
     (TEST_INPUT_LINES[3], 630),
     (TEST_INPUT_LINES[4], 36)]
)
def test_get_game_power(input_line, power):
    handfuls = day02.parse_input_line(input_line)
    assert day02.get_game_power(handfuls) == power


@pytest.mark.parametrize(
    'input_line, min_cubes',
    [(TEST_INPUT_LINES[0], (4, 2, 6)),
     (TEST_INPUT_LINES[1], (1, 3, 4)),
     (TEST_INPUT_LINES[2], (20, 13, 6)),
     (TEST_INPUT_LINES[3], (14, 3, 15)),
     (TEST_INPUT_LINES[4], (6, 3, 2))]
)
def test_get_min_required_cubes(input_line, min_cubes):
    handfuls = day02.parse_input_line(input_line)
    assert day02.get_min_required_cubes(handfuls) == min_cubes
