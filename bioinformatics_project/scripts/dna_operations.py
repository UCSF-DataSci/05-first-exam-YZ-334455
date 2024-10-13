import sys

# Function to compute the complement of a DNA sequence
def complement(sequence):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Create the complement sequence
    return ''.join([complement_map[base] for base in sequence.upper()])

# Function to reverse a DNA sequence
def reverse(sequence):
    return sequence[::-1]

# Function to compute the reverse complement of a DNA sequence
def reverse_complement(sequence):
    return reverse(complement(sequence))

# Main function to handle command-line input and print results
def main():
    if len(sys.argv) != 2:
        print("Usage: python dna_operations.py <DNA_sequence>")
        sys.exit(1)

    # Accepting the input DNA sequence from the command line
    sequence = sys.argv[1]

    # Perform DNA sequence operations
    complement_sequence = complement(sequence)
    reverse_sequence = reverse(sequence)
    reverse_complement_sequence = reverse_complement(sequence)

    # Output the results
    print(f"Original sequence: {sequence}")
    print(f"Complement: {complement_sequence}")
    print(f"Reverse: {reverse_sequence}")
    print(f"Reverse complement: {reverse_complement_sequence}")

# Run the script
if __name__ == "__main__":
    main()