"""
🧬 Análisis de Secuencia de ADN

Programa que analiza una secuencia de ADN ingresada por teclado y reporta
el conteo de nucleótidos (A, T, C, G).
"""


def validate_sequence(sequence: str) -> bool:
    """
    Valida que la secuencia contenga solo nucleótidos válidos (A, T, C, G).

    Args:
        sequence: Secuencia de ADN a validar.

    Returns:
        True si la secuencia es válida, False en caso contrario.

    Raises:
        ValueError: Si la secuencia está vacía o contiene caracteres inválidos.
    """
    if not sequence:
        raise ValueError("❌ Error: La secuencia no puede estar vacía.")

    valid_nucleotides = set("ATCG")
    invalid_chars = set(sequence) - valid_nucleotides

    if invalid_chars:
        raise ValueError(
            f"❌ Error: Caracteres inválidos encontrados: {', '.join(sorted(invalid_chars))}"
        )

    return True


def count_nucleotides(sequence: str) -> dict[str, int]:
    """
    Cuenta la frecuencia de cada nucleótido en la secuencia.

    Args:
        sequence: Secuencia de ADN (debe ser válida y en mayúsculas).

    Returns:
        Diccionario con el conteo de cada nucleótido (A, T, C, G).
    """
    counts = {"A": 0, "T": 0, "C": 0, "G": 0}

    for nucleotide in sequence:
        if nucleotide in counts:
            counts[nucleotide] += 1

    return counts


def main() -> None:
    """
    Función principal que orquesta el análisis de la secuencia de ADN.

    Flujo:
    1. Lee la secuencia del teclado
    2. Normaliza a mayúsculas y elimina espacios
    3. Valida la secuencia
    4. Cuenta los nucleótidos
    5. Muestra los resultados
    """
    print("=" * 50)
    print("🧬 ANÁLISIS DE SECUENCIA DE ADN 🧬")
    print("=" * 50)

    try:
        # Lectura y normalización de entrada
        sequence = input("\n📝 Ingresa la secuencia de ADN: ").strip().upper()

        # Validación
        validate_sequence(sequence)

        # Conteo de nucleótidos
        counts = count_nucleotides(sequence)

        # Mostrar resultados
        print("\n✅ Secuencia válida")
        print(f"📊 Longitud de la secuencia: {len(sequence)} nucleótidos\n")
        print("📈 Conteo de nucleótidos:")
        print("-" * 30)

        for nucleotide in ["A", "T", "C", "G"]:
            count = counts[nucleotide]
            percentage = (count / len(sequence) * 100) if len(sequence) > 0 else 0
            bar = "█" * count
            print(f"  {nucleotide}: {count:4d} ({percentage:5.1f}%) {bar}")

        print("-" * 30)

        # Información adicional
        gc_content = (counts["G"] + counts["C"]) / len(sequence) * 100
        print(f"\n🔬 Contenido GC: {gc_content:.1f}%")
        print("=" * 50 + "\n")

    except ValueError as e:
        print(f"\n{e}")
        print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
