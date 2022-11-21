
# REDUCE

# Sirve para reducir algo a un solo valor, o en otras palabras sirve para sacar una conclusión de un determinado numero de valores es decir tenemos una lista de marikos y no marikos, con REDUCE podemos decir hay más marikos que no marikos


# En este caso nos toca importar una librería que sirve para importar funciones para hacer determinados trabajos

'''
1. Importar librería de funciones
2. Creamos una lista
3. Creamos una variabl result para almacenar la lambda 
4. llamamos a la librería y le ponemos el metodo reduce, 
5. Creamos la lambda con dos parámetros que en este caso son increment y item: 
6. despues creamos una operación sumando ambos parámetros
7. Finalmente le decimos que nos haga esta operación con la lista numbers

EXPLICACIÓN TODO ESTO NOS DA UN 10, y esto es porque queremos sacar un solo resultado de sumar el increment + item
'''

import functools

numbers = [1,2,3,4]

result = functools.reduce(lambda increment, item: increment + item, numbers)

print(result)