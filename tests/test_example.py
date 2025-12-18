"""Example test module to demonstrate test structure.

This module serves as a template for writing tests for sailaps components.
"""

import pytest


class TestExample:
    """Example test class demonstrating pytest patterns."""

    def test_placeholder(self):
        """Placeholder test - replace with actual tests."""
        assert True

    def test_basic_assertion(self):
        """Example of a basic assertion."""
        result = 2 + 2
        assert result == 4

    @pytest.mark.parametrize("input_val,expected", [
        (1, 1),
        (2, 4),
        (3, 9),
    ])
    def test_parametrized(self, input_val, expected):
        """Example of parametrized tests."""
        result = input_val ** 2
        assert result == expected


def test_standalone_function():
    """Example standalone test function."""
    assert 1 == 1
