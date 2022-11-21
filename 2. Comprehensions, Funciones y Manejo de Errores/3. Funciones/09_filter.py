

# FILTER

# Por ejemplo tenemos una lista con elementos de comida, pues con filter podemos filtrar entre dicha lista un cierto tipo de elementos por ejemplo comida saludable

'''
EXPLICACIÓN SINTAXIS DE LAMBDA FUNCTIONS

1.Primero creamos una variable en la que almacenar la lambda para poderla imprimir 
2. Le decimos list para que al imprimir en pantalla nos arroje una lista
3. Le damos filter para que nos filtre conteniso, basado en una condición
4. Creamos la lambda con un parametro en este caso llamado x:
5: creamos la condición con una operación que sería todos los numeros que del residuo de la división de x entre 2 de 0, y 
6. finalmente le decimos de donde queremos que filtre dicha información
'''
numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(new_numbers)
print(numbers)

