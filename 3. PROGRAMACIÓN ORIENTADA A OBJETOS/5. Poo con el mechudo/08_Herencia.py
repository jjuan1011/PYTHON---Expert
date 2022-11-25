

# HERENCIA

# Nos permite heredar comportamientos de unos objetos padre a unos objetos hijos, en este ejemplo podemos ver como pudimos utilizar la función area de la clase rectangulo en la clase cuadrado utilizando como parametro rectangulo


class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base*self.altura

class cuadrado(rectangulo):
    def __init__(self, lado):
        super().__init__(lado,lado)


if __name__=='__main__':
    rectangulo = rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = cuadrado(lado=5)
    print(cuadrado.area())
