
# AGREGAR AL JUEGO, para poner la palabra que digite el usuario en minuscula así la escriba una letra mayusucla y otra minuscula, todo ello para que no haya problemas con el programa

#user_option = input('piedra, papel o tijera =>')

#  user_options = user_option.lower()


# INDEXING Y SLICING

# Esto hace referencia a las posiciones de los caracteres en la cadena de texto

text = "Ella sabe python"

# Acá le estamos diciendo que nos imprima la posicion 0 en la cadena text
print(text[0])
print(text[3])

# Para sacar la posicion de derecha a izquierda se hace con el signo (-), esta sería la letra n que es la primera de derecha a izquierda
print(text[-1])

# slicing

# Basado en las posiciones podemos sacar fracciones del texto

# Acá estamos imprimiendo la posición del caracter en la posición 0 hasta la posición 5 es lo mismo que el siguiente ya que cuando no le ponemos parametro al iniio le estamos diciendo que vaya desde la posición cero y cuando no le ponemos parametro al final le estamos diciendo que vaya hasta el caracter en la ultima posición
print(text[0:5])
# del 3 al 4
print(text[3:9])
# 5 hasta el final
print(text[5:0])
# del 5 hasta el penultimo
print(text[5:-1])

# El ultimo digito mide los saltos
print(text[10:16:2])