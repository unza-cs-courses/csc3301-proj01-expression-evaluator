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

## Your Variant

Run `python scripts/show_variant.py` to see your personalized requirements.

Your variant includes:
- **Required functions:** Subset of {sqrt, abs, sin, cos, tan, log, exp, floor, ceil}
- **Test constants:** Numbers used in hidden tests
- **Precision:** Decimal places for comparison

---

## Project Structure

```
├── src/
│   ├── tokenizer.py      # Lexical analysis
│   ├── parser.py         # Syntax analysis → AST
│   ├── evaluator.py      # AST evaluation
│   └── repl.py           # Interactive mode
├── tests/
│   └── test_evaluator.py
├── scripts/
│   ├── generate_variant.py
│   └── show_variant.py
└── variant.json
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
2. Ensure tests pass: `pytest tests/ -v`
3. Fill out `SUBMISSION.md`
4. Create final tag: `git tag final-submission && git push --tags`

---

## Academic Integrity

- Discuss concepts with classmates ✓
- Use Python documentation ✓
- Use parsing tutorials/concepts ✓
- Share or copy code ✗
- Use AI to generate solutions ✗
