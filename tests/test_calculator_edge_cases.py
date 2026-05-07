"""Additional edge-case tests for the demo calculator module."""

import pytest

from src.calculator import add, divide, subtract,power


def test_add_with_negative_numbers() -> None:
    assert add(-2, -3) == -5
    assert add(-2, 3) == 1


def test_subtract_to_zero() -> None:
    assert subtract(7, 7) == 0


def test_divide_with_fractional_result() -> None:
    assert divide(7, 2) == 3.5


def test_divide_zero_numerator() -> None:
    assert divide(0, 5) == 0.0


def test_divide_by_zero_message() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Made with Bob

def test_negative_base_fractional_exponent() -> None:
    with pytest.raises(ValueError, match="Negative base with fractional exponent not supported"):
        power(-2, 0.5)

def test_zero_to_negative_power() -> None:
    with pytest.raises(ValueError, match="Zero cannot be raised to a negative power"):
        power(0, -1)