
# INSERCCIÓN Y ACTUALIZACIÓN DE DICCIONARIOS

# 
developer = {
    'name':'juan',
    'last_name': 'meneses',
    'langs':'python',
    'age': 20
}

print(developer)

# Actualizar un valor de una llave, acá le estamos actualizando el nombre

developer['name'] = 'david'
print(developer)

developer['age'] -= 5
print(developer)

# Eliminar un elemento
del developer['name']
print(developer)

# Otra forma de eliminar 
developer.pop('age')
print(developer)

# imprimir solo las llaves
print(developer.keys)

# imprimir solo los valores
print(developer.values)