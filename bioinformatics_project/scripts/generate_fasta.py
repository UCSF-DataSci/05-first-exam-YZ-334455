import random
import os

# Function to generate a random DNA sequence
def generate_random_dna_sequence(length):
    return ''.join(random.choices('ACGT', k=length))

# Function to format the sequence with 80 characters per line
def format_sequence(sequence, line_length=80):
    return '\n'.join(sequence[i:i+line_length] for i in range(0, len(sequence), line_length))

# Define the main function to generate and save the sequence in FASTA format
def main():
    # Define the project directory and the output file path
    project_dir = "bioinformatics_project"
    data_dir = os.path.join(project_dir, "data")
    fasta_file = os.path.join(data_dir, "random_sequence.fasta")

    # Generate a random DNA sequence of 1 million base pairs
    sequence_length = 1_000_000
    random_sequence = generate_random_dna_sequence(sequence_length)

    # Format the sequence with 80 base pairs per line
    formatted_sequence = format_sequence(random_sequence)

    # Save the formatted sequence to the FASTA file
    with open(fasta_file, 'w') as file:
        file.write(formatted_sequence)

    print(f"Random DNA sequence generated and saved to {fasta_file}")

# Run the script
if __name__ == "__main__":
    main()