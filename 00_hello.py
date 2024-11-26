# Esto es un comentario
# Nuestro hola mundo en Python
print("Hola Python")
print("Hola Python")

# Una string o cadena es la union de uno o mas caracteres

# Ejemplos:
"Asabeneh"
"Finlandia"
"Python"
"Me encanta enseñar"
"Espero que estés disfrutando el primer día del reto 30DaysOfPython"
"""
Este es un
comentario
en varias lineas
"""

"""
Este tambien
es un comentario
en varias lineas
"""

# Boleanos
"""
tipo de datos que contiene valores logicos como: Verdadero
y Falso (T y F deben estar siempre en MAYUSCULAS)
"""
# Ejemplos:
True  # ¿Está la luz encendida? Si está encendida, el valor es True
False  # ¿Está la luz encendida? Si está apagada, el valor es False


# Listas
"""
es una colección ordenada que permite almacenar 
elementos de diferentes tipos de datos
"""

# Ejemplos:
[0, 1, 2, 3, 4, 5]  # todos son del mismo tipo de datos: una lista de números
[
    "Plátano",
    "Naranja",
    "Mango",
    "Aguacate",
]  # todos son del mismo tipo de datos: una lista de cadenas (frutas)
[
    "Finlandia",
    "Estonia",
    "Suecia",
    "Noruega",
]  # todos son del mismo tipo de datos: una lista de cadenas (países)
[
    "Plátano",
    10,
    False,
    9.81,
]  # diferentes tipos de datos en la lista: cadena, entero, booleano y flotante

# Diccionario
"""
es una colección de datos no ordenada
en un formato de par de valores clave
"""

# Ejemplos:
{
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "country": "Finland",
    "age": 250,
    "is_married": True,
    "skills": ["JS", "React", "Node", "Python"],
}

# Tupla
"""
Una tupla es una colección ordenada de 
diferentes tipos de datos como la lista, 
pero las tuplas no se pueden modificar una
vez que se crean. Son inmutables.
"""

# Ejemplos:
("Asabeneh", "Pawel", "Brook", "Abraham", "Lidiya")  # Nombres
(
    "Tierra",
    "Júpiter",
    "Neptuno",
    "Marte",
    "Venus",
    "Saturno",
    "Urano",
    "Mercurio",
)  # Planetas


# Set / conjutos
"""
Un conjunto es una colección de tipos de datos similar 
a las listas y tuplas. A diferencia de las listas 
y tuplas, un conjunto no es una colección ordenada 
de elementos
"""
{2, 4, 3, 5}  # Un conjunto de números
{3.14, 9.81, 2.7}  # El orden no importa en un conjunto


# Día 1 - Reto 30DaysOfPython

print(2 + 3)  # adición(+)
print(3 - 1)  # resta(-)
print(2 * 3)  # multiplicación(*)
print(3 / 2)  # división(/)
print(3**2)  # exponencial(**)
print(3 % 2)  # módulo(%)
print(3 // 2)  # División entera (//)

# Comprobando tipos de datos
print(type(10))  # Entero
print(type(3.14))  # Flotante
print(type(1 + 3j))  # Número complejo
print(type("Asabeneh"))  # Cadena
print(type([1, 2, 3]))  # Lista
print(type({"nombre": "Asabeneh"}))  # Diccionario
print(type({9.8, 3.14, 2.7}))  # Conjunto
print(type((9.8, 3.14, 2.7)))  # Tupla
print(type(print("Una cadena de texto"))) # Tipo 'NoneType'
#Problema sobre distancia euclidiana entre (2, 3) y (10, 8)
x1 = 2
x2 = 10
y1 = 3
y2 = 8

dx = x2 - x1
dy = y2 - y1

dx_elevado = dx ** 2
dy_elevado = dy ** 2

distancia = (dx_elevado + dy_elevado) ** 0.5

print(distancia)


