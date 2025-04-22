'''
DNA-Sequence-Analyzer/
│── main.py                  # Main entry point of the application
│── gui.py                    # Manages the graphical user interface (PyQt/Tkinter)
│── dna_processing.py         # Handles DNA-to-mRNA transcription and translation
│── visualization.py          # Generates graphical representations of DNA, mRNA, and protein
│── mutations.py              # Implements mutation simulations and their effects
│── utils.py                  # Helper functions for sequence handling and processing
│── config.py                 # Configuration settings and constants
│── README.md                 # Project documentation
│── requirements.txt          # List of dependencies
│── tests/                    # Unit tests for different modules
│   ├── test_dna_processing.py
│   ├── test_visualization.py
│   ├── test_mutations.py
│── assets/                   # Stores static assets like icons, images, or sample sequences
│── docs/                     # Additional project documentation

'''
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QTabWidget, QTextEdit, QHBoxLayout, QMessageBox
)

class DNAInputTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel("Enter non-template DNA sequence:")
        self.dna_input = QLineEdit()
        self.validate_button = QPushButton("Validate DNA")
        self.output_label = QLabel("")

        self.validate_button.clicked.connect(self.validate_dna)

        layout.addWidget(self.label)
        layout.addWidget(self.dna_input)
        layout.addWidget(self.validate_button)
        layout.addWidget(self.output_label)
        self.setLayout(layout)

    def validate_dna(self):
        dna = self.dna_input.text().upper()
        if all(base in "ATCG" for base in dna):
            self.output_label.setText("Valid DNA sequence.")
        else:
            self.output_label.setText("Invalid DNA sequence! Use only A, T, C, G.")

class TranscriptionTab(QWidget):
    def __init__(self):
        super().__init__()
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
        if all(base in "ATCG" for base in dna):
            transcription = dna.replace('A', 'U').replace('T', 'A').replace('C', 'G').replace('G', 'C')
            self.result_label.setText(f"mRNA: {transcription}")
        else:
            self.result_label.setText("Invalid DNA sequence!")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODEFORCODE: Central Dogma Simulator")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tabs.addTab(DNAInputTab(), "DNA Input")
        self.tabs.addTab(TranscriptionTab(), "Transcription")
        self.tabs.addTab(QWidget(), "Translation (TBD)")
        self.tabs.addTab(QWidget(), "Mutations (TBD)")
        self.tabs.addTab(QWidget(), "Visualization (TBD)")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
