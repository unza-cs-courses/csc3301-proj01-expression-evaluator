#!/usr/bin/env python3
"""
Generate personalized ASSIGNMENT.md from template.
CSC3301 Programming Language Paradigms - Project 1: Expression Evaluator
"""
import json
from pathlib import Path


def main():
    repo_root = Path(__file__).parent.parent

    # Load variant config - try both possible locations
    config_paths = [
        repo_root / ".variant_config.json",
        repo_root / "variant.json"
    ]

    variant = None
    for config_path in config_paths:
        if config_path.exists():
            with open(config_path) as f:
                variant = json.load(f)
            break

    if variant is None:
        print("No variant config found. Run generate_variant.py first.")
        return

    # Load template
    template_path = repo_root / "ASSIGNMENT_TEMPLATE.md"
    if not template_path.exists():
        print("No assignment template found.")
        return

    template = template_path.read_text()

    # Replace placeholders with variant values
    assignment = template

    # Basic info
    assignment = assignment.replace("{{STUDENT_ID}}", variant["student_id"])

    # Required functions - format as a markdown list
    functions_list = "\n".join(
        f"- `{func}()`" for func in variant["required_functions"]
    )
    assignment = assignment.replace("{{REQUIRED_FUNCTIONS_LIST}}", functions_list)

    # Test constants
    test_constants = variant["test_constants"]
    assignment = assignment.replace("{{TEST_CONSTANT_1}}", str(test_constants[0]))
    assignment = assignment.replace("{{TEST_CONSTANT_2}}", str(test_constants[1]))
    assignment = assignment.replace("{{TEST_CONSTANT_3}}", str(test_constants[2]))

    # Precision
    precision = variant["precision"]
    assignment = assignment.replace("{{PRECISION}}", str(precision))
    assignment = assignment.replace("{{TOLERANCE}}", str(10 ** (-precision)))

    # Write personalized assignment
    output_path = repo_root / "ASSIGNMENT.md"
    output_path.write_text(assignment)
    print(f"Generated personalized assignment: {output_path}")


if __name__ == "__main__":
    main()
