

#  Operadores and & or

# AND

# En esta tabla queremos graficar que al comparar dos valores verdaderos o falsos siempre vamos a obtener un reultado verdadero o falso, LA REGLA es que siempre para que de True se deben comparar dos valores verdaderos o de lo contrario dará falso

print('True and True => ', True and True)
print('True and True => ', True and False)
print('False and True => ', False and True)
print('False and False => ', False and False)

# Es decir, acá por ejemplo estamos comparando dos operaciones si 10 es mayor que 5 es verdadero y 5 es menor que 10 es verdadero por lo que si comparamos con el and dos resultados verdaderos tendremos una compararcioon verdadera
print(10 > 5 and 5 < 10)

# PROGRAMA QUE EJEMPLIFICA EN EL MUNDO REAL
SolicitudTarjetaCredito = input("Ingrese sus ganancias para ver si puede obtener una tarjeta de crédito= ")

# Convertimos el valor que ingresó el usuario a numero entero para que no haya conflictos con el programa
SolicitudTarjetaCredito = int(SolicitudTarjetaCredito)

print(SolicitudTarjetaCredito >= 1000000 and SolicitudTarjetaCredito <= 19000000)


# OR || 

# En cuanto al or solo necesita que uno de los dos valores comparados sea verdadero para que de verdadero como resultado final, y si alguno de los valores es false entonces el resultado será false

print('True or True => ', True and True)
print('True or True => ', True and False)
print('False or True => ', False and True)
print('False orFalse => ', False and False)

# PROGRAMA PARA EJEMPLIFICAR

estrato = input('Ingresa tu estrato para ver si puedes o NO acceder al subsidio:  ') 
estrato = int(estrato)

print(estrato == 1 or estrato == 2)
