#!/usr/bin/env python3
"""
Interactive REPL (Read-Eval-Print Loop) for the Expression Evaluator.
CSC3301 Programming Language Paradigms - Project 1

This module provides an interactive mode for testing your evaluator.
"""
from tokenizer import tokenize
from parser import parse
from evaluator import evaluate


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
            
            # Eval
            tokens = tokenize(user_input)
            ast = parse(tokens)
            result = evaluate(ast)
            
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
  = 5
  >>> (2 + 3) * 4
  = 20
  >>> sqrt(16)
  = 4.0
  
Commands:
  help  - Show this help message
  quit  - Exit the REPL
  exit  - Exit the REPL
""")


if __name__ == "__main__":
    repl()
