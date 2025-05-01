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
# Main application
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget

# Import custom GUI components for each tab
from gui import DNAInputTab, TranscriptionTab, TranslationTab, MutationTab

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setObjectName("MainWindow")
        self.setWindowTitle("CODEFORCODE: Central Dogma Simulator")
        self.setGeometry(200, 200, 600, 500)  # Window size and position

        # Set up layout and tabs
        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        # Initialize tabs (pass dependencies as needed)
        self.translation_tab = TranslationTab()
        self.transcription_tab = TranscriptionTab(self.translation_tab)
        self.dna_input_tab = DNAInputTab(self.transcription_tab)
        self.mutation_tab = MutationTab()

        # Add tabs to the main window
        self.tabs.addTab(self.dna_input_tab, "DNA Input")
        self.tabs.addTab(self.transcription_tab, "Transcription")
        self.tabs.addTab(self.translation_tab, "Translation")
        self.tabs.addTab(self.mutation_tab, "Mutations")

        # Add the tab widget to the main layout
        layout.addWidget(self.tabs)
        self.setLayout(layout)

        # Apply application-wide stylesheet
        app.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #2c3e50;
                background: #f4f6f7;
            }

            QTabBar::tab {
                background: #2c3e50;
                color: white;
                padding: 8px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }

            QTabBar::tab:selected {
                background: #f1c40f;
                color: black;
            }

            QPushButton {
                background-color: #2c3e50;
                color: white;
                border-radius: 5px;
                padding: 6px 12px;
            }

            QPushButton:hover {
                background-color: #1a252f;
            }

            QLabel {
                color: #34495e;
                font-weight: bold;
            }

            QLineEdit, QTextEdit {
                background-color: #ffffff;
                border: 1px solid #bdc3c7;
                padding: 4px;
                color: #2c3e50;
            }
        """)

# Entry point of the application
if __name__ == "__main__":
    app = QApplication(sys.argv)         # Create the application
    window = MainWindow()                # Create the main window
    window.show()                        # Show the GUI
    sys.exit(app.exec())                 # Start the event loop
