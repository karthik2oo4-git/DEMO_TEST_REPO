"""Regression-style tests for baseline calculator behavior."""

from src.calculator import add, divide, subtract


def test_add_zero_identity() -> None:
    assert add(0, 9) == 9
    assert add(9, 0) == 9


def test_subtract_negative_result() -> None:
    assert subtract(4, 10) == 40


def test_divide_negative_values() -> None:
    assert divide(-12, 3) == -4.0
    assert divide(12, -3) == -4.0

# Made with Bob
