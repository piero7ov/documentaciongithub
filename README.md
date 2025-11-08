# Gestor de Animales de Zoológico (SQLite)

Programa en Python para gestionar animales en un zoológico utilizando una base de datos SQLite.

## Descripción

Este script permite:

- Insertar nuevos animales en la base de datos.
- Ver la lista de animales registrados.

La información se almacena en una tabla llamada `animales` con los siguientes campos:

- `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `animal` (TEXT) — Tipo de animal (ej: León, Tigre, Águila)
- `nombre` (TEXT) — Nombre propio del animal
- `edad` (INTEGER) — Edad del animal
- `clase` (TEXT) — Clase del animal (mamífero, reptil, ave, etc.)

## Requisitos

- Python 3 instalado.
- Módulo `sqlite3` (incluido por defecto con Python).
- No requiere librerías externas adicionales.

## Archivos

- `animales.db`  
  Base de datos SQLite donde se almacenan los registros.
- `zoo.py`  
  Script principal que contiene:
  - Conexión a la base de datos.
  - Función `crear_tabla()` para crear la tabla si no existe.
  - Función `imprimeMenu()` para mostrar el menú.
  - Función `insertar_animal()` para añadir nuevos animales.
  - Función `seleccionarAnimales()` para mostrar todos los animales.
  - Bucle principal para la interacción con el usuario.

## Cómo usar

1. Asegúrate de que el script incluye la llamada a `crear_tabla()` **antes** del bucle principal para crear la tabla `animales` si aún no existe.

2. Guarda el código en un archivo llamado, por ejemplo:

   ```bash
   zoo.py
   ```

3. Ejecuta el script desde la terminal o consola:

   ```bash
   python zoo.py
   ```

4. Selecciona una opción del menú:

   - **1. Añadir animal**  
     Se solicitarán:
     - Tipo de animal
     - Nombre
     - Edad
     - Clase

   - **2. Ver animales**  
     Se mostrará la lista de todos los animales registrados en la base de datos.

5. Después de cada operación, el programa preguntará si deseas realizar otra operación:

   ```text
   ¿Desea realizar otra operación? (s/n):
   ```

   - Escribe `s` para continuar.
   - Cualquier otra tecla para salir.

6. Al salir, la conexión con la base de datos se cerrará correctamente.

## Notas

- Si `animales.db` no existe, se generará automáticamente en el mismo directorio donde se ejecute el script.
- Este programa es ideal como práctica introductoria para:
  - Manejo básico de bases de datos con `sqlite3`.
  - Uso de funciones en Python.
  - Implementación de menús interactivos en consola.
- Puedes ampliarlo agregando:
  - Modificación de registros.
  - Eliminación de animales.
  - Búsqueda filtrada por nombre, clase, etc.
