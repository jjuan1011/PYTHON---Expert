
# FUNCIONES LAMBDA

# Una función de este tipo es la misma mierda pero con una sintaxis más corta

def increment(x):
    return x + 1
result = increment(10)
print(result)

# Primero hay que saber que estas lambda las podemos guardar dentro de variables

# Acá el y despues de lambda cumple la misma función de parametro cuando en una función normal esta en parentesis, lo siguiente es la operación que en la parte de arriba va a devolver el return
increment_v2 = lambda y : y + 1
# Ahora creamos una variable para guardar el reultado de la operación
result = increment_v2(50)
print(result)

# ACÁ hacemos la misma mierda, creamos una variable en la que vamos a guardar la función lambda
# Le damos los parametros que son name y last_name y le damos un mensaje y el formato para reemplazar el name y last_name mas adelante
full_name = lambda name, last_name: f'full name {name} {last_name}'

# Por ultimo creamos una función para establecer los valores de nuestros parametros de la variable full_name
text = full_name('juan', 'meneses')
print(text)
