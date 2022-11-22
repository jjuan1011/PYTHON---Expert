

# MANEJO DE EXCEPCIONES 

#  Cuando ocurre un error el programa suele deternee,  con esto vamos a evitar que esto suceda


'''
Hacemos un print con una operación que el programa identifica como un error y mas abajo hacemos otro print, Qué es lo que pasa? Sencillo, el programa e detiene con este error y NO nos ejecuta el segundo print.

Esto es un FORMA DE CAPTURAR UN ERROR para saber que tipo de error es y evitar que el programa se detenga, es decir que el segundo print si se podrá ejecutar así haya un error en el programa ya que dicho error se capturará en un bloque como pasandole por encima sin afectar toda la estructura logica
'''

try:
    print(0 / 0)
except ZeroDivisionError as error:
    print(error)

print('hola')