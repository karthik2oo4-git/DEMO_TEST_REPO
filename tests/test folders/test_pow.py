import pytest

from src.calculator import power

def test_power() -> None:
    assert power(2, 3) == 9