# Project 1: Expression Evaluator

**CSC3301 Programming Language Paradigms**
**Student ID:** {{STUDENT_ID}}
**Weight:** 3% of final grade
**Duration:** 2 weeks

---

## Your Unique Variant

This assignment has been personalized for you. Your specific requirements are:

### Required Functions

Your expression evaluator must support these functions:

{{REQUIRED_FUNCTIONS_LIST}}

### Test Constants

Your implementation will be tested with these values:
- Constant 1: `{{TEST_CONSTANT_1}}`
- Constant 2: `{{TEST_CONSTANT_2}}`
- Constant 3: `{{TEST_CONSTANT_3}}`

### Precision Requirement

Your calculations must be accurate to **{{PRECISION}} decimal places**.

Tolerance: `{{TOLERANCE}}`

**Important:** Your code must produce results matching these exact specifications to pass the tests.

---

## Overview

Build a mathematical expression evaluator that parses and evaluates arithmetic expressions. This project establishes Python foundations including parsing, recursion, data structures, and testing.

---

## Requirements

Your expression evaluator must:

1. Parse arithmetic expressions with `+`, `-`, `*`, `/`, `^` (power)
2. Respect operator precedence: `^` > `*,/` > `+,-`
3. Handle parentheses for grouping
4. Support floating-point and negative numbers
5. Support variables (single letters a-z) with a provided environment
6. Implement the required functions listed above
7. Return meaningful error messages for invalid expressions
8. Provide a REPL interface

---

## Example Usage

```python
from src.evaluator import evaluate

# Basic arithmetic
evaluate("2 + 3 * 4")  # Returns 14.0

# Parentheses
evaluate("(2 + 3) * 4")  # Returns 20.0

# Variables
evaluate("x + y * 2", {"x": 3, "y": 4})  # Returns 11.0

# Functions (examples from your variant)
evaluate("sqrt({{TEST_CONSTANT_1}})")  # Returns sqrt of your test constant
evaluate("abs(-{{TEST_CONSTANT_2}})")  # Returns {{TEST_CONSTANT_2}}
```

---

## Milestones

| Milestone | Due | Deliverables | Weight |
|-----------|-----|--------------|--------|
| M1 | Week 2, Day 3 | Tokenizer complete | 20% |
| M2 | Week 2, Day 7 | Parser builds correct AST | 30% |
| M3 | Week 3, Day 3 | Full evaluation with variables | 30% |
| Final | Week 3, Day 7 | Complete with tests | 20% |

**Tag milestones:** `git tag milestone-1 && git push --tags`

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       ├── autograding.yml         # Runs visible tests
│       └── generate-variant.yml    # Generates student variant
├── scripts/
│   ├── generate_variant.py         # Creates unique test values
│   ├── generate_assignment.py      # Creates personalized ASSIGNMENT.md
│   └── show_variant.py             # Display current variant
├── src/
│   ├── tokenizer.py      # Lexical analysis
│   ├── parser.py         # Syntax analysis -> AST
│   ├── evaluator.py      # AST evaluation
│   └── repl.py           # Interactive mode
├── tests/
│   └── visible/
│       ├── conftest.py             # Loads variant config
│       └── test_evaluator.py       # Visible test suite
├── .variant_config.json            # Your unique test values (generated)
├── ASSIGNMENT.md                   # Your personalized assignment (generated)
├── ASSIGNMENT_TEMPLATE.md          # Template for generating ASSIGNMENT.md
├── variant.json                    # Your variant config
└── README.md                       # Project documentation
```

---

## Running Tests

```bash
# Run visible tests (these are what you see)
pytest tests/visible/ -v

# Run a specific test class
pytest tests/visible/test_evaluator.py::TestBasicArithmetic -v
pytest tests/visible/test_evaluator.py::TestVariables -v
pytest tests/visible/test_evaluator.py::TestFunctions -v
```

---

## Grading

| Component | Points |
|-----------|--------|
| Tokenizer | 15% |
| Parser | 25% |
| Evaluator | 25% |
| Error handling | 10% |
| Testing | 10% |
| Code quality | 10% |
| Process | 5% |

---

## Submission

1. Complete all components in `src/`
2. Ensure tests pass: `pytest tests/visible/ -v`
3. Fill out `SUBMISSION.md`
4. Create final tag: `git tag final-submission && git push --tags`

**Note:** Hidden tests will run after the deadline to verify additional edge cases.

---

## Academic Integrity

- Discuss concepts with classmates
- Use Python documentation
- Use parsing tutorials/concepts
- Share or copy code (NOT ALLOWED)
- Use AI to generate solutions (NOT ALLOWED)

Your submission will be checked for similarity with other students using automated plagiarism detection.
