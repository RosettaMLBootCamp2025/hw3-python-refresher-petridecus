#!/usr/bin/env python3
"""
HW3 Part 2: Sequence Utilities
Implement functions for analyzing protein sequences.
"""

# Exercise 1: Calculate Molecular Weight
# TODO: Implement a function to calculate the approximate molecular weight of a protein
# Use the average molecular weights for amino acids
def molecular_weight(protein_seq):
    """
    Calculate the approximate molecular weight of a protein sequence.

    Uses average molecular weights for each amino acid.

    Args:
        protein_seq (str): Protein sequence (single letter codes)

    Returns:
        float: Molecular weight in Daltons (Da)

    Example:
        >>> molecular_weight("AAA")
        231.27
    """
    # Average molecular weights of amino acids (in Daltons)
    aa_weights = {
        'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.15,
        'Q': 146.15, 'E': 147.13, 'G': 75.07, 'H': 155.16, 'I': 131.17,
        'L': 131.17, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13,
        'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15
    }

    # because bond weight will be subtracted N times instead of N-1 times (i am lazy)
    weight = 18.01

    for aa in protein_seq:
        weight += aa_weights[aa] - 18.01

    return weight


# Exercise 2: Count Hydrophobic Residues
# TODO: Write a function to count hydrophobic amino acids in a sequence
def count_hydrophobic(protein_seq):
    """
    Count the number of hydrophobic amino acids in a protein sequence.

    Hydrophobic amino acids: A, V, I, L, M, F, W, P

    Args:
        protein_seq (str): Protein sequence

    Returns:
        int: Number of hydrophobic residues

    Example:
        >>> count_hydrophobic("AVLMFWP")
        7
    """
    hydrophobic = set('AVILMFWP')

    num_hydrophobic = 0
    for aa in protein_seq:
        if aa in hydrophobic:
            num_hydrophobic += 1

    return num_hydrophobic


# Exercise 3: Find Motif Positions
# TODO: Write a function to find all occurrences of a motif in a sequence
def find_motif(seq, motif):
    """
    Find all starting positions of a motif in a sequence.

    Args:
        seq (str): Protein sequence to search
        motif (str): Motif pattern to find

    Returns:
        list: List of starting positions (0-indexed) where motif is found

    Example:
        >>> find_motif("ACDEFACGH", "AC")
        [0, 5]
    """
    # TODO: Implement this function
    # Hint: Loop through the sequence and check if seq[i:i+len(motif)] == motif

    motif_positions = []
    for i in range(len(seq) - len(motif) + 1):
        if i+len(motif)-1 < len(seq) and seq[i:i+len(motif)] == motif:
            motif_positions.append(i)

    return motif_positions
            
# Exercise 4: Calculate Isoelectric Point (Simplified)
# TODO: Implement a simplified function to estimate the isoelectric point
def count_charged_residues(protein_seq):
    """
    Count positively and negatively charged amino acids.

    Positively charged: K, R, H
    Negatively charged: D, E

    Args:
        protein_seq (str): Protein sequence

    Returns:
        tuple: (positive_count, negative_count)

    Example:
        >>> count_charged_residues("KRHDE")
        (3, 2)
    """
    positive = set('KRH')
    negative = set('DE')

    pos_neg_counts = (0, 0)

    for aa in protein_seq:
        if aa in positive:
            pos_neg_counts = (pos_neg_counts[0] + 1, pos_neg_counts[1])
        elif aa in negative:
            pos_neg_counts = (pos_neg_counts[0], pos_neg_counts[1] + 1)

    return pos_neg_counts

# Test your functions
if __name__ == "__main__":
    print("Testing Sequence Utility Functions")
    print("=" * 50)

    # Example protein sequence (a short peptide)
    test_seq = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"

    # Test Exercise 1
    print("\nExercise 1: Molecular Weight")
    short_seq = "ACDEFGHIKLM"
    print(f"Sequence: {short_seq}")
    mw = molecular_weight(short_seq)
    if mw:
        print(f"Molecular Weight: {mw:.2f} Da")

    # Test Exercise 2
    print("\nExercise 2: Count Hydrophobic Residues")
    print(f"Sequence: {short_seq}")
    hydrophobic_count = count_hydrophobic(short_seq)
    print(f"Hydrophobic residues: {hydrophobic_count}")

    # Test Exercise 3
    print("\nExercise 3: Find Motif Positions")
    motif = "LV"
    print(f"Searching for motif '{motif}' in: {test_seq[:50]}...")
    positions = find_motif(test_seq, motif)
    print(f"Found at positions: {positions}")

    # Test Exercise 4
    print("\nExercise 4: Count Charged Residues")
    print(f"Sequence: {short_seq}")
    pos, neg = count_charged_residues(short_seq) or (0, 0)
    print(f"Positive charges: {pos}")
    print(f"Negative charges: {neg}")
    print(f"Net charge: {pos - neg}")

    print("\n" + "=" * 50)
    print("If you see results above, your functions are working!")
