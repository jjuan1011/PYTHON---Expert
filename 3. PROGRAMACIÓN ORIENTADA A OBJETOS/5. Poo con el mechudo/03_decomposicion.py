

# DECOMPOSICIÓN

# Es partir un problema en problemas pequeños, por ejemplo partir una computadora en componentes, la ram, la ssd, la grafica etc

# Las clases nos permiten generar dichos componentes más pequeños, nos permiten agarrar un problema y generar muchas clases que en conjunto nos ayudan a crear un software, pero dichas partes sean más sencillas y faciles de mantener.

class automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = motor(cilindros=4)

        def acelerar(self, tipo='despacio'):
            if tipo == 'rapida':
                self._motor.inyecta_gasolina(10)
            else: 
                self._motor.inyecta_gasolina(3)
            self.estado = 'en_movimiento'


class motor:
    def __init__(self, cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0
    def inyecta_gasolina(self, cantidad):
        pass 