
# LIST COMPREHENSION

# Esto nos ofrece una sintaxis más corta, nos da el mismo resultado pero en menos lineas de codigo

# Acá creamos una variable limpia sin datos y abajo le decimos a un iterador que nos recorra en un rango de 1 a 11 y despues con el metodo append agregamos dicha iteración a la variable de lista numbers siempre y cuando se cumpla la condicion de que el residuo de la division de i (que es cada uno de los valores del rango), entre 2 sea igual a 0.
numbers = []

for i in range(1,11):
    if i % 2 == 0:
        numbers.append(i * 2)
print(numbers)

# Con list comprehension nos da una sintaxis mas corta obteniendo el mismo resultado
numbers_v2 = [i * 2 for i in range(1,11) if i % 2 == 0]
print(numbers_v2)


