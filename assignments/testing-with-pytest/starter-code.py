"""
Starter code for Unit Testing with Pytest assignment.
This module contains functions and classes to test, along with examples.
"""

# TODO: Install pytest if you haven't already
# Run: pip install pytest
# Then run tests with: pytest starter-code.py -v


# ============================================================================
# FUNCTIONS TO TEST
# ============================================================================

def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def divide(a, b):
    """Divide a by b. Raise ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


def remove_duplicates(items):
    """Remove duplicate items from a list, preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


class Calculator:
    """Simple calculator class for testing."""
    
    def __init__(self):
        self.result = 0
    
    def add(self, x):
        """Add x to the current result."""
        self.result += x
        return self.result
    
    def subtract(self, x):
        """Subtract x from the current result."""
        self.result -= x
        return self.result
    
    def reset(self):
        """Reset the result to zero."""
        self.result = 0


# ============================================================================
# EXAMPLE TESTS
# ============================================================================

def test_add_positive_numbers():
    """Test adding two positive numbers."""
    assert add(2, 3) == 5


def test_add_negative_numbers():
    """Test adding negative numbers."""
    assert add(-2, -3) == -5


def test_add_mixed_numbers():
    """Test adding positive and negative numbers."""
    assert add(5, -3) == 2


# TODO: Add more test functions for the add() function
# Test edge cases: zero, floats, large numbers


# TODO: Write test functions for divide()
# Remember to test for the ValueError when dividing by zero


# TODO: Write test functions for is_even()


# TODO: Write test functions for remove_duplicates()


# TODO: Write test functions for the Calculator class
# Test __init__, add(), subtract(), and reset()
