

# MODIFICANDO CONJUNTOS

# 

# Creando un conjunto
set_countries = {'colombia', 'mexico', 'bolivia'}

# Preguntar tamaño del conjunto con metodo len
size = len(set_countries)
print(size)

# Preguntar si un elemento se encuentra dentro del conjunto
print('colombia' in set_countries)

# Agregar un elemento al conjunto
set_countries.add('perú')
print(set_countries)

# Como actualiar un conjunto, es decir agregar un grupo de elementos al conjunto
set_countries.update({'argentina', 'alemania'})
print(set_countries)

# Remover elementos del conjunto
set_countries.remove('alemania')
print(set_countries)

# Limpiar todo el conjunto y dejarlo en vacio
set_countries.clear()
print(set_countries)