

# MODULOS

# Sirven para solucionar diferentes tipos de problemas, son como extenciones del lenguaje que le dan más funcionalidad al mismo para poder desarrollar

# SISTEMA OPERATIVO

#  Para saber donde y en qué sistema operativo se esta ejecutando un archiv
import sys
print(sys.path)


# EXPRESIONES REGULARES

# Esta nos sirve para trabajar con expresiones regulares, que son patrones de combinaciones de caracteres, en este caso queremos buscar expresiones que coincidan con los numeros del 0 al 9 
import re
text = 'mi numero de telefono es 3209758629 codigo de pais 57 mi numero de suerte 10'
result = re.findall('[0-9]+', text)

# TIME

# Es para saber la hora actual, 
# Este caso nos arroja la hora en formato unix interpretado por la pc
import time
timestamp = time.time()
print(timestamp)
#  En este caso nos toca usar unos metodo para ver la hora n formato humano
local = time.localtime()
result = time.asctime(local)
print(result)

# COLECTIONS

# Nos sirve por ejemplo para saber cuantos vaces se repite un dato en una lista

import collections
numbers = [1,1,2,1,3,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)