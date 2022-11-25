

# FUNCIÓN DECORADOR

# Hagamos de cuenta que ya tenemos nuestro progrma hecho PERO resulta que queremos añadir algún mensaje a nuestras funciones que en realidad son muchas pero sin tener que entrar a cada una de ellas a modificarlas.

'''
QUÉ SON?
Son funciones que a su vez añaden funcionalidad a otras funciones.
--------------------------------------
ESTRUCTURA DE UN DECORADOR

3Funciones (A,B,C) Donde A recibe como parámetros a B para devolver C
'''

# Creamos la función decoradora con un parámetro que va a ser reemplazada por la función a la que le apliquemos la función decoradora es decir que, cuando a la función suma le apliquemos la funcion decoradora, esa funcion suma pasará a ser el parametro de la funcion decoradora y se reemplazará en todos los lados donde en la funcion decoradora se llame a ala funcion parametro-
'''
La funcion decoradora tiene una sintaxis sencilla, se define la funcion, se le da un parametro que en un futuo será la función a la que apliquemos la decoración y aplicamos las funciones internas para gestionar los mensajes y el orden del parametro apara saber si el mensaje va a antes o depsues de ejecutar la funcion a la que le vamos a aplicar la decoración
'''
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print('vamos a realizar un claculo')
    funcion_parametro()
    print('Hemos terminado el calculo')
    return funcion_interior

@funcion_decoradora
def suma():
    print(15+25)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()
