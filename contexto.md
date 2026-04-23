# 🧬 Contexto del Programa: Análisis de Secuencia de ADN

## 🎯 Problema

Desarrollar un programa en Python que analice una secuencia de ADN
ingresada por teclado y reporte el conteo de nucleótidos (A, T, C, G).

------------------------------------------------------------------------

## 📌 Requisitos

### Funcionales

-   Leer secuencia desde teclado
-   Convertir a mayúsculas
-   Validar caracteres (A, T, C, G)
-   Contar nucleótidos
-   Mostrar resultados

### No funcionales

-   Código claro y mantenible (PEP8)
-   Manejo adecuado de errores

------------------------------------------------------------------------

## 🧠 Análisis del Problema

El problema se divide en:

1.  Entrada de datos
2.  Normalización (mayúsculas)
3.  Validación de caracteres
4.  Conteo de nucleótidos
5.  Salida de resultados

------------------------------------------------------------------------

## 🏗️ Diseño del Programa

### Enfoque

Paradigma procedural (script simple y claro)

### Componentes

-   validate_sequence(seq)
-   count_nucleotides(seq)
-   main()

------------------------------------------------------------------------

## 🧾 Algoritmo (Pseudocódigo)

INICIO\
Leer secuencia\
SI secuencia vacía → mostrar error y terminar\
Convertir a mayúsculas\
Validar caracteres\
Inicializar conteo\
Contar nucleótidos\
Mostrar resultados\
FIN

------------------------------------------------------------------------
Inicio

  Solicitar la secuencia de ADN
  Leer dna_sequence
  Convertir dna_sequence a mayúsculas

  Solicitar el valor de k
  Leer k_input

  Si dna_sequence está vacía entonces
      Mostrar error
      Terminar
  FinSi

  Definir valid_bases = "ACGTN"
  Definir invalid_characters = falso

  Para cada base en dna_sequence hacer
      Si base no pertenece a valid_bases entonces
          invalid_characters = verdadero
          Salir del ciclo
      FinSi
  FinPara

  Si invalid_characters es verdadero entonces
      Mostrar error
      Terminar
  FinSi

  Intentar convertir k_input a entero → k
  Si falla entonces
      Mostrar error
      Terminar
  FinSi

  Si k <= 0 entonces
      Mostrar error
      Terminar
  FinSi

  Si k > longitud(dna_sequence) entonces
      Mostrar error
      Terminar
  FinSi

  Mostrar "K-mers:"

  Para i desde 0 hasta longitud(dna_sequence) - k hacer
      current_kmer = subcadena(dna_sequence, i, i + k)
      Mostrar current_kmer
  FinPara

Fin
## 🔁 Diagrama de Flujo (Mermaid)

``` mermaid
flowchart TD
    A[Inicio] --> B[Leer secuencia]
    B --> C{¿Secuencia vacía?}
    C -- Sí --> D[Error]
    D --> Z[Fin]

    C -- No --> E[Convertir a mayúsculas]

    E --> F{¿Caracteres válidos?}
    F -- No --> G[Error: inválido]
    G --> Z

    F -- Sí --> H[Contar nucleótidos]
    H --> I[Mostrar resultados]
    I --> Z[Fin]
```

------------------------------------------------------------------------

## 📌 Notas

-   Se pueden aceptar minúsculas (normalización)
-   Posible extensión: cálculo de GC content
-   Posible extensión: lectura desde archivo FASTA
