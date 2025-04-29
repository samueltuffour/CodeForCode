import sys
import math
import turtle
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QTabWidget, QTextEdit, QHBoxLayout, QMessageBox
)

# Simple codon table for translation
codon_table = {
    'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine',
    'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine',
    'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine',
    'AUG': 'Methionine (Start)',
    'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine',
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'AGU': 'Serine', 'AGC': 'Serine',
    'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline',
    'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine',
    'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine',
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'CAU': 'Histidine', 'CAC': 'Histidine',
    'CAA': 'Glutamine', 'CAG': 'Glutamine',
    'AAU': 'Asparagine', 'AAC': 'Asparagine',
    'AAA': 'Lysine', 'AAG': 'Lysine',
    'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid',
    'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid',
    'UGU': 'Cysteine', 'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine',
    'AGA': 'Arginine', 'AGG': 'Arginine',
    'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}


def draw_dna(dna_sequence):
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)

    color1 = "cyan"
    color2 = "magenta"

    base_pair_colors = {
        ('A', 'T'): "yellow",
        ('T', 'A'): "yellow",
        ('C', 'G'): "green",
        ('G', 'C'): "green"
    }

    x = -len(dna_sequence) * 4

    for i, base in enumerate(dna_sequence):
        y = 100 * math.sin(x * 0.04)

        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color(color1)
        pen.dot(10)

        pen.color(color2)
        pen.goto(x, -y)
        pen.dot(10)

        pair = None
        if base == 'A':
            pair = 'T'
        elif base == 'T':
            pair = 'A'
        elif base == 'C':
            pair = 'G'
        elif base == 'G':
            pair = 'C'

        if pair:
            color = base_pair_colors.get((base, pair), "white")
            pen.color(color)
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.goto(x, -y)

        x += 8

    pen.hideturtle()
    turtle.done()

class DNAInputTab(QWidget):
    def __init__(self, transcription_tab):
        super().__init__()
        self.transcription_tab = transcription_tab
        layout = QVBoxLayout()

        self.label = QLabel("Enter non-template DNA sequence:")
        self.dna_input = QLineEdit()
        self.validate_button = QPushButton("Validate DNA and Draw")
        self.output_label = QLabel("")

        self.validate_button.clicked.connect(self.validate_and_draw)

        layout.addWidget(self.label)
        layout.addWidget(self.dna_input)
        layout.addWidget(self.validate_button)
        layout.addWidget(self.output_label)
        self.setLayout(layout)

    def validate_and_draw(self):
        dna = self.dna_input.text().upper()
        if all(base in "ATCG" for base in dna) and dna:
            self.output_label.setText("Valid DNA sequence. Drawing...")
            draw_dna(dna)
            self.transcription_tab.set_dna_input(dna)
        else:
            self.output_label.setText("Invalid DNA sequence! Use only A, T, C, G.")

class TranscriptionTab(QWidget):
    def __init__(self, translation_tab):
        super().__init__()
        self.translation_tab = translation_tab
        layout = QVBoxLayout()

        self.input_label = QLabel("DNA (non-template) → mRNA")
        self.dna_input = QLineEdit()
        self.transcribe_button = QPushButton("Transcribe")
        self.result_label = QLabel("")

        self.transcribe_button.clicked.connect(self.transcribe)

        layout.addWidget(self.input_label)
        layout.addWidget(self.dna_input)
        layout.addWidget(self.transcribe_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def transcribe(self):
        dna = self.dna_input.text().upper()
        if all(base in "ATCG" for base in dna) and dna:
            transcription = dna.replace('A', 'U').replace('T', 'A').replace('C', 'G').replace('G', 'C')
            self.result_label.setText(f"mRNA: {transcription}")
            self.translation_tab.set_mrna_input(transcription)
        else:
            self.result_label.setText("Invalid DNA sequence!")

    def set_dna_input(self, dna):
        self.dna_input.setText(dna)

class TranslationTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.input_label = QLabel("mRNA → Protein")
        self.mrna_input = QLineEdit()
        self.translate_button = QPushButton("Translate")
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)

        self.translate_button.clicked.connect(self.translate)

        layout.addWidget(self.input_label)
        layout.addWidget(self.mrna_input)
        layout.addWidget(self.translate_button)
        layout.addWidget(self.result_area)
        self.setLayout(layout)

    def translate(self):
        mrna = self.mrna_input.text().upper()
        protein_sequence = []
        if all(base in "AUCG" for base in mrna) and len(mrna) >= 3:
            for i in range(0, len(mrna), 3):
                codon = mrna[i:i+3]
                protein = codon_table.get(codon, "Unknown")
                protein_sequence.append(f"{codon} → {protein}")
            self.result_area.setText("\n".join(protein_sequence))
        else:
            self.result_area.setText("Invalid mRNA sequence!")

    def set_mrna_input(self, mrna):
        self.mrna_input.setText(mrna)
        
