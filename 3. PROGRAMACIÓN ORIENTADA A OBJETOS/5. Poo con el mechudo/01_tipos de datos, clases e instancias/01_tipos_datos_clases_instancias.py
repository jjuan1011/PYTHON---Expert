

# TIPOS DE DATOS ABSTRACTOS

# En python todo es un objeto, es decir que tiene un espacio en memoria y tiene un tipo, que es una encapsulación de datos y comportamientos de dichos objetos.

# INTEACCIÓN CON EL OBJETO

#  Creación
#  Manipulación
#  Destrucción
#___________________________________
# VENTAJAS

# Descomponer
# Abstracción
# Encapsulamiento

# DEFINICIÓN DE CLASE

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saluda(self, otra_persona):
        return f'Hola otra_persona.nombre, me llamo {self.nombre}.'
        
    # Uso
david = Persona('David', 35)
erika = Persona('Erika', 32)
david.saluda(erika)
'Hola erika me llamo david'