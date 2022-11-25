

# POLIMORFISMO

# Es la hábilidad de tomar varias formas

# En python nos permite cambiar el comportamiento de una superclase para adaptarlo a una subclase

'''
POR EJEMPLO:

Acá utilizamos la super clase Persona como parametro de entrada de la clase Ciclista
'''
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('ando caminando')


# Esta es la sintaxis para poder inicializar la clase llamando a la superclase
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print('Ando moviendome en mi bicicleta')

# Acá le pasamos el parametro a persona y a ciclista
def main():
    persona = Persona('david')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__=='__main__':
    main()

