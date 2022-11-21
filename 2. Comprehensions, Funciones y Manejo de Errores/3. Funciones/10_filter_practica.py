
# Creamos una lista con diccionarios adentro

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

# Imprimimos la lista matches y el tamaño de dicha lista con el metodo len
print(matches)
print(len(matches))

'''
 1. Creamos una nueva lista, le ponemos el atributo lista, para que al imprimir en pantalla lo imprima como lista
 2.le ponemos el filter para filtrar información
 3. Creamos la lambda con un parametro en este caso llamado item
 4. le damos un valor al parámetro, diciendole que nos saque ['home_team_result'] == 'Win', de la lista matches
 5. imprimimos la new_list y el tamaño de la misma

'''

# Creamos una lambda
new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print(new_list)
print(len(new_list))

print(matches)
print(len(matches))