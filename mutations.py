# Mutation simulation
import random
from dna_processing import transcribe_dna_to_mrna, translate_mrna_to_protein
from config import codon_table

def mutate_dna(dna, mutation_type):
    mutated_dna = dna
    consequence = ""

    if mutation_type == "substitution":
        idx = random.randint(0, len(dna) - 1)
        bases = ['A', 'T', 'C', 'G']
        bases.remove(dna[idx])
        new_base = random.choice(bases)
        mutated_dna = dna[:idx] + new_base + dna[idx+1:]
        consequence = "Point mutation: can be silent, missense, or nonsense."

    elif mutation_type == "insertion":
        idx = random.randint(0, len(dna))
        new_base = random.choice(['A', 'T', 'C', 'G'])
        mutated_dna = dna[:idx] + new_base + dna[idx:]
        consequence = "Insertion: causes frameshift unless multiple of 3."

    elif mutation_type == "deletion":
        if len(dna) > 1:
            idx = random.randint(0, len(dna) - 1)
            mutated_dna = dna[:idx] + dna[idx+1:]
            consequence = "Deletion: causes frameshift unless multiple of 3."
        else:
            consequence = "Cannot delete from very short DNA."

    elif mutation_type == "duplication":
        idx = random.randint(0, len(dna) - 2)
        duplicated = dna[idx:idx+2]
        mutated_dna = dna[:idx+2] + duplicated + dna[idx+2:]
        consequence = "Duplication: repeats a DNA segment."

    elif mutation_type == "inversion":
        idx1 = random.randint(0, len(dna) - 2)
        idx2 = random.randint(idx1 + 1, len(dna))
        segment = dna[idx1:idx2]
        mutated_dna = dna[:idx1] + segment[::-1] + dna[idx2:]
        consequence = "Inversion: flips a DNA segment."

    elif mutation_type == "frameshift":
        idx = random.randint(0, len(dna))
        new_base = random.choice(['A', 'T', 'C', 'G'])
        mutated_dna = dna[:idx] + new_base + dna[idx:]
        consequence = "Frameshift: alters protein sequence."

    elif mutation_type == "silent":
        idx = random.randint(0, len(dna) - 1)
        bases = ['A', 'T', 'C', 'G']
        original_base = dna[idx]
        bases.remove(original_base)
        new_base = random.choice(bases)
        mutated_dna = dna[:idx] + new_base + dna[idx+1:]
        original_mrna = transcribe_dna_to_mrna(dna)
        mutated_mrna = transcribe_dna_to_mrna(mutated_dna)

        if len(original_mrna) >= 3 and len(mutated_mrna) >= 3:
            original_codon = original_mrna[idx//3*3:idx//3*3+3]
            mutated_codon = mutated_mrna[idx//3*3:idx//3*3+3]
            if codon_table.get(original_codon) == codon_table.get(mutated_codon):
                consequence = "Silent mutation: no change in protein."
            else:
                consequence = "Actually caused missense mutation!"

    return mutated_dna, consequence
