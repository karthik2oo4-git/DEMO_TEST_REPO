"""Standalone demo runner for the PR validation sample repository."""

from __future__ import annotations

from src.calculator import add, divide, subtract


def main() -> None:
    print("=== Demo Test Repository Runner ===")
    print("This script shows baseline behavior for the demo repository.")
    print()

    print("[1] Running sample calculator operations")
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"divide(12, 3) = {divide(12, 3)}")
    print()

    print("[2] Demonstrating expected guarded failure")
    try:
        divide(5, 0)
    except ValueError as exc:
        print(f"divide(5, 0) raised ValueError as expected: {exc}")
    print()

    print("[3] Demo guidance")
    print("- Baseline tests in the base branch should keep passing on PR branches.")
    print("- New functions added in a PR should also include new tests.")
    print("- Use this repository to simulate pass, fail, and missing-test scenarios.")
    print()

    print("=== Demo complete ===")


if __name__ == "__main__":
    main()

# Made with Bob
