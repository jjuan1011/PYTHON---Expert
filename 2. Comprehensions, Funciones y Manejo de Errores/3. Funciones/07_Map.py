

# MAP

# Hace transformaciones a una lista de elementos 

# Ejemplo, tenemos un grupo de elementos que son comida cruda, y los pasamos por una función map llamada cocinar, por lo que dichos elementos despues de ser pasados y transformados po dicha función, saldrán elementos cocinados.


'''
1.En este ejemplo tenemos dos listas, una llena y una vacia

2. Abajo hacemos una iteración a la lista llena u tilizamos el metodo append en la lista _v2 para agregar la iteración de cada número multiplicado * 2

3. Entonces con esto agarramos los elemntos de una lista y lo transformamos y los ponemos en otra lista
'''
numbers = [1,2,3,4,5]
numbers_v2 = []

for i in numbers:
  numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)
# *********************************

'''
SIN EMBARGO TODO ESTE PROCESO LO PODEMOS HACR CON MAP

1. Primero creamos la variable en la que vamos a guardar la transformación
2. despues la igualamos para que sea una lista, le aplicamos la función map para que haga la transformación, 
3. creamos una función lambda con un parametro i, y dicho parametro i lo multiplicamos * 4 para hacer la transformación de cada iteración, y finalmente le decimos que cada iteración la agarre de la lista numbers o en otras palabras sería enviarle la lista numbers
'''

numbers_v3 = list(map(lambda i: i *4, numbers))

print(numbers_v3)