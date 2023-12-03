import pytest

import day01


def test_get_calibration_value_total():
    input_lines = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    assert day01.get_calibration_val_total(input_lines) == 142


@pytest.mark.parametrize(
    'input_line, calibration_val',
    [('1abc2', 12),
     ('pqr3stu8vwx', 38),
     ('a1b2c3d4e5f', 15),
     ('treb7uchet', 77)]
)
def test_get_calibration_value(input_line, calibration_val):
    assert day01.get_calibration_val(input_line) == calibration_val


def test_get_calibration_value_total_with_strs():
    input_lines = ['two1nine', 'eightwothree', 'abcone2threexyz',
                   'xtwone3four', '4nineeightseven2', 'zoneight234',
                   '7pqrstsixteen']
    assert day01.get_calibration_val_total(input_lines, allow_strs=True) == 281


@pytest.mark.parametrize(
    'input_line, calibration_val',
    [('two1nine', 29),
     ('eightwothree', 83),
     ('abcone2threexyz', 13),
     ('xtwone3four', 24),
     ('4nineeightseven2', 42),
     ('zoneight234', 14),
     ('7pqrstsixteen', 76)]
)
def test_get_calibration_value_with_strs(input_line, calibration_val):
    assert day01.get_calibration_val(input_line, allow_strs=True) == calibration_val
