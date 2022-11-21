
# FUNCIONES

# La funciones se crean con def, que significa definir la función, acá los dos print que se encuentran segidos de los (:) despues de efinir la función pertenecen al bloque de la función es decir que cuando se llame dicha función nos imprimirá dichos prints
def my_print():
    print('this is my print')
    print('Este bloque de codigo pertenece a mi función my_print')

my_print()

# Acá le pasamos un parámetro a la función, en este caso será texto y abajo le decimos que haga algo con ese parámetro y e que lo multiplique *2, entonces cuando llamemos a la función y reemplacemos dicho parametro por algun, caracter, mensaje, digito etc, nos hará la operación guardada en dicha función
def my_print_v2(text):
    print(text * 2)

my_print_v2('mamame el guevo')


# Las variables son muy interesantes, como podemos ver creamos la variable suma, y le definimos dos parametros, recuerda que esos dos parámetros pueden ser cualquier mierda, pueden ser una letra, una palabra, algo sin sentido, lo que importa es la lógica y la coma despues de cada parámetro, ya que esta coma va a indicar con cuántos valores vamos a poder hacer una operación en dicha función.

# EJEMPLO: A esta variable le pusimos dos valores, esto quiere decir que vamos a poder hacer muchas operaciones cuando llamamemos a la variable suma y le indiquemos que valores queremos que adquieran dichas variables

def suma (puta,guarra):
    print(puta * guarra)
    print(puta + guarra)
    print(puta - guarra)
    print(puta / guarra)

# Llamamos a la variable suma y le asignamos un valor a los dosparametros asignados
suma(4,5)
