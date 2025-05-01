# Final-CSCI203-Project

## #CODEFORCODE (A tool for the Central Dogma of molecular biology)

## INSPIRATION

Code for Code is a project inspired by my BIOL204 class, in which we discussed the central dogma of molecular biology, which includes DNA replication, transcription, translation, and a whole lot more. The goal is to make software that takes all of this data and analyzes it into meaningful data that can also be visualized on a molecular level.

## Overview

CODEFORCODE is a standalone software designed to simplify the analysis of the central dogma of molecular biology. It allows users to input non-template DNA sequences, visualize transcription and translation, and generate graphical representations of DNA strands. The goal is to make biological data analysis more accessible and intuitive.

## Features

- **DNA Sequence Input**: Accepts non-template DNA sequences for analysis.
- **Transcription Simulation**: Converts DNA sequences into mRNA sequences.
- **Translation Simulation**: Translates mRNA into amino acid sequences.
- **Visual Representation**: Generates graphical drawings of DNA, mRNA, and protein structures.
- **Mutation Simulation**: Allows users to introduce mutations and observe their effects.
- **User-Friendly Interface**: Easy-to-use desktop application for biologists, students, and researchers.

## Installation

### Prerequisites

- Python (>=3.8)
- Required libraries: Turtle, PyQt5, PyQt/Tkinter (for GUI)

### HOW TO USE

1. Clone the repository
2. Install dependencies:
   ```sh
   pip install PyQt5 PyQt6
   ```
3. Run the application:

   ```sh
   python main.py
   ```

4. DNA Input Tab:

Paste your non-template DNA sequence in the text field, or

Upload one of the sample DNA text files from the docs/ folder.

5. Transcription Tab:

Click the "Transcribe" button to convert the DNA into mRNA.

The transcribed mRNA sequence will be displayed.

6. Translation Tab:

Click the "Translate" button to convert the mRNA into a chain of amino acids.

The resulting protein sequence is shown.

7. Mutation Tab:

Introduce a point mutation by specifying the position and base change.

View how the mutation affects the mRNA and resulting amino acid sequence.

## Future Plans

- Implement a mobile version for Android and iOS.
- Add AI-based protein function prediction.
- Enhance visualization with 3D molecular structures.
- Enable comparison with real genomic datasets.

## Citations and Acknowledgments

This project was built with the help of several valuable resources:

- [Tech With Tim’s YouTube Tutorial on PyQt5 & PyQt6](https://youtu.be/Vde5SH8e1OQ)
  This video helped me understand the fundamentals of PyQt GUI design, signal-slot mechanisms, and how to structure user interfaces in Python.

- [National Human Genome Research Institute’s Central Dogma Glossary Entry](https://www.genome.gov/genetics-glossary/Central-Dogma)
  This source provided clear explanations of the processes of transcription and translation, which formed the biological foundation for the project. It helped me model the steps of the central dogma accurately in the simulation.

- I also received inspiration and clarification on object-oriented design and defensive programming from various online Python communities and documentation.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## Contact

For questions or suggestions, contact [samueltuffour235@gmail.com] or open an issue on GitHub.
