# 🧬 Análisis de Secuencia de ADN

Un programa en Python que analiza secuencias de ADN e identifica el conteo de nucleótidos (A, T, C, G).

## 📋 Descripción

Este programa lee una secuencia de ADN desde la entrada del usuario, valida que contenga únicamente nucleótidos válidos (Adenina, Timina, Citosina y Guanina), y proporciona estadísticas detalladas sobre la composición de la secuencia.

## ✨ Características

- ✅ Validación de secuencias de ADN
- 📊 Conteo detallado de nucleótidos
- 🔬 Cálculo del contenido GC
- 📈 Visualización gráfica con barras
- 🛡️ Manejo robusto de errores
- 📝 Código limpio y documentado (PEP8)

## 🚀 Instalación

### Requisitos
- Python 3.11+
- Sin dependencias externas

### Configuración

```bash
# Clonar o descargar el proyecto
cd conteo_nucleotidos

# (Opcional) Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# o
.venv\Scripts\activate  # En Windows

# Instalar con uv (recomendado)
uv sync
```

## 🎯 Uso

```bash
# Ejecutar el programa
python main.py
```

### Ejemplo de sesión

```
==================================================
🧬 ANÁLISIS DE SECUENCIA DE ADN 🧬
==================================================

📝 Ingresa la secuencia de ADN: ATAGGCTA

✅ Secuencia válida
📊 Longitud de la secuencia: 8 nucleótidos

📈 Conteo de nucleótidos:
------------------------------
  A:    3 ( 37.5%) ███
  T:    2 ( 25.0%) ██
  C:    1 ( 12.5%) █
  G:    2 ( 25.0%) ██
------------------------------

🔬 Contenido GC: 37.5%
==================================================
```

## 📚 Casos de Uso

### Casos Normales
- **`ATGC`** → A:1 T:1 C:1 G:1
- **`AAAA`** → A:4 T:0 C:0 G:0
- **`ATATGC`** → A:2 T:2 C:1 G:1

### Casos de Error
- **Secuencia vacía** → Error: "La secuencia no puede estar vacía"
- **`ATBX`** → Error: "Caracteres inválidos encontrados: B, X"
- **`1234`** → Error: "Caracteres inválidos encontrados: 1, 2, 3, 4"

### Casos Especiales
- **Letra única** → `A` funciona correctamente
- **Minúsculas** → `atgc` se convierte automáticamente a `ATGC`
- **Espacios** → Se eliminan automáticamente con `.strip()`
- **Secuencias largas** → Se procesan sin problemas

## 🏗️ Estructura del Código

### Funciones

#### `validate_sequence(sequence: str) -> bool`
Valida que la secuencia contenga solo nucleótidos válidos (A, T, C, G).
- **Parámetros**: `sequence` (str) - La secuencia a validar
- **Retorna**: `True` si es válida
- **Lanza**: `ValueError` si es inválida o vacía

#### `count_nucleotides(sequence: str) -> dict[str, int]`
Cuenta la frecuencia de cada nucleótido.
- **Parámetros**: `sequence` (str) - La secuencia validada
- **Retorna**: Diccionario con conteos {A, T, C, G}

#### `main() -> None`
Función principal que orquesta el flujo del programa.
- Lee entrada del usuario
- Normaliza y valida
- Muestra resultados

## 🔄 Flujo del Programa

```
┌─ Inicio
│
├─ Leer secuencia del teclado
├─ Normalizar a mayúsculas
├─ Eliminar espacios
│
├─ Validar secuencia
│  ├─ ¿Vacía? → Error
│  └─ ¿Caracteres válidos? → Error
│
├─ Contar nucleótidos
│
├─ Mostrar resultados:
│  ├─ Longitud
│  ├─ Tabla de conteos
│  ├─ Porcentajes
│  └─ Contenido GC
│
└─ Fin
```

## 📊 Contenido GC

El programa calcula automáticamente el **GC content** (contenido de pares G-C), una métrica importante en biología:

$$GC\% = \frac{(G + C)}{Longitud\,total} \times 100$$

## 🛠️ Desarrollo

### Verificar PEP8
```bash
python -m py_compile main.py
```

### Ejecutar con diferentes secuencias
```bash
# Interactivamente
python main.py
```

## 📝 Notas

- Las minúsculas se convierten automáticamente a mayúsculas
- Los espacios iniciales y finales se eliminan
- Solo se aceptan los nucleótidos estándar: A, T, C, G
- El programa es amigable con el usuario (emojis y mensajes claros)

## 🔮 Posibles Extensiones

- [ ] Lectura desde archivos FASTA
- [ ] Análisis de codones
- [ ] Búsqueda de genes
- [ ] Traducción de ADN a proteína
- [ ] Exportar resultados a CSV
- [ ] Comparación entre secuencias

## 📄 Licencia

Proyecto de práctica educativa.

## 👨‍💻 Autor

Desarrollado como parte del programa de análisis de ADN en Python.

---

**Última actualización**: 16 de abril de 2026
