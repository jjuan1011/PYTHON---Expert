

#  Multiples returns

# Retornos multiples hace refrencia en sentido literal a retornan varios valores, por ejemplo acá le estamos asignando una operación al return que es multiplicar lenght * width * depth, pero tambien con una coma estamos imprimiendo algo fuera de contexto que es solo el valor de width que es 20, y una adena de texto

def find_volume(lenght, width, depth):
    return lenght * width * depth, width, 'putito sin cintexto'

Result = find_volume(10,20,3)
print(Result)