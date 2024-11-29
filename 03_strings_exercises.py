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

# Extras

# Declara una variable quote con la frase: "El aprendizaje de Python es divertido". 
# Convierte todas las letras en minúsculas y luego imprímela.

quote = "El aprendizaje de Python es divertido"
print(quote.lower())

# Crea una cadena con tu comida favorita en formato de lista separada por comas 
# (ejemplo: "pizza, hamburguesa, sushi") y divídela en elementos usando el método split().
fav_food = "pizza, hamburguesa, sushi"
print(fav_food.split(","))


# Usa la función join() para combinar una lista de palabras ["Python", "es", "asombroso"] 
# en una sola cadena separada por espacios.
word_list = ["Python", "es", "asombroso"] 
list = "-".join(word_list)
print(list)

# Declara una cadena con la frase "La programación requiere paciencia" y reemplaza 
# la palabra "paciencia" por "dedicación". Imprime el resultado.
frase = "La programación requiere paciencia"
print(frase.replace("paciencia", "dedicacion"))

# Comprueba si la palabra "Python" está contenida en la frase "Estoy aprendiendo Python" 
# usando el operador in, e imprime el resultado.
print("Python" in "Estoy aprendiendo Python")

# Declara una variable con un nombre en minúsculas (ejemplo: "juan perez") y usa métodos 
# de cadena para convertirla en formato de título ("Juan Perez").
full_name = "juan perez"
print(full_name.title())

# Declara una cadena con espacios extra al principio y al final (ejemplo: " Python ") 
# y elimina los espacios innecesarios usando el método adecuado.
str_with_space = " Python "
print(str_with_space.replace(" ",""))

# Escribe una cadena de texto que incluya tanto comillas dobles como simples 
# (ejemplo: 'Ella dijo: "Estoy aprendiendo Python"') y luego imprímela.
print("\'Ella dijo: \"Estoy aprendiendo Python\"\'")

# Verifica si la cadena "Hola123" contiene únicamente caracteres alfabéticos 
# usando el método adecuado. Imprime el resultado.
str = "Hola123"
print(str.isalpha())

# Divide la frase "Python es fácil y poderoso" en dos partes: desde el inicio hasta 
# la palabra "fácil", y desde "fácil" hasta el final, usando slicing. Imprime ambas partes.
frase = "Python es fácil y poderoso"
frase_slice1 = frase[0: 15]
frase_slice2 = frase[16:]
print(frase_slice1)
print(frase_slice2)