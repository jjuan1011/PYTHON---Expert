

#  TRANSFORMACIÓN DE DATOS

# Podemos transformar un dato por ejemplo a una variable name que era una variable asignada a una cadena de texto la podemos asignar la misma variabloe name a un tipo de dato numerico

# variable name tipo de dato cadena
name = "Juan"
print(type(name))

# Variable name tipo de dato numerico
name = 22
print(type(name))

# AHORA, cómo podemos concatenar dos tipos de datos distintos, como podemos ver este ejemplo nos dá error ya que estamos suamndo dos tipos de atos diferentes 

# age = 12
# print("mi edad es " + 12)

# SOLUCIÓN: Le estamos diciendo a age que se transforme en un str
age = 12
print("mi edad es " + str(age))

# Acá es lo opuesto estamos diciendole al usuario que ingrese un numero pero lo ponemos en un input y los inputs son de tipo string por lo que no nos va a ejecutar la operación es por ello que debmos a la variable age convertirla en un int entero y despues ahí si ejecutar la operación e imprimir la concatenación del mensaje más la operación
age = input('Escribe tu edad => ')
print(type(age))
age = int(age)
age += 10
print(f'tu edad en 10 años será => {age}')