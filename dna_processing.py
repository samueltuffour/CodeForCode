# dna_processing.py
# Handles transcription (DNA → mRNA) and translation (mRNA → Protein)

from config import codon_table  # Import codon to amino acid mappings

def transcribe_dna_to_mrna(dna):
    """
    Converts a non-template strand of DNA to its complementary mRNA strand.
    
    Rules:
    - A → U
    - T → A
    - C → G
    - G → C

    Note: This function assumes input is the non-template strand (coding strand).
    """
    return dna.replace('A', 'U').replace('T', 'A').replace('C', 'G').replace('G', 'C')

def translate_mrna_to_protein(mrna):
    """
    Translates mRNA sequence into a protein sequence using the codon table.

    Each 3-letter codon is mapped to an amino acid.
    Unknown codons will be labeled as "Unknown".

    Returns:
        List of strings in the format "CODON → AminoAcid"
    """
    protein_sequence = []

    if len(mrna) >= 3:
        for i in range(0, len(mrna), 3):
            codon = mrna[i:i+3]
            protein = codon_table.get(codon, "Unknown")  # Handle invalid/unknown codons
            protein_sequence.append(f"{codon} → {protein}")

    return protein_sequence
