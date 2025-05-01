# utils.py
# Utility functions used across the DNA processing GUI application

def validate_dna_sequence(dna):
    """
    Validates that a given DNA sequence contains only valid bases: A, T, C, G.
    Returns True if valid and not empty, False otherwise.
    """
    return all(base in "ATCG" for base in dna) and len(dna) > 0

def validate_mrna_sequence(mrna):
    """
    Validates that a given mRNA sequence contains only valid bases: A, U, C, G.
    Returns True if valid and not empty, False otherwise.
    """
    return all(base in "AUCG" for base in mrna) and len(mrna) > 0

import random

def generate_random_dna(length=100):
    """
    Generates a random DNA sequence of the specified length.
    Default length is 100 bases.
    
    Returns:
        A string composed of randomly selected A, T, C, G characters.
    """
    return ''.join(random.choices('ATCG', k=length))
