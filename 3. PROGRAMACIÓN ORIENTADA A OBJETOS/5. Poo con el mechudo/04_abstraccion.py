

# ABSTRACCIÓN

# LA IDEA CENTRAL CUANDO ESCRIBIMOS SOFTWARE:

# Al usuario No le interesan muchas cosas, solo que la lavadora en este caso le sirva, quiere ajustar la temperatura y el tiempo, NO le interesa cómo esta programada, o como funciona su sistema interno, solo le interesa que lave sus chiros

# Enfocarnos en la información relevante y NO relevante, por ejemplo cuando estas manejando un auto no estas pendiente de como se genera el proceso de combustión, o como esta funcionando el sistema electrico del vehículo, te concentras en manejar, en escuchar musica, en el camino, etc. La abstracción es entender como muchas veces NO tenemos que preocuparnos por ejemplo como funcionan las librerías al detalle, a las cosas que nos rodean al detalle para poder hacer uso de ellas.
# Cuando te subes a un asensor NO estas preocupado de su software o de como sube y baja, simplemente te preocupa tu interacción con el mismo y que no se vaya a caer, esto es la abstracción, saber diferenciar la Información relevante y NO relevante.

class Lavadora:
    def __init__(self):
        pass
    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'llenando el tanque con agua{temperatura}')
    
    def _anadir_jabon(self):
        print('añadiendo jabon')
    
    def _lavar(self):
        print('lavando la ropa')
    
    def _centrifugar(self):
        print('centrifugando la ropa')


if __name__=='__main__':
    lavadora = Lavadora
    lavadora.lavar()