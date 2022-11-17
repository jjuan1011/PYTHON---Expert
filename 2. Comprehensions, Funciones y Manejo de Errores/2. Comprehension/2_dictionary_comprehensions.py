

# DICCIONARY COMPREHENSIONS

# Es una forma de acortar la sintaxis de una determinada linea de codigo

'''
{key:value for var in iterable}
'''

# Estamos creando un diccionario limpio, y le estamos diciendo que el iterador i recorra el rango 1,11 y ejecute la operación de la iteracin de caa elemento del conjunto * 2 y lo imprima 
dict = {}

for i in range(1,11):
    dict[i] = i *2

print(dict)

# Esta es otra forma de hacerlo
dict_v2 = {i: i * 2 for i in range(1,5)}
print(dict_v2)

# iMPORTAMOS UNA LIBRERÍA RANDOM 
# CREAMOS una lista llena y abajo un conjunto vacio que se va a llenar con la iteración del i en la lista countries. 
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}

for i in countries:
    population[i] = random.randint(1,100)

print(population) 