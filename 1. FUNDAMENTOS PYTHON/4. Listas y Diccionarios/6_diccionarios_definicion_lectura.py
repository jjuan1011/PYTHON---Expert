

# DEFINICIÓN Y LECTURA DE DICCIONARIOS

# Es literalmente como un diccionario, tenemos un valor y un significado, o en el codigo una lavve y un valor

my_dict = {
    'name':"juan", 
    'last_name': "Meneses",
    'age': '20'
}

# Obtener un valor del diccionario mediante su llave
print(my_dict['age'])
print(my_dict['last_name'])
# Esta es otra forma de obtener el valor de la llave age
print(my_dict.get['age'])

# Saber si hay un valor o llame en mi diccionario
print('avion' in my_dict)