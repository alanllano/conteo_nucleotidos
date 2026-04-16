# 🧪 Casos de Prueba

## ✅ Casos normales

  Caso   Entrada   Descripción   Salida esperada
  ------ --------- ------------- -----------------
  1      ATGC      Caso básico   A:1 T:1 C:1 G:1
  2      AAAA      Repetición    A:4 T:0 C:0 G:0
  3      ATATGC    Mixto         Conteo correcto

------------------------------------------------------------------------

## ❌ Casos de error

  Caso   Entrada   Descripción         Resultado esperado
  ------ --------- ------------------- --------------------
  4      ""        Secuencia vacía     Error
  5      ATBX      Caracter inválido   Error
  6      1234      No biológico        Error

------------------------------------------------------------------------

## ⚠️ Casos límite (edge cases)

  Caso   Entrada            Descripción       Resultado esperado
  ------ ------------------ ----------------- -------------------------
  7      A                  Longitud mínima   A:1
  8      atgc               Minúsculas        A:1 T:1 C:1 G:1
  9      ATGCATGCATGCATGC   Secuencia larga   Conteo correcto
  10     " ATGC "           Espacios          Trim o error controlado
  11     NNNN               Bases ambiguas    Error
