"""
Project 1: Expression Evaluator - Evaluator
Evaluate AST to produce a result.
"""
import math
import json
from typing import Dict, Optional
from src.parser import parse, ASTNode, NumberNode, VariableNode, BinaryOpNode, UnaryOpNode, FunctionCallNode

# Load variant for required functions
def load_variant():
    try:
        with open('variant.json') as f:
            return json.load(f)
    except:
        return {'required_functions': ['sqrt', 'abs']}

VARIANT = load_variant()

# Built-in functions
FUNCTIONS = {
    'sqrt': math.sqrt,
    'abs': abs,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'log': math.log,
    'exp': math.exp,
    'floor': math.floor,
    'ceil': math.ceil,
}

def evaluate(expression: str, env: Optional[Dict[str, float]] = None) -> float:
    """
    Evaluate a mathematical expression.
    
    Args:
        expression: Expression string
        env: Variable bindings (e.g., {"x": 5, "y": 10})
    
    Returns:
        Evaluation result as float
    
    Raises:
        ValueError: For undefined variables
        SyntaxError: For invalid expressions
    """
    if env is None:
        env = {}
    
    ast = parse(expression)
    return eval_node(ast, env)

def eval_node(node: ASTNode, env: Dict[str, float]) -> float:
    """Recursively evaluate an AST node."""
    # YOUR CODE HERE
    pass

if __name__ == "__main__":
    print(evaluate("2 + 3 * 4"))  # 14.0
    print(evaluate("(2 + 3) * 4"))  # 20.0
    print(evaluate("x + y", {"x": 1, "y": 2}))  # 3.0
