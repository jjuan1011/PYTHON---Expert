
# SCOPE

# cada variable tiene un alcance de uso es decir, es la capacidad de dicha variable para poder ejecutarse en una linea mucho más abajo u otro archivo .py en el mismo proyecto

# Local scope

# Ya sabiendo que es el scope podemos definir el local scope como la capacidad que tiene una variable para ser usada unicamente en una función

# EJEMPLO
# Estas variable estan fuera de cualquier función es decir su uso es global, en este archivo.py u otro
price = 100
result = 200

# Las variable que creamos dentro de la función solo tiene alcance en dicha función, es por ello que No choca con la variable que tiene el mismo nombre pero que esta en el scope global
def increment():
    price = 200
    price = price + 10
    print(price)
    return price

print(price)
price_2 = increment()
print(price_2)