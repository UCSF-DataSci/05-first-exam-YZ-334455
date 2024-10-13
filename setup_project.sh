#!/bin/bash

# setup_project.sh
# This script sets up the directory structure for the bioinformatics_project.


# Define the main project directory
PROJECT_DIR="bioinformatics_project"

# Create the main project directory and subdirectories
mkdir -p "$PROJECT_DIR/data" "$PROJECT_DIR/scripts" "$PROJECT_DIR/results"

# Navigate to the scripts directory
cd "$PROJECT_DIR/scripts"

# Create empty Python scripts
touch generate_fasta.py dna_operations.py find_cutsites.py

# Navigate to the results directory and create an empty summary file
cd ../results
touch cutsite_summary.txt

# Navigate to the data directory and create an empty fasta file
cd ../data
touch random_sequence.fasta

# Navigate back to the main project directory
cd ..

# Create README.md with a brief description
echo "# Bioinformatics Project Structure

This project is organized as follows:

- **data/**: Contains input data files such as \`random_sequence.fasta\`.
- **scripts/**: Contains Python scripts for various bioinformatics operations:
  - \`generate_fasta.py\`: Script to generate FASTA files.
  - \`dna_operations.py\`: Script for performing DNA operations.
  - \`find_cutsites.py\`: Script to find restriction enzyme cut sites.
- **results/**: Stores output results, including \`cutsite_summary.txt\`.

" > README.md


# Print success message
echo "Project directory structure created successfully:
$PROJECT_DIR/
├── data/
│   └── random_sequence.fasta
├── scripts/
│   ├── generate_fasta.py
│   ├── dna_operations.py
│   └── find_cutsites.py
├── results/
│   └── cutsite_summary.txt
└── README.md
"