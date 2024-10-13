import sys
import re
import os

# Function to find all cut site locations in the sequence
def find_cut_sites(sequence, cut_site):
    # Remove the '|' character from the cut site
    cut_site = cut_site.replace('|', '')
    # Find all positions of the cut site in the sequence
    return [match.start() for match in re.finditer(cut_site, sequence)]

# Function to find pairs of cut sites that are 80-120kbp apart
def find_cut_site_pairs(locations):
    pairs = []
    for i, loc1 in enumerate(locations):
        for loc2 in locations[i+1:]:
            distance = loc2 - loc1
            if 80000 <= distance <= 120000:  # Distance between 80-120kbp
                pairs.append((loc1, loc2))
    return pairs

# Main function to handle command-line input and output results
def main():
    if len(sys.argv) != 3:
        print("Usage: python find_cutsites.py <FASTA_file> <cut_site_sequence>")
        sys.exit(1)

    # Accept the FASTA file and cut site sequence from the command line
    fasta_file = sys.argv[1]
    cut_site = sys.argv[2]

    # Read the FASTA file
    with open(fasta_file, 'r') as file:
        sequence = file.read().replace('\n', '').replace(' ', '')

    # Find all cut site locations
    cut_sites = find_cut_sites(sequence, cut_site)
    total_cut_sites = len(cut_sites)

    # Find pairs of cut sites 80-120kbp apart
    cut_site_pairs = find_cut_site_pairs(cut_sites)
    total_pairs = len(cut_site_pairs)

    # Output the results
    print(f"Analyzing cut site: {cut_site}")
    print(f"Total cut sites found: {total_cut_sites}")
    print(f"Cut site pairs 80-120 kbp apart: {total_pairs}")

    # Output the first 5 pairs
    print("First 5 pairs:")
    for i, (loc1, loc2) in enumerate(cut_site_pairs[:5], start=1):
        print(f"{i}. {loc1} - {loc2}")

    # Save the results in the results directory
    project_dir = "bioinformatics_project"
    results_file = os.path.join(project_dir, "results", "cutsite_summary.txt")
    with open(results_file, 'w') as file:
        file.write(f"Analyzing cut site: {cut_site}\n")
        file.write(f"Total cut sites found: {total_cut_sites}\n")
        file.write(f"Cut site pairs 80-120 kbp apart: {total_pairs}\n")
        file.write("First 5 pairs:\n")
        for i, (loc1, loc2) in enumerate(cut_site_pairs[:5], start=1):
            file.write(f"{i}. {loc1} - {loc2}\n")

# Run the script
if __name__ == "__main__":
    main()