class MutationTab(QWidget):
    def __init__(self, transcription_tab, translation_tab):
        super().__init__()
        self.transcription_tab = transcription_tab
        self.translation_tab = translation_tab

        layout = QVBoxLayout()

        self.label = QLabel("Enter DNA sequence:")
        self.dna_input = QLineEdit()

        self.mutation_type_label = QLabel("Select mutation type:")
        self.mutation_type = QLineEdit()
        self.mutation_type.setPlaceholderText("Options: substitution, insertion, deletion, duplication, inversion, frameshift, silent")

        self.mutate_button = QPushButton("Mutate!")
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)

        self.mutate_button.clicked.connect(self.mutate)

        layout.addWidget(self.label)
        layout.addWidget(self.dna_input)
        layout.addWidget(self.mutation_type_label)
        layout.addWidget(self.mutation_type)
        layout.addWidget(self.mutate_button)
        layout.addWidget(self.result_area)

        self.setLayout(layout)

    def mutate(self):
        dna = self.dna_input.text().upper()
        mutation = self.mutation_type.text().lower()
        result = ""

        if not all(base in "ATCG" for base in dna) or not dna:
            self.result_area.setText("Invalid DNA sequence!")
            return

        import random

        mutated_dna = dna

        if mutation == "substitution":
            idx = random.randint(0, len(dna) - 1)
            bases = ['A', 'T', 'C', 'G']
            bases.remove(dna[idx])
            new_base = random.choice(bases)
            mutated_dna = dna[:idx] + new_base + dna[idx+1:]
            consequence = "Point mutation: can be silent, missense, or nonsense."

        elif mutation == "insertion":
            idx = random.randint(0, len(dna))
            new_base = random.choice(['A', 'T', 'C', 'G'])
            mutated_dna = dna[:idx] + new_base + dna[idx:]
            consequence = "Insertion: causes frameshift unless multiple of 3."

        elif mutation == "deletion":
            if len(dna) > 1:
                idx = random.randint(0, len(dna) - 1)
                mutated_dna = dna[:idx] + dna[idx+1:]
                consequence = "Deletion: causes frameshift unless multiple of 3."
            else:
                consequence = "Cannot delete from very short DNA."

        elif mutation == "duplication":
            idx = random.randint(0, len(dna) - 2)
            duplicated = dna[idx:idx+2]
            mutated_dna = dna[:idx+2] + duplicated + dna[idx+2:]
            consequence = "Duplication: repeats a DNA segment."

        elif mutation == "inversion":
            idx1 = random.randint(0, len(dna) - 2)
            idx2 = random.randint(idx1 + 1, len(dna))
            segment = dna[idx1:idx2]
            mutated_dna = dna[:idx1] + segment[::-1] + dna[idx2:]
            consequence = "Inversion: flips a DNA segment."

        elif mutation == "frameshift":
            idx = random.randint(0, len(dna))
            new_base = random.choice(['A', 'T', 'C', 'G'])
            mutated_dna = dna[:idx] + new_base + dna[idx:]
            consequence = "Frameshift: completely alters downstream protein sequence."

        elif mutation == "silent":
            idx = random.randint(0, len(dna) - 1)
            bases = ['A', 'T', 'C', 'G']
            original_base = dna[idx]
            bases.remove(original_base)
            new_base = random.choice(bases)

            mutated_dna = dna[:idx] + new_base + dna[idx+1:]

            # Now check if it actually changed the codon to a different amino acid
            original_mrna = dna.replace('A', 'U').replace('T', 'A').replace('C', 'G').replace('G', 'C')
            mutated_mrna = mutated_dna.replace('A', 'U').replace('T', 'A').replace('C', 'G').replace('G', 'C')

            if len(original_mrna) >= 3 and len(mutated_mrna) >= 3:
                original_codon = original_mrna[idx//3*3:idx//3*3+3]
                mutated_codon = mutated_mrna[idx//3*3:idx//3*3+3]
                if codon_table.get(original_codon) == codon_table.get(mutated_codon):
                    consequence = "Silent mutation: no change in protein."
                else:
                    consequence = "Actually caused missense mutation!"

        else:
            self.result_area.setText("Invalid mutation type! Try: substitution, insertion, deletion, duplication, inversion, frameshift, silent.")
            return

        # Transcribe and Translate
        mrna = mutated_dna.replace('A', 'U').replace('T', 'A').replace('C', 'G').replace('G', 'C')
        protein_sequence = []
        if len(mrna) >= 3:
            for i in range(0, len(mrna) - 2, 3):
                codon = mrna[i:i+3]
                protein = codon_table.get(codon, "Unknown")
                protein_sequence.append(f"{codon} → {protein}")

        result = f"Mutated DNA: {mutated_dna}\n\nmRNA: {mrna}\n\nProtein Translation:\n" + "\n".join(protein_sequence)
        result += f"\n\nConsequence: {consequence}"  # type: ignore

        self.result_area.setText(result)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODEFORCODE: Central Dogma Simulator")
        self.setGeometry(200, 200, 600, 500)

        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.translation_tab = TranslationTab()
        self.transcription_tab = TranscriptionTab(self.translation_tab)
        self.dna_input_tab = DNAInputTab(self.transcription_tab)

        self.tabs.addTab(self.dna_input_tab, "DNA Input")
        self.tabs.addTab(self.transcription_tab, "Transcription")
        self.tabs.addTab(self.translation_tab, "Translation")
        self.tabs.addTab(QWidget(), "Mutations (TBD)")
        self.tabs.addTab(QWidget(), "Visualization (TBD)")
        
        self.mutation_tab = MutationTab(self.transcription_tab, self.translation_tab)
        self.tabs.addTab(self.mutation_tab, "Mutations")


        layout.addWidget(self.tabs)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
