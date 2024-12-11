# 1. Crea una lista con los números del 1 al 5 e imprímela.
first_list = [1, 2, 3, 4, 5] 
print(first_list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
second_list = [10, 20, 30, 40, 50]
print(second_list[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
first_list.append(6)
print(first_list)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
second_list.insert(2, 15)
print(second_list)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
second_list = [10, 20, 30, 30, 40, 50]
second_list.remove(30)
print(second_list)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
pop_first_list = first_list.pop()
print(pop_first_list)
print(first_list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
third_list = [100, 200, 300, 400, 500]
third_list.reverse()
print(third_list)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
fourth_list = [3, 1, 4, 2, 5]
fourth_list.sort()
print(fourth_list)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
fifth_list = [1, 2, 3]
sixth_list = [4, 5, 6]
concatenated_list = fifth_list + sixth_list
print(concatenated_list)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
sub_list = second_list[1:3]
print(sub_list)