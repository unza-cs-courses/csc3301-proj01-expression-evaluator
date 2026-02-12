# Project 1: Expression Evaluator

**CSC3301 Programming Language Paradigms**
**Weight:** 3% of final grade
**Duration:** 2 weeks

---

## Overview

Build a mathematical expression evaluator that parses and evaluates arithmetic expressions. This project establishes Python foundations including parsing, recursion, data structures, and testing.

---

## Learning Outcomes

1. Implement recursive descent parsing in Python
2. Design and use appropriate data structures (AST)
3. Handle errors gracefully with meaningful messages
4. Write comprehensive unit tests
5. Follow Python style conventions (PEP 8)

---

## Getting Started

### For Students (via GitHub Classroom)

When you accept this assignment, a unique variant is automatically generated for you:

1. A GitHub Actions workflow automatically generates `variant.json` and `ASSIGNMENT.md` on first push
2. Check `ASSIGNMENT.md` for your specific requirements (generated after first push)
3. Your code must implement the functions specified in your variant

### Manual Setup (Instructors/Testing)

```bash
# Clone the repository
git clone <repo-url>
cd csc3301-proj01-expression-evaluator

# Install dependencies
pip install -r requirements.txt

# Generate a variant manually (optional)
python scripts/generate_variant.py <student_id>

# Run tests
pytest tests/visible/ -v
```

---

## Variant System

Each student receives a unique variant generated from their student ID. The variant determines:

| Parameter | Description | Range |
|-----------|-------------|-------|
| `required_functions` | Functions to implement | 4-6 from {sqrt, abs, sin, cos, tan, log, exp, floor, ceil} |
| `test_constants` | Test values | 3 random values between 1-100 |
| `precision` | Decimal accuracy | 4, 5, or 6 decimal places |

### Viewing Your Variant

```bash
# Show your current variant
python scripts/show_variant.py

# Or check variant.json / .variant_config.json directly
```

### Variant Generation

The variant is generated deterministically using a hash of your student ID:

```python
seed = hash(f"{student_id}-P1-CSC3301-2026")
```

This ensures:
- Same student always gets same variant
- Different students get different variants
- Instructors can reproduce any student's variant

---

## Requirements

Your expression evaluator must:

1. Parse arithmetic expressions with `+`, `-`, `*`, `/`, `^` (power)
2. Respect operator precedence: `^` > `*,/` > `+,-`
3. Handle parentheses for grouping
4. Support floating-point and negative numbers
5. Support variables (single letters a-z) with a provided environment
6. Implement functions from your variant (see `variant.json`)
7. Return meaningful error messages for invalid expressions
8. Provide a REPL interface

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
└── README.md                       # This file
```

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

# Functions (if in your variant)
evaluate("sqrt(16) + abs(-5)")  # Returns 9.0
```

---

## Running Tests

```bash
# Run all visible tests
pytest tests/visible/ -v

# Run tests for a specific class
pytest tests/visible/test_evaluator.py::TestBasicArithmetic -v
pytest tests/visible/test_evaluator.py::TestVariables -v
pytest tests/visible/test_evaluator.py::TestFunctions -v
```

**Note:** Visible tests run on every push. Hidden tests with additional edge cases will run after the submission deadline.

---

## Grading

| Component | Points | When |
|-----------|--------|------|
| Visible Tests | 40 | Every push |
| Hidden Tests | 30 | After deadline |
| Code Quality | 20 | Manual review |
| Process | 10 | Milestone compliance |
| **Total** | 100 | |

### Component Breakdown

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

---

## Academic Integrity

- Discuss concepts with classmates (allowed)
- Use Python documentation (allowed)
- Use parsing tutorials/concepts (allowed)
- Share or copy code (NOT ALLOWED)
- Use AI to generate solutions (NOT ALLOWED)

Your submission will be checked for similarity with other students using automated plagiarism detection.
