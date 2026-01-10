#!/usr/bin/env python3
"""Display current variant."""
import json
try:
    with open('variant.json') as f:
        variant = json.load(f)
    print("Your variant:")
    print(json.dumps(variant, indent=2))
except FileNotFoundError:
    print("No variant.json found. Run: python scripts/generate_variant.py YOUR_STUDENT_ID")
