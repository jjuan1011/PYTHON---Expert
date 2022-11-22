
# ESCRIBIR EN UN ARCHIVO DE TEXTO


'''
PRIMERO QUE TODO:
Ten en cuenta que los archivos tiene permisos
- lectura ('r')
- escritura('w')
- lectura y escritura ('r+') Respetando el contenido del texto, es decir agregando lineas nuevas sin tocar las existentes
- Lectura y ESCRITURA sobreescribiendo el texto ('w+')

'''
#  Podemos escribir en un archivo con:

    # file.write('Nuevas cosas para este archivo')

with open('./05_text.txt', 'w+' ) as file:
    for i in file:
        print(i) 
    file.write('\nNuevas cosas para este archivo')