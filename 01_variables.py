# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable)

# Concatenacion de variables en un print
print("Este es el valor de:", my_bool_variable)
print(my_string_variable, my_int_variable, my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea ¡No abusar de este sintaxis!
name, lastname, alias, age = "Eliezer", "Avilan", "Eliskopun", 25
print("Me llamo:", name, lastname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 25
age = "Eliezer"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))


# Ejerccios - Dia 2

# Nivel 1
nombre = "Eliezer" #3
apellido = "Avilan" #4
nombre_completo = "Eliezer Avilan" #5
pais = "Venezuela" #6
cuidad = "Los Teques" #7
edad = 25 #8
año = 1999 #9
estado_civil = "Casado" #10
es_verdadero = True #11
luz_encendida = False #12
color_fav, numero_fav, comida_fav, estatura, peso = "salmon", 11, "Hamburguesa", 1.74, 64.3 #13

# Nivel 2

#1
print(type(nombre)) 
print(type(apellido))
print(type(nombre_completo)) 
print(type(pais)) 
print(type(cuidad)) 
print(type(edad))
print(type(año))
print(type(estado_civil))
print(type(es_verdadero))
print(type(luz_encendida))
print(type(color_fav))
print(type(numero_fav))
print(type(comida_fav))
print(type(estatura))
print(type(peso))

#2
print(len(nombre))
#3
print(len(apellido))

#4
num_one = 5
num_two = 4

#5
total = num_one + num_two

#6
diff = num_two - num_one

#7
product = num_two * num_one

#8
division = num_one / num_two

#9
remainder = num_two % num_one

#10
exp = num_one ** num_two

#11
floor_division = num_one // num_two

#12
radius_of_circle = 30

#i
area_of_circle = (radius_of_circle ** 2) * 3.1416

#ii
circum_of_circle = (radius_of_circle * 2) * 3.1416

#iii
radius_of_circle = input("Enter your radius of circle: ")
area_of_circle = (int(radius_of_circle) ** 2) * 3.1416

#13
nombre = input("Enter your name: ")
apellido = input("Enter your lastname: ")
pais = input("Enter your country: ")
age = input("Enter your age: ")





