

# OPERACIONES ENTRE CONJUNTOS

# UNIÓN
# Union de conjuntos, ya que no pueden haber elementos repetidos, crearíamos un conjunto de forma limpio con elementos únicos por lo que la únion sería impia
set_a = {'col', 'mex', 'arg', 'usa'}
set_b = {'per', 'braz', 'usa'}


# Acá estamos uniendo ambos conjuntos
set_c = set_a.union(set_b)
print(set_c)
# Es lo mismo pero con operadores
print(set_a | set_b)

# INTERSECCIÓN
# Acá estamo haciendo una intersección de conjuntos, en las cuales sacamos los elementos en comun que tienen ambos conjuntos, en este caso ambos tiene el termino 'usa'
set_d = set_a.intersection(set_b)
print(set_d)
# Es lo mismo pero con operadores
print(set_a & set_b)

# DIFFERENCIA
# Acá estamos practicamente restando lo del set_a - set_b, es decir. veamos que entre ambos conjuntos el unico termino semejante es 'usa', es por ello que al efectuar la resta, omitimos todo lo del conjunto set_b que se encuentra en la difference y le restamos el unico termino es decir que tambien se omitiría este termino en la impresion ES DECIR que quedarían todos los terminos del set_a menos el que compartía como semejante en el set_b, ya que se restó
set_e = set_a.difference(set_b)
print(set_c)
# Esta es la forma de hacerlo pero con operadores
print(set_a - set_b)

# DIFERENCIA SYMETRICA
# Estamos solo dejando los elementos de ambos conjuntos que no se repiten es decir quedarían todos los datos del set_a y set_b excepto los que tienen en común, estos se omitirían en la impresión
set_f = set_a.symmetric_difference(set_b)
print(set_f)
# Esto es lo mismo que arriba pero con un operador
print(set_a ^ set_b)