
# TUPLAS

# SON INMUTABLES, no podemos agregar elementos, no podemos modificarla, solo podríamos hacer lectura

numbers = (1,2,3,4,5)
strings = ('juan', 'geiny', 'meneses','mendez','meneses','meneses')

# METODOS LISTAS

# Saber en qué posición hay un elemento
print(strings.index('geiny'))

# Cuántas veces esta el mismo elemento en la tupla
print(strings.count('meneses'))

# Convertir una tupla en lista, asignandola a una nueva variable, POR EJEMPLO: Como las tuplas son inmutables y no se pueden modificar utilizamos este metodo para convertir dicha tupla en lista y poderla modificar
my_list = list(strings)
print(type(my_list))
# Modificando tupla convertida en lista
my_list[1] = 'david'

# Convertir la tupla en lista, en el ejemplo anterior convertimos la tupla en lista para modificarla, ya modificada la convertimos en tupla de nuevo
my_tuple = tuple(my_list)
print(type(my_tuple))