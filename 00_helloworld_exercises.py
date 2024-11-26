# 1. Imprime "¡Hola Mundo!" por consola.
print("¡Hola Mundo!")


# 2. Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1.
# imprime por consola una cadena texto que dice: '¡Hola Mundo!'

# 3. Imprime tu nombre y edad en la misma línea utilizando la función print.
print("Me llamo Eliezer y tengo 25 años.")

# 4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.
print(type("Quiero ser un programador")) # cadena de texto
print(type(28)) # numero entero favorito
print(type(3.13)) # numero decimal que es mi version de Python actualmente

# 5. Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.
"""
Los tipos de datos son clases para poder distinguir valores y poder clasificarlos, entre ellos lo mas comunes son:
str = string = cadena texto (Ejemplo: "Hola" , "Vamos con todo")
int = integer =   numeros enteros (Ejemplo: 21, 1325135)
float = numeros flotante (Ejemplo: 3.1416)
bool = boolean = booleano
"""

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
print("¡Hola"+ "" + "Mundo!")

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.
nombre = "Eliezer"
edad = 25
print("Hola mi nombre es:", nombre, "y tengo", edad, "años")

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
nombre = input("¿Cual es tu nombre? ")
print("Hola " + nombre)

# 9. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.
suma = 28 + 11 
print(suma) 
print(type(suma)) 

# 10. Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.
# variable que suma dos entero
suma = 28 + 11 

# se impreme la suma de los enteros
print(suma)

# se imprime el tipo de dato de la suma
print(type(suma))

