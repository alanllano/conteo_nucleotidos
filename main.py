# 1.Leer secuencia
dna_sequence = input("Ingrese la secuencia de ADN: ")
# 2.Convertir a mayusculas
dna_sequence = dna_sequence.upper()
# 3.Leer 'k'
k = input("Ingrese el valor de k: ").strip
# 4.Convertir 'k' a entero
k = int(k)
# 5. Validar secuencia
# Si dan esta vacia entonces
if not dna_sequence:
    print("La secuencia de ADN no puede estar vacía.")
    exit()
# Para cada base en dna_sequence hacer .Si base no pertenece a valid_bases entonces invalid_characters = verdadero Salir del ciclo FinSi FinPara
for base in dna_sequence:
    if base not in valid_bases:
       invalid_characters = True
         break
    # Si valid_characters es verdadero entonces
    # Mostrar "La secuencia de ADN contiene caracteres no válidos." Salir del programa FinSi
if invalid_characters:
    print("La secuencia de ADN contiene caracteres no válidos.")
    exit()  


#6. validar "k"
# Si k es menor o igual a 0 entonces
if k <= 0:
    print("El valor de k debe ser un número entero positivo.")
    exit()
# Si k es mayor que la longitud de la secuencia entonces        
if k > len(dna_sequence):
    print("El valor de k no puede ser mayor que la longitud de la secuencia de ADN.")
    exit()
# 7. Generar k-mers
for i in range(len(dna_sequence) - k + 1):
    k_mer = dna_sequence[i:i+k]
    print(k_mer)



# 8. Mostrar resultados
