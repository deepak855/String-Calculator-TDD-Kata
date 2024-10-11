# String Calculator TDD Kata

## Requirements:
- Python 3.x
- pytest (for running tests)

## Instructions to Run the Code:

1. Clone the repository:
    ```bash
    git clone https://github.com/deepak855/String-Calculator-TDD-Kata.git
    cd string-calculator
    ```

2. Install pytest for running the tests:
    ```bash
    pip install pytest
    ```

3. Run the tests:
    ```bash
    pytest
    ```

4. The `add` function is defined to take a string of comma-separated numbers and return their sum. Example:
    ```python
    from string_calculator import add

    result = add("1,2,3")
    print(result)  # Output: 6
    ```

## Features:
- Handles empty string input and returns `0`.
- Handles single or multiple numbers separated by commas.
- Allows newlines between numbers (e.g., `"1\n2,3"`).
- Supports custom delimiters defined in the input string (e.g., `"//;\n1;2"`).
- Throws an exception for negative numbers, showing all negative numbers in the error message.

## Commit History:
This project follows TDD principles with frequent commits to highlight each step in the development process. Please refer to the commit history for a step-by-step evolution of the solution.
