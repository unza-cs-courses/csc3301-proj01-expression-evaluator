"""Public tests for Expression Evaluator."""
import pytest
from src.evaluator import evaluate

class TestBasicArithmetic:
    def test_addition(self):
        assert evaluate("2 + 3") == 5.0
    
    def test_multiplication(self):
        assert evaluate("4 * 5") == 20.0
    
    def test_precedence(self):
        assert evaluate("2 + 3 * 4") == 14.0
    
    def test_parentheses(self):
        assert evaluate("(2 + 3) * 4") == 20.0

class TestVariables:
    def test_single_variable(self):
        assert evaluate("x", {"x": 5}) == 5.0
    
    def test_expression_with_variables(self):
        assert evaluate("x + y * 2", {"x": 3, "y": 4}) == 11.0

class TestFunctions:
    def test_sqrt(self):
        result = evaluate("sqrt(16)")
        assert abs(result - 4.0) < 0.0001
