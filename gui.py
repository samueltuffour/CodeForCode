# GUI logic
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTabWidget, QTextEdit, QFileDialog
from dna_processing import transcribe_dna_to_mrna, translate_mrna_to_protein
from visualization import draw_dna
from mutations import mutate_dna
from utils import validate_dna_sequence, validate_mrna_sequence, generate_random_dna

class DNAInputTab(QWidget):
    def __init__(self, transcription_tab):
        super().__init__()
        self.transcription_tab = transcription_tab
        layout = QVBoxLayout()

        self.label = QLabel("Enter non-template DNA sequence:")
        self.dna_input = QTextEdit()
        self.validate_button = QPushButton("Validate DNA and Draw")
        self.load_button = QPushButton("Load DNA from File")
        self.generate_button = QPushButton("Generate Random DNA")
        self.output_label = QLabel("")

        self.validate_button.clicked.connect(self.validate_and_draw)
        self.load_button.clicked.connect(self.load_from_file)
        self.generate_button.clicked.connect(self.handle_generate_random_dna)

        layout.addWidget(self.label)
        layout.addWidget(self.dna_input)
        layout.addWidget(self.validate_button)
        layout.addWidget(self.load_button)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.output_label)
        self.setLayout(layout)
        
        long_dna = generate_random_dna(100)  # 1000 bases
        self.dna_input.setPlainText(long_dna)
    
    def handle_generate_random_dna(self):
        random_sequence = generate_random_dna(100)  # <- from utils.py
        self.dna_input.setPlainText(random_sequence)

    def load_from_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open DNA Text File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    dna = file.read().strip().upper()
                    if all(base in "ATCG" for base in dna) and dna:
                        self.dna_input.setText(dna)
                        self.output_label.setText("Valid DNA loaded. Drawing...")
                        draw_dna(dna)
                        self.transcription_tab.set_dna_input(dna)
                    else:
                        self.output_label.setText("Invalid DNA sequence in file! Use only A, T, C, G.")
            except Exception as e:
                QMessageBox.critical(self, "File Error", f"Could not read file: {e}")


    def validate_and_draw(self):
        dna = self.dna_input.toPlainText().strip().upper()
        if validate_dna_sequence(dna):
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
        if validate_dna_sequence(dna):
            mrna = transcribe_dna_to_mrna(dna)
            self.result_label.setText(f"mRNA: {mrna}")
            self.translation_tab.set_mrna_input(mrna)
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
        if validate_mrna_sequence(mrna):
            protein_sequence = translate_mrna_to_protein(mrna)
            self.result_area.setText("\n".join(protein_sequence))
        else:
            self.result_area.setText("Invalid mRNA sequence!")

    def set_mrna_input(self, mrna):
        self.mrna_input.setText(mrna)

class MutationTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Enter DNA sequence:")
        self.dna_input = QLineEdit()
        self.mutation_label = QLabel("Mutation type:")
        self.mutation_type = QLineEdit()
        self.mutation_type.setPlaceholderText("e.g., substitution, deletion, insertion")
        self.mutate_button = QPushButton("Mutate!")
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.mutate_button.clicked.connect(self.perform_mutation)
        layout.addWidget(self.label)
        layout.addWidget(self.dna_input)
        layout.addWidget(self.mutation_label)
        layout.addWidget(self.mutation_type)
        layout.addWidget(self.mutate_button)
        layout.addWidget(self.result_area)
        self.setLayout(layout)

    def perform_mutation(self):
        dna = self.dna_input.text().upper()
        mutation = self.mutation_type.text().lower()
        if validate_dna_sequence(dna):
            mutated_dna, consequence = mutate_dna(dna, mutation)
            mrna = transcribe_dna_to_mrna(mutated_dna)
            protein = translate_mrna_to_protein(mrna)
            result = f"Mutated DNA: {mutated_dna}\n\nmRNA: {mrna}\n\nProtein Translation:\n" + "\n".join(protein)
            result += f"\n\nConsequence: {consequence}"
            self.result_area.setText(result)
        else:
            self.result_area.setText("Invalid DNA sequence!")
