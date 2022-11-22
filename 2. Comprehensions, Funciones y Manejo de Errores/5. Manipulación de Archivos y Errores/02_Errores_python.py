

# MANEJO DE ERRORES EN PYTHON

# Error de syntaxis
# Es sencillo e arreglar, se analiza bien el codigo y se corrige
print(0/0))
print('Hola)


# Esta es la forma de testear un error haciendo una verificación de la veracidad de un problema, esto lo hacemos con assert le damos los parametros a suma y le decimos que su operación debe ser igual a 4
suma = lambda x,y: x + y
assert suma(2,2) == 4

# ***********************************

# AHORA vamos a ver como por ejemplo tenemos un programa y en el programa necesitamos que el usuario cumpla ciertas condiciones para hacer determinada cosa, si el usuario NO cumple dichas condiciones entonces podremos mandar una especie de error al programa indicando un mensaje para el uuario.

'''
Acá le decimos si la edad es menor a 18: Lanzamos un raise con excepción y un mensaje para el usuario
'''
age = 10
if age < 18:
    raise Exeption('No se permiten menores de edad en el pogo')