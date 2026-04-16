from collections import Counter


def validate_sequence(seq):
    """Validate that the sequence is not empty and contains only A, T, C, G."""
    if not seq:
        return False, "Sequence cannot be empty."
    valid_chars = set("ATCG")
    if not all(c in valid_chars for c in seq):
        return (
            False,
            "Sequence contains invalid characters. Only A, T, C, G are allowed.",
        )
    return True, ""


def count_nucleotides(seq):
    """Count the occurrences of each nucleotide in the sequence."""
    counts = Counter(seq)
    return {nuc: counts.get(nuc, 0) for nuc in "ATCG"}


def main():
    """Main function to run the DNA sequence analysis."""
    seq = input("Enter DNA sequence: ").strip().upper()
    valid, error_msg = validate_sequence(seq)
    if not valid:
        print(f"Error: {error_msg}")
        return
    counts = count_nucleotides(seq)
    print("Nucleotide counts:")
    for nuc in "ATCG":
        print(f"{nuc}: {counts[nuc]}")


if __name__ == "__main__":
    main()
