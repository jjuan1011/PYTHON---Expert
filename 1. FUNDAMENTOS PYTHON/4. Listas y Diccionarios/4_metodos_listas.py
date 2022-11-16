
# Metodo listas

# CRUD
# Esto de arriba significa create, read, update, delte. Son 4 cosas que deberíamos lograr con los metodos de las listas

# Leer
numbers = [1,2,3,4,5]
print(numbers[1])

# Actualizar reemplazando
numbers[-1] = 20
print(numbers)

# Actualizar Agregando un numero al final de la lista
numbers.append(700)
print(numbers)

# Agregar una nuevo elemento a una posición sin eliminar el elemento que se encuentra en dicha posiciónm si no armando un esacio para ingrear el nuevo elemento 
numbers.insert(0, 'holi')
print(numbers)

# Fusionar listas
taks = ['todo', 'todo 2', 'todo 3']
new_list = numbers + taks
print(new_list)

# Saber la posición de un elemento de la lista
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

# Eliminar un elemento de lista
new_list.remove('todo')
print(new_list)

# Otra forma de eliminar un elemento, asignandole la posición del elemento que queremos eliminar
new_list.pop(0)
print(new_list)

# Eliminar el ultimo elemento de la lista
new_list.pop()
print(new_list)

# Revertir los elementos de lista, de derecha a izquierda
new_list.reverse()
print(new_list)

# Ordenar elemento de una lista, solo se pueden ordenar cuando hay un solo tipo de datos
numbers_2 = [1,3,7,3,8,74,2]
numbers_2.sort()
print(numbers_2)