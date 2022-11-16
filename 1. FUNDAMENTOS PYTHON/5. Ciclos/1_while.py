
#  CICLO WHILE

# Mientras una condición sea True se ejecutará añgo 

counter = 0

# Mientras la variable contador sea menor o igual a 10 ejecuta la operación de abajo que es counter + 1 = Hasta llegar a 10 
# Ahora si el counter llega a 15 le decimos que rompa el ciclo con un break
# Tambien podemos ajecutar un continue en este caso le decimos si el contador es igual a 15 continue
while counter < 40:
    counter += 1
    if counter == 15:
        continue
    if counter == 35:
        break
    print(counter)

