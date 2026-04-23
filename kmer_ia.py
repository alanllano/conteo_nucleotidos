from collections import Counter

VALID_BASES = {"A", "C", "G", "T", "N"}


def validate_sequence(sequence: str) -> tuple[bool, str | None]:
    """Valida que la secuencia solo contenga bases válidas."""
    if not sequence:
        return False, "La secuencia de ADN no puede estar vacía."

    invalid_bases = sorted({base for base in sequence if base not in VALID_BASES})
    if invalid_bases:
        return False, (
            "La secuencia de ADN contiene caracteres no válidos: "
            f"{', '.join(invalid_bases)}. Use solo A, C, G, T, N."
        )

    return True, None


def parse_k(k_input: str, max_length: int) -> tuple[int | None, str | None]:
    """Convierte y valida el valor de k."""
    try:
        k_value = int(k_input)
    except ValueError:
        return None, "El valor de k debe ser un número entero."

    if k_value <= 0:
        return None, "El valor de k debe ser un número entero positivo."

    if k_value > max_length:
        return (
            None,
            "El valor de k no puede ser mayor que la longitud de la secuencia de ADN.",
        )

    return k_value, None


def count_nucleotides(sequence: str) -> dict[str, int]:
    """Cuenta cada nucleótido en la secuencia."""
    counts = Counter(sequence)
    return {base: counts.get(base, 0) for base in sorted(VALID_BASES)}


def generate_kmers(sequence: str, k: int) -> list[str]:
    """Genera una lista de k-mers para la secuencia dada."""
    return [sequence[i : i + k] for i in range(len(sequence) - k + 1)]


def main() -> int:
    dna_sequence = input("Ingrese la secuencia de ADN: ").strip().upper()
    is_valid, error_message = validate_sequence(dna_sequence)
    if not is_valid:
        print(error_message)
        return 1

    k_input = input("Ingrese el valor de k: ").strip()
    k_value, error_message = parse_k(k_input, len(dna_sequence))
    if error_message:
        print(error_message)
        return 1

    print("\nConteo de nucleótidos:")
    nucleotide_counts = count_nucleotides(dna_sequence)
    for base in sorted(VALID_BASES):
        print(f"  {base}: {nucleotide_counts[base]}")

    print("\nK-mers:")
    for kmer in generate_kmers(dna_sequence, k_value):
        print(kmer)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
