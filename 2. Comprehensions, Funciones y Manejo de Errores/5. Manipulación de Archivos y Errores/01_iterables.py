
# ITERABLES

# Acá tenemos una iteración normal, un iterador y rangos normales

for i in range(1,11):
    print(i)


# SIN EMBARGO
# Acá tenemos una iteración controlada, es decir que vamos a ir iterando a medida que nuestro culo ansioso nos lo pida
# Primero creamos una variable para almacenar la estructura de iteración, y el rango, para iterar manualmente lo hacemos con next y llamamo a la variable que almacena nuestra iteración
my_iter = iter(range(1, 4))
print(my_iter)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
