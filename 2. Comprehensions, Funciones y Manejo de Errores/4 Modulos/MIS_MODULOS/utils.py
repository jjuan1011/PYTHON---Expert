


# MIS MODULOS

# Todo archivo .py es un modulos es decir que podemos utilizar utilidades de un archivo dentro de otro, es como importar nuestros propios archivos

'''
PODEMOS IMPORTAR

- funciones
- Variables
'''

def get_population():
    keys = ['col', 'bol']
    values = [300, 400]
    return keys, values

A = 'hola'

# EJEMPLO

def population_by_country(data, country):
    result = list(filter(lambda item: item['country'] == country, data))
    return result