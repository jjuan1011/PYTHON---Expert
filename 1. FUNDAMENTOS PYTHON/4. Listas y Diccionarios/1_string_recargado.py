
# STRINGS RECARGADO

# Cómo verificar si un caracter o grupo de caracteres se encuentran en una cadena de texto, acá le estamos preguntando si la palabra javascript o python esta en la variable texto

text = 'Ella sabe programar en python'
print('Javascript' in text)
print('Python' in text)
# *********************************
#  Metodo len

# Para saber cuántos caracteres tiene una cadena
size = len(text)
print(size)
# *********************************
# Metodo upper

# Este metodo nos sirve para poner en mayuscula una cadena
print(text.upper())
# *********************************
# Metodo lower

# Este metodo nos sirve para poner en minúscula una cadena de texto
print(text.lower())
# *********************************
# Metodo count

# Para contar cuánto caracteres iguales hay en una cadena ejemplo cuantas 'a' hay en la variable text
print(text.count('a'))
# *********************************
# Metodo swapcase

# Para poner en mayuscula los caracteres en minuscula y los caracteres en minuscula los caracteres en mayuscula
print(text.swapcase)

#**********************************
# Metodo starswith

# Para preguntar si un texto o cadena empieza con cierto caracter
print(text.starswith('ella'))
# *********************************
# Metodo endwith

# Es para preguntar si un texto finaliza con cierto tipo caracter
print(text.endswith('rust'))
# *********************************
# Metodo replace

# Es para reemplazar un caracter o cadena por otra en un texto o cadena
print(text.replace('python', 'Go'))
# ********************************
# Metodo Capitalize

# Es para poner el primer caracter en mayuscula
print(text.capitalize())
# *********************************
# Metodo title

# Sirve para poner el inicio de cada una de las palabras que hay en el texto en mayuscula
print(text.title())
# *********************************
# Metodo isdigit

# Sirve para preguntar si el texto es un digito
print(text.isdigit())