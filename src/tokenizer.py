"""
Project 1: Expression Evaluator - Tokenizer
Convert expression string to list of tokens.
"""
from enum import Enum, auto
from dataclasses import dataclass
from typing import List

class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    CARET = auto()
    LPAREN = auto()
    RPAREN = auto()
    IDENTIFIER = auto()
    COMMA = auto()
    EOF = auto()

@dataclass
class Token:
    type: TokenType
    value: str
    position: int

def tokenize(expression: str) -> List[Token]:
    """
    Convert expression string to list of tokens.
    
    Args:
        expression: Mathematical expression string
    
    Returns:
        List of Token objects
    
    Raises:
        SyntaxError: For unexpected characters
    """
    # YOUR CODE HERE
    pass

if __name__ == "__main__":
    tokens = tokenize("2 + 3 * (4 - 1)")
    for t in tokens:
        print(t)
