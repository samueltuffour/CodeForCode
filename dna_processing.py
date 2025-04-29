# Handles transcription and translation
from config import codon_table

def transcribe_dna_to_mrna(dna):
    return dna.replace('A', 'U').replace('T', 'A').replace('C', 'G').replace('G', 'C')

def translate_mrna_to_protein(mrna):
    protein_sequence = []
    if len(mrna) >= 3:
        for i in range(0, len(mrna), 3):
            codon = mrna[i:i+3]
            protein = codon_table.get(codon, "Unknown")
            protein_sequence.append(f"{codon} → {protein}")
    return protein_sequence
