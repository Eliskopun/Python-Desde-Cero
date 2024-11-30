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