

# En este archivo vamos a ejecutar una utilidad de nuestro archivo mod.py en este caso vamos a llamar a una función

import utils

# Nos tocó meter esta sintaxis en una función run para que al importar un modulo en el archivo example.py no nos ejecute todo si no solo lo que necesitamos ahora nos tocaría llamar a run 
def run():
    keys, values = utils.get_population()
    print(keys, values)

    data = [
    {
    'country': 'colombia',
    'population': 500
    },
    {
    'country': 'bolivia',
    'population': 300
    }
    ]

    country = input('type Country => ')

    result = utils.population_by_country(data, 'colombia')
    print(result)

    
if __name__ == '__main__':
    run()







'''
EJEMPLO

Acá estamos importando una función de juestro archivo utils.py, es la función population_by_country dicha función nos sirve para filtrar contenido de la lista de diccionarios data a la cual hacemos referencia al definir la función
'''

# data = [
# {
# 'country': 'colombia',
# 'population': 500
# },
# {
#  'country': 'bolivia',
#  'population': 300
# }
# ]

# Acá creamos un input para que el usuario interactue con el contenido
# country = input('type Country => ')

# result = utils.population_by_country(data, 'colombia')
# print(result)
