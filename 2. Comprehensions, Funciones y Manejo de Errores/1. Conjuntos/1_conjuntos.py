
# CONJUNTOS

# Los podemos modificar, no tienen orden en concretos, No admite elementos repetidos, usa corchete igual que los diccionarios, pero no tiene llaves:valores

set_countries = {'colombia', 'mexico', 'bolivia'}

# El conjunto puede ser de varios tipos
set_types = {1, 'hola', False, 12.12}

# A partir de un elemento podemos crear un conjunto, es decir nos va a convertir en un conjunto la palabra hola
set_from_string = set('hola')
print(set_from_string)

# A partir de una tupla podemos tener un conjunto  es decir nos aparecerá imperso con corchetes indicando que es conjunto
set_from_tuples = set('abc', 'cbv', 'as')

# A patir de una lista obtener un conjunto, es decir nos aparecerá imperso con corchetes indicando que es conjunto
numbers = [1,2,3,4,5]
set_numbers = set(numbers)
print(set_numbers)