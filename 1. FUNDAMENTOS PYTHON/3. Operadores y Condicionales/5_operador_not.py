
# OPERADOR not

# Este operador nos invierte un valor a su opuesto 

# Acá estamos volvieno false el true y true el false
print(not True)
print(not False)


# PROGRAMA PARA EJEMPLIFICAR

# Agarramos el programa del punto pasado y lo ajustamos entonces le estabamos diciendo que si estrato es igual a 1 o estrato es igual a 2 la persona podía ir al concierto pero con el Not le estamos diciendo que si la persona es estrato 1 0 2 paila NO va a poder ir

estrato = input('Ingresa tu estrato para ver si puedes o NO entrar a la zona VIP del concierto de feid:  ') 
estrato = int(estrato)

print(not (estrato == 1 or estrato == 2))