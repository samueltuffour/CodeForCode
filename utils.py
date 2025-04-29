# Utility functions

def validate_dna_sequence(dna):
    return all(base in "ATCG" for base in dna) and len(dna) > 0

def validate_mrna_sequence(mrna):
    return all(base in "AUCG" for base in mrna) and len(mrna) > 0

import random

def generate_random_dna(length=100):
    return ''.join(random.choices('ATCG', k=length))