

# HIGUER OBTJECT FUNCTION

# Es la forma de llamar una función dentro de una función 


# Creamos la función increment con un solo parametro y despues hacemos un return de la operación del parametro queaún No hemo asignado + 1
def increment(x):
    return x + 1
# R: 2


# AHORA, creamos otrs función high_ord_func y le establecemos dos parametros, uno es x que es valor sin asignar y el segundom parametro es una función, le decimos que nos retorne la operación del parametro x mas la función 
def high_ord_func(x, func):
    return x + func(x)
# R: 2 + increment = 2 + (2 + 1)

# Creamos una variale para guardr el resultado y asignamos los parametros de la funcion high_ord_func. Un parámetro será 2 y el otro será el resutado de la operación de la función increment
resutl = high_ord_func(2, increment)
print(resutl)