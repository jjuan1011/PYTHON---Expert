

# CONDICIONALES

#  IF 

# Si ocurre algo le decimos al programa que haga algo 
# Si la condición NO se cumple no pasa nada o pedemos decirle que haga algo 

cachon = input('Pon cuántos amigos tiene tu novia para ver si eres cachón: ')
cachon = int(cachon)

if cachon >= 4:
    print('Eres cachón')

if cachon <= 1:
    print('Probablemente eres cachón ♥')


#  ELSE

# Es para indicar si la condción NO es correcta entonce corra otra instrucción


renta = input('Pon tus ganancias anuales para ver si debes declarar renta')
renta = int(renta)

if renta >= 50000000 and renta <= 100000000:
    print('Debes declarar renta')
else:
    print('O eres un muerto de hambre o seguiste los consejos del padre kiyosaky para obtener descuentos fiscales =D')

#  ELIF

# Es para anidar condiciones, es decir tenemos varias condciones en un programa que se pueden cumplir o no, entonces las anidamos

pecados = input('Pon cuantos pecados cometes al día para ver si irás al infierno: ')
pecados = int(pecados)

if pecados <= 1:
    print('Irás con papa santa')
elif pecados == 2:
    print('Te espera papá satan')
elif pecados == 5:
    print('Ya valiste mondá')
elif pecados >= 10:
    print('Creo que ni satan te aceptaría en su reyno')
else:
    print('Ve con papa chuco')
