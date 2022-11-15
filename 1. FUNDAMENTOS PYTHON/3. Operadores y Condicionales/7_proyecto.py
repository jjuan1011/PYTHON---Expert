
# PROJECTO

#  juego piedra papel o tijera


# input para que el usuario ponga una opcion
user_option = input('Piedra papel o tijera ♥ ]=> ')
computer_option = 'piedra'

# Hay que crear una lógica para cuando el usuario elija piedra, tanto para cuando elija papel y tijera

# Empezamos con la lógica de la piedra
'''
ANALICEMOS EL PROBLEMA

Tenemos 3 posibles escenarios empezando por la lógica de la piedra:

1. EL USUARIO GANA
- Si el usuario gana al poner piedra es porque la maquina sacó tijeras

2. EL USUARIO PIERDE
- Si la maquina saca papel.

3. EL USUARIO EMPATA
- El usuario empata porque la maquina sacó lo mismo que en este caso es piedra.

'''

# En la primera fase se asume que la maquina sacó piedra...
if user_option == computer_option:
    print('Empatados :|\n JUEGA DE NUEVO ')
elif user_option == 'papel':
    print('Maquina saca PIEDRA')
    print('PAPEL gana a PIEDRA\n User WINS =D ')
elif user_option == 'tijera':
    print('Maquina saca PIEDRA')
    print('Piedra gana a tijera\n computer WINS')


