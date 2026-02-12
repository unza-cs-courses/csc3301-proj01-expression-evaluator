"""Public tests for Expression Evaluator."""
import pytest
import math
from src.evaluator import evaluate


class TestBasicArithmetic:
    def test_addition(self):
        assert evaluate("2 + 3") == 5.0

    def test_subtraction(self):
        assert evaluate("10 - 4") == 6.0

    def test_multiplication(self):
        assert evaluate("4 * 5") == 20.0

    def test_division(self):
        assert evaluate("15 / 3") == 5.0

    def test_precedence(self):
        assert evaluate("2 + 3 * 4") == 14.0

    def test_parentheses(self):
        assert evaluate("(2 + 3) * 4") == 20.0

    def test_power(self):
        assert evaluate("2 ^ 10") == 1024.0


class TestVariables:
    def test_single_variable(self):
        assert evaluate("x", {"x": 5}) == 5.0

    def test_expression_with_variables(self):
        assert evaluate("x + y * 2", {"x": 3, "y": 4}) == 11.0


class TestFunctions:
    """Test required functions from the student's variant.

    These tests dynamically check only the functions assigned
    to the student via their variant configuration.
    """

    # Known safe test inputs and expected outputs for each function
    FUNCTION_TESTS = {
        "sqrt":  ("sqrt(4)",    2.0),
        "abs":   ("abs(-5)",    5.0),
        "sin":   ("sin(0)",     0.0),
        "cos":   ("cos(0)",     1.0),
        "tan":   ("tan(0)",     0.0),
        "log":   ("log(1)",     0.0),
        "exp":   ("exp(0)",     1.0),
        "floor": ("floor(3.7)", 3.0),
        "ceil":  ("ceil(3.2)",  4.0),
    }

    def test_required_functions(self, required_functions, tolerance):
        """Each function in the student's variant must evaluate correctly."""
        for func in required_functions:
            expr, expected = self.FUNCTION_TESTS[func]
            result = evaluate(expr)
            assert abs(result - expected) < tolerance, (
                f"{func}: evaluate(\"{expr}\") returned {result}, "
                f"expected {expected}"
            )

    def test_function_in_expression(self, required_functions, tolerance):
        """A required function used inside a larger expression."""
        # Pick whichever function is first in the variant list
        func = required_functions[0]
        expr, base_expected = self.FUNCTION_TESTS[func]
        full_expr = f"{expr} + 1"
        result = evaluate(full_expr)
        assert abs(result - (base_expected + 1)) < tolerance, (
            f"evaluate(\"{full_expr}\") returned {result}, "
            f"expected {base_expected + 1}"
        )


class TestVariantConstants:
    """Sanity-check the student's variant test constants."""

    def test_constant_arithmetic(self, test_constants, tolerance):
        """Evaluate each test constant multiplied by 2."""
        for const in test_constants:
            result = evaluate(f"{const} * 2")
            expected = const * 2
            assert abs(result - expected) < tolerance, (
                f"evaluate(\"{const} * 2\") returned {result}, "
                f"expected {expected}"
            )
