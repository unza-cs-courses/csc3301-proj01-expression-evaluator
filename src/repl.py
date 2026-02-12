#!/usr/bin/env python3
"""
Interactive REPL (Read-Eval-Print Loop) for the Expression Evaluator.
CSC3301 Programming Language Paradigms - Project 1

Usage (from repository root):
    python -m src.repl
"""
import sys
import os

# Ensure the repo root is on sys.path so `from src.…` imports work
# regardless of how the script is invoked.
_repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _repo_root not in sys.path:
    sys.path.insert(0, _repo_root)

from src.evaluator import evaluate


def repl():
    """
    Start an interactive REPL session.

    Commands:
        - Type an expression to evaluate it
        - Type 'quit' or 'exit' to end the session
        - Type 'help' for usage information
    """
    print("=" * 50)
    print("  Expression Evaluator REPL")
    print("  CSC3301 - Programming Language Paradigms")
    print("=" * 50)
    print("Type an expression to evaluate, or 'quit' to exit.")
    print("Example: 2 + 3 * 4")
    print()

    env = {}  # variable environment persists across the session

    while True:
        try:
            # Read
            user_input = input(">>> ").strip()

            # Handle special commands
            if not user_input:
                continue
            if user_input.lower() in ('quit', 'exit'):
                print("Goodbye!")
                break
            if user_input.lower() == 'help':
                print_help()
                continue

            # Eval  (evaluate already calls tokenize -> parse -> eval_node)
            result = evaluate(user_input, env)

            # Print
            print(f"= {result}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def print_help():
    """Print help information."""
    print("""
Supported Operations:
  - Arithmetic: +, -, *, /, ^ (power)
  - Parentheses: ( )
  - Functions: Based on your variant (check ASSIGNMENT.md)

Examples:
  >>> 2 + 3
  = 5.0
  >>> (2 + 3) * 4
  = 20.0
  >>> sqrt(16)
  = 4.0

Commands:
  help  - Show this help message
  quit  - Exit the REPL
  exit  - Exit the REPL
""")


if __name__ == "__main__":
    repl()
