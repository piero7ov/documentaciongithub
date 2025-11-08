'''
Programa para gestionar animales en un zoológico utilizando SQLite.
Permite insertar nuevos animales y ver la lista de animales existentes.
Utiliza una tabla llamada 'animales' con los campos: id, animal, nombre, edad y clase.
'''

import sqlite3

basededatos = sqlite3.connect('animales.db')
cursor = basededatos.cursor()

def imprimeMenu():
    '''
    Muestra el menú de opciones al usuario.
    No tiene parámetros ni retorna valores.'''
    print("Seleccione una opción:")
    print("1. Añadir animal")
    print("2. Ver animales")

def insertar_animal():
    '''
    Inserta un nuevo animal en la base de datos.
    Solicita al usuario el tipo de animal, nombre, edad y clase.
    No retorna valores.'''
    animal = input("Ingrese el tipo de animal: ")
    nombre = input("Ingrese el nombre del animal: ")
    edad = int(input("Ingrese la edad del animal: "))
    clase = input("Ingrese la clase del animal (mamifero, reptil, ave, etc.): ")

    cursor.execute('''
    INSERT INTO animales (animal, nombre, edad, clase)
    VALUES  (?, ?, ?, ?)
    ''', (animal, nombre, edad, clase))
    basededatos.commit()
    print("Animal añadido exitosamente.")

def seleccionarAnimales():
    '''
    Selecciona y muestra todos los animales de la base de datos.
    No tiene parámetros ni retorna valores.
    '''
    cursor.execute('SELECT * FROM animales')
    animales = cursor.fetchall()
    print("Lista de animales:")
    for animal in animales:
        print(f"ID: {animal[0]}, Tipo: {animal[1]}, Nombre: {animal[2]}, Edad: {animal[3]}, Clase: {animal[4]}")

def crear_tabla():
    '''
    Crea la tabla 'animales' en la base de datos si no existe.
    No tiene parámetros ni retorna valores.
    '''
    cursor.execute('''
CREATE TABLE IF NOT EXISTS animales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal TEXT NOT NULL,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    clase TEXT NOT NULL
    
)
''')    
basededatos.commit()

print("Bienvenido al sistema de gestión de animales de un zoologico")

while True:                                                             #Bucle principal del programa
    imprimeMenu()                                                       #Muestra el menú de opciones
    opcion = input("Opción (1/2): ")                                    #Solicita la opción al usuario                                 
    if opcion == '1':                                                   #Si la opción es 1, inserta un nuevo animal
        insertar_animal()                                               #   Llama a la función para insertar un animal                                                   
    elif opcion == '2':                                              #Si la opción es 2, muestra la lista de animales
        seleccionarAnimales()                                    #   Llama a la función para seleccionar y mostrar animales
    else:                                                           #Si la opción no es válida, muestra un mensaje de error
        print("Opción no válida. Por favor, seleccione 1 o 2.")          #   Mensaje de error
    continuar = input("¿Desea realizar otra operación? (s/n): ")    # Pregunta si desea continuar
    if continuar.lower() != 's':                                    #   Si la respuesta no es 's', termina el bucle
        break                                                   #Sale del bucle principal

basededatos.close()


