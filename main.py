# 1. Leer secuencia
dna_sequence = input("Ingrese la secuencia de ADN: ").strip()

# 2. Convertir a mayúsculas
dna_sequence = dna_sequence.upper()

# 3. Leer `k`
k = input("Ingrese el valor de k: ").strip()

# 4. Convertir `k` a entero
k = int(k)

# 5. Validar secuencia
# Si dna_sequence está vacía entonces
if not dna_sequence:
    print("La secuencia de ADN no puede estar vacía.")
    exit()

# Definir valid_bases = "ACGTN"
valid_bases = "ACGTN"

# Definir invalid_characters = falso
invalid_characters = False

# buscando caracteres no válidos en dna_sequence
for base in dna_sequence:
    if base not in valid_bases:
        invalid_characters = True
        break

# salir si hay caracteres no válidos
if invalid_characters:
    print("La secuencia de ADN contiene caracteres no válidos.")
    exit()


# 6. Validar `k`
# k tiene que ser un entero positivo y menor o igual a la longitud de la secuencia
if k <= 0:
    print("El valor de k debe ser un entero positivo.")
    exit()

if k > len(dna_sequence):
    print("El valor de k no puede ser mayor que la longitud de la secuencia de ADN.")
    exit()


# 7. Generar k-mers
for i in range(len(dna_sequence) - k + 1):
    k_mer = dna_sequence[i : i + k]
    print(k_mer)
