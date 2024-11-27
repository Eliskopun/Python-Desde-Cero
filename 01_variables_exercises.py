# 1. Declara y asigna valores a las siguientes variables:
# •	name: una cadena que contenga tu nombre.
# •	age: un número entero que represente tu edad.
# •	height: un número flotante que represente tu altura.
# •	Imprime cada variable en una línea separada.

name = "Eliezer"
age = 25
height = 63.4
print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.
convert_age_to_str = str(age)
print("Tengo", age, "años")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student = True
print(is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
full_name = "Eliezer Avilan"
print(len(full_name))

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, lastname, city_of_origin = "Eliezer", "Avilan", "Los Teques"
print("Soy de", city_of_origin, "y mi nombre es:", name, lastname)

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
fav_color = input("¿What is your favorite color? ")
print("Tu color favorito es:", fav_color)

# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "Banana"
print(fruit)
fruit = "Kiwi"
print(fruit)

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price = 57.73 # Lo que me ha costado la anualidad de mouredev-pro
convert_price_to_int = int(price)
print(convert_price_to_int)

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
adrress = "Av Uxmal Mz 1 LT 04"
address_len = len(adrress)
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone = int("14")
print(type(phone))
phone = 12
print(type(phone))