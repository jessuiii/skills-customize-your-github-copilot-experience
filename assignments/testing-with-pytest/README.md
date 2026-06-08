# 📘 Assignment: Unit Testing with Pytest

## 🎯 Objective

Learn to write automated unit tests using pytest to validate your code, catch bugs early, and build confidence in your implementations. You'll practice writing test cases, using assertions, and organizing tests for maintainability.

## 📝 Tasks

### 🛠️ Write Basic Test Functions

#### Description

Create test functions that validate the behavior of simple functions. Use pytest assertions to verify expected outputs and understand how tests catch bugs.

#### Requirements

Completed program should:

- Import pytest and the functions to be tested
- Write multiple test functions with descriptive names (test_function_does_something)
- Use assert statements to verify function outputs
- Test both expected success cases and edge cases (empty input, zero, None)
- Run tests with pytest and verify all tests pass

---

### 🛠️ Test Multiple Scenarios and Error Cases

#### Description

Expand test coverage to include testing for exceptions, multiple input scenarios, and boundary conditions. Use pytest features to organize related tests.

#### Requirements

Completed program should:

- Write tests that verify functions raise appropriate exceptions for invalid inputs
- Test functions with multiple input combinations (parametrized tests or multiple assertions)
- Test boundary conditions and edge cases (empty strings, negative numbers, etc.)
- Use clear test organization with logical grouping
- Achieve 80%+ test coverage of the target code

---

### 🛠️ Test Classes and Complex Objects

#### Description

Write tests for class methods and complex objects. Practice testing state changes and method interactions.

#### Requirements

Completed program should:

- Write test functions that validate class initialization and attributes
- Test class methods that modify state
- Test interaction between multiple methods
- Use test fixtures for setup and teardown if needed
- Document test purpose with clear function names and assertions
