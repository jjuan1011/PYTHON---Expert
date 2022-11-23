

# HERENCIA 

# Como buna practica NO repitamos lineas de código si no que reutilicemos código

# La HERENCIA nos permitirá crear nuevas clases, a partir de una clase global 

'''
SUPERCLASE
___________________________________
Esta super clase hará de padre y le hereará a las demás clases material necesario para crear subclases.

SUBCLASE
____________________________________
Serán los hijos de la superclase los cuales heredarán material necesario de la superclase

'''

'''
            VEHICULO
            color ruedas
            cc
            vel
            tipo
                |
                |
        ________|_______
        |               |
        |               |
        |               |
      COCHE          BICICLETA
       vel             tipo
       cc
        |               |
        |               |
    CAMIONETA        MOTOCICLETA
      carga            vel
                        cc
'''

# En el ejemplo anterior podemos ver una SUPERCLASE vehiculo que es el padre y los hijos o subclases.
# Podemos observar que las subclases o hijos heredan atributos del padre como lo es la cc y la vel y el tipo. 

'''
AUTOMATICAMENTE se hereda todo sin embargo nosotros decidimos que usar
'''