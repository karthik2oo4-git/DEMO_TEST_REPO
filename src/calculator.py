"""Simple calculator module for PR validation demo."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a+b


def subtract(a: int, b: int) -> int:
    """Return the difference of two integers."""
    return a - b


def divide(a: int, b: int) -> float:
    """Return the division result.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Made with Bob
