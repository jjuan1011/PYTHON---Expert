
# CICLOS ANIDADOS

# lISTAS DENTRO DE UNA LISTA, ahora vamos a tener un ciclo dentro de otro ciclo para hacer dos impresiones de la ñista pero de forma diferente

my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Le decimos a un iterador llamado (i) que itere la lisa my_list y despues imprimimos el resultado, EN LA SEGUNDA ITERACIÓN le decimos a un  uevo iterador llamado (i2) que recorra el resultado de recorrido del iterador (i) y ahora imprimimos el resultado de la segunda iteración
for i in my_list :
    print(i)
    for i2 in i:
        print(i2)