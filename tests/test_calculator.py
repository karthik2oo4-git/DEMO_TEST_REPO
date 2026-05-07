"""Tests for the demo calculator module."""

import pytest

from src.calculator import add, divide, subtract,power


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(10, 4) == 6


def test_divide() -> None:
    assert divide(12, 3) == 4

def test_power() -> None:
    assert power(2, 3) == 8

def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

# Made with Bob
