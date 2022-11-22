

# LEER ARCHIVOS DE TEXTO

# Esto nos lee todo el contenido del texto
file = open('./05_text.txt')
# print(file.read())

# De esta manera podemos leer el texto linea a linea
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

# Con esto cerramos el archivo para liberar espacio en RAM
file.close()


'''PARA HACER LO MISMO DE ARRIBA PERO DE UNA FRMA MAS SENCILLA Y ORDENADA'''
with open('./05_text.txt') as file:
    for i in file:
        print(i) 