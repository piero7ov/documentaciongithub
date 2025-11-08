# 🦁 Sistema de Gestión de Animales en un Zoológico

**Autor:** Piero Olivares Velazques  
**Curso:** DAM 1 (Desarrollo de Aplicaciones Multiplataforma)  

---

## 📘 Descripción del proyecto

Este programa permite **gestionar animales en un zoológico** utilizando una base de datos **SQLite**.  
A través de una interfaz de consola, el usuario puede:

- Insertar nuevos animales con sus datos (tipo, nombre, edad y clase).  
- Consultar la lista completa de animales registrados.

La base de datos se gestiona mediante una tabla llamada **`animales`** con los siguientes campos:

| Campo   | Tipo    | Descripción |
|----------|----------|-------------|
| `id`     | INTEGER (PK, AUTOINCREMENT) | Identificador único del animal |
| `animal` | TEXT | Tipo de animal (por ejemplo: tigre, loro, tortuga) |
| `nombre` | TEXT | Nombre del animal |
| `edad`   | INTEGER | Edad del animal |
| `clase`  | TEXT | Clase del animal (mamífero, reptil, ave, etc.) |

---

## ⚙️ Funcionalidades

### 1. Crear la tabla
```python
crear_tabla()
