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

    Returns:
        str: Transcribed mRNA sequence
    """
    try:
        dna = dna.upper().strip()
        if not all(base in "ATCG" for base in dna):
            raise ValueError("Invalid characters in DNA sequence. Only A, T, C, and G are allowed.")

        return dna.replace('A', 'U').replace('T', 'A').replace('C', 'G').replace('G', 'C')
    except Exception as e:
        return f"Error during transcription: {e}"

def translate_mrna_to_protein(mrna):
    """
    Translates mRNA sequence into a protein sequence using the codon table.

    Each 3-letter codon is mapped to an amino acid.
    Unknown codons will be labeled as "Unknown".

    Returns:
        List[str]: List of "CODON → AminoAcid" strings
    """
    protein_sequence = []
    try:
        mrna = mrna.upper().strip()
        if not all(base in "AUCG" for base in mrna):
            raise ValueError("Invalid characters in mRNA sequence. Only A, U, C, and G are allowed.")

        for i in range(0, len(mrna) - 2, 3):
            codon = mrna[i:i+3]
            protein = codon_table.get(codon, "Unknown")
            protein_sequence.append(f"{codon} → {protein}")
        return protein_sequence

    except Exception as e:
        return [f"Error during translation: {e}"]
