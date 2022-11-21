
# FUNCIONES RETURN

# A las funciones les podemos decir que nos retornen algún valor, despues de cumplir determinadas operaciones.
'''
LOGICA:
1. Empezamos por definir una funcion llamada 
sum_width_range
2. A dicha función le damos dos parametros random sin ningun valor asignado 
(min,max)
3. Ahora establecemos una variable que valga cero, para mas adelante hacer una iteeración o recorrido en un rango que vamos a establecer más adelante
 sum = 0
4. Empezamos con la iteración y su lógica
 sum = 0
 5. La operación va a ser la variable sum + i =, es entonces como la variable sum comienza en cero con cada iteración se va a sumar un difito en el rango que establezcamos, si establecemos un rango (1,10) la operación sería 
 
 ITERACIÓN 1
 sum + i =
 0 + 1 = 1
 ITERACIÓN 2
 sum + i =
 1 + 2 = 3
  ITERACIÓN 3
 sum + i =
 3 + 3 = 6
 ITERACIÓN 4
 sum + i =
 6 + 4 = 10
  ITERACIÓN 5
 sum + i =
 10 + 5 = 15
 ITERACIÓN 6
 sum + i =
 15 + 6 = 21
  ITERACIÓN 7
 sum + i =
 21 + 7 = 28
 ITERACIÓN 8
 sum + i =
 28 + 8 = 36
 Y ASÍ SISESIVAMENTE
 
 6. Creamos una variable para guardar el rango y la imrpimimos

 7. Creamos otra variable para hacer una operación con el calculo final


'''

def sum_width_range(min, max):
    print(min, max)
    sum = 0
    for i in range(min, max):
        sum += i
    return sum

result = sum_width_range(1, 10)
print(result)

result_2 = sum_width_range(result, result + 10)
print(result_2)
