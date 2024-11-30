# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
print("Hola"+"Python")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
str = "Cadena con\nsalto de linea"
print(str)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname, age = "Eliezer", "Avilan", 25
print(f"Mi nombre es {name} {surname} y tengo {age} años")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
language = "Python"
a, b, c, d, f, e = language
print(a)
print(b)
print(c)
print(d)
print(f)
print(e)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
word = "Programación"
slice_word = word[3:8]
print(slice_word)

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
slicing = language[::-1]
print(slicing)

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
str = "aprendiendo python"
print(str.upper())

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
str = "Programación en Python"
print(str.count("n"))

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
str = "12345"
print(str.isnumeric())