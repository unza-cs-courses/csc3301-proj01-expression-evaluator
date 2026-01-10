#!/usr/bin/env python3
"""Generate student variant based on ID."""
import hashlib
import random
import json
import sys

ALL_FUNCTIONS = ['sqrt', 'abs', 'sin', 'cos', 'tan', 'log', 'exp', 'floor', 'ceil']

def generate_variant(student_id: str) -> dict:
    combined = f"{student_id}-P1-CSC3301-2026"
    seed = int(hashlib.sha256(combined.encode()).hexdigest()[:8], 16)
    random.seed(seed)
    
    num_functions = random.randint(4, 6)
    required_functions = random.sample(ALL_FUNCTIONS, num_functions)
    
    return {
        'student_id': student_id,
        'seed': seed,
        'required_functions': sorted(required_functions),
        'test_constants': [round(random.uniform(1, 100), 4) for _ in range(3)],
        'precision': random.choice([4, 5, 6])
    }

if __name__ == '__main__':
    student_id = sys.argv[1] if len(sys.argv) > 1 else 'default'
    variant = generate_variant(student_id)
    with open('variant.json', 'w') as f:
        json.dump(variant, f, indent=2)
    print(json.dumps(variant, indent=2))
