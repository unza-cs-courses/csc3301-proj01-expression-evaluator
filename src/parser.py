"""
Project 1: Expression Evaluator - Parser
Build an Abstract Syntax Tree from tokens.

Grammar:
  expr     -> term (('+' | '-') term)*
  term     -> factor (('*' | '/') factor)*
  factor   -> base ('^' factor)?          # Right associative
  base     -> NUMBER | IDENTIFIER | IDENTIFIER '(' args ')' | '(' expr ')' | '-' base
  args     -> expr (',' expr)*
"""
from dataclasses import dataclass
from typing import List, Union, Optional
from src.tokenizer import Token, TokenType, tokenize

# AST Node types
@dataclass
class NumberNode:
    value: float

@dataclass
class VariableNode:
    name: str

@dataclass
class BinaryOpNode:
    op: str
    left: 'ASTNode'
    right: 'ASTNode'

@dataclass
class UnaryOpNode:
    op: str
    operand: 'ASTNode'

@dataclass
class FunctionCallNode:
    name: str
    args: List['ASTNode']

ASTNode = Union[NumberNode, VariableNode, BinaryOpNode, UnaryOpNode, FunctionCallNode]

class Parser:
    """Recursive descent parser for expressions."""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self) -> ASTNode:
        """Parse tokens and return AST root."""
        # YOUR CODE HERE
        pass
    
    # Helper methods...

def parse(expression: str) -> ASTNode:
    """Parse expression string to AST."""
    tokens = tokenize(expression)
    parser = Parser(tokens)
    return parser.parse()
