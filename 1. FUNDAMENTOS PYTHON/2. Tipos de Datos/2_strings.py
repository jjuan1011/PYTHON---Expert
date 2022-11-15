
# Strings

name = 'juan'
last_name = ' meneses'

# Cómo podemos unir estos dos valores que  se encuentran en nuestras variables?

# CONCATENACIÓN
full_name = name + last_name
print(full_name)

# Errores al juntar las comillas simples y las comillas

quote = "I'm Nicolas"
quote2 = ' She said "Hello" '


#  format 
# Acá en donde están dichos parentesis {} se reemplazan por los valores puestos en los parentesis despues del .format, el primer parentesis hace referencia al primer valor dentro del parentesis despues del .format y así sesesivamente.
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

# Concatenación
templateV2= "Hola mi nombre es " + name + "Y mi apellido es " + last_name
print(templateV2)

# f al inicio
templateV3 = f"Hola, mi nombre es {name}, y mi apellido es {last_name}"
print(templateV3)