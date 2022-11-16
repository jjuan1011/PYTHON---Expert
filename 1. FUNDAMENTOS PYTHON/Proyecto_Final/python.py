# PROJECTO

#  juego piedra papel o tijera




# Hay que crear una lógica para cuando el usuario elija piedra, tanto para cuando elija papel y tijera

# Empezamos con la lógica de la piedra
'''
ANALICEMOS EL PROGRAMA

1- Necesitamos que el usuario pueda digitar en algún lado cualquira de las opciones tanto, piedra, papel o tijera.
2- Necesitamos que cuando el usuario ponga su opción la maquina ponga la suya y nos imprima un resultado, EJEMPLO: User wins, maquina wins.
3. Tambien necesitamos que se vayan sumando los puntos de las victorias, para la maquina y el usuario.
4. Necesitamos que haya un limite de rondas o un límite de puntos, y que se imprima un mensaje ganador o perdedor para el usuario de pendiendo si ganó o no la partida.
5. Necesitamos que el progrema esté listo para volver a iniciar cuando un nuevo usuario ingrese al juego, es decir que el programa se ponga en ceros en cuanto a victorias y empiece una nueva cuenta de puntos.


ANALICEMOS LA LÓGICA

Tenemos 3 posibles escenarios empezando por la lógica de la piedra:

1. EL USUARIO GANA
- Si el usuario gana al poner piedra es porque la maquina sacó tijeras
- si el usuario gana al poner papel es porque la maquina sacó piedra
-si el usuario gana al poner tijera es porque la maquina sacó papel

2. EL USUARIO PIERDE
- Si la maquina saca piedra, porque el usuario sacó papel
- si la maquina saca papel, porque el usuario sacó piedra
- si la maquina saca tijera, porque el usuario sacó papel

3. EL USUARIO EMPATA
- El usuario y la maquina sacan pidra
- el usuario y la maquina sacan papel
- el usuario y la maquina sacan tijera
'''
# Importamos la librería para poder crear una respuesta aleatoria por parte de la maquina
import random

# PRIMERO el input para que el usuario ponga una opcion que le estamos diciendo que puede elegir
user_option = input('piedra, papel o tijera ♥ ]=> ')

# De aquí sacamos para que la maquina saque su respuesta
options = ['piedra', 'papel', 'tijera']

# Definamos la variable marcador para almacenar las victorias de cada uno, los marcadores deben empezar en ceros

puntos_usuario = 0
puntos_maquina = 0
marcador = puntos_usuario,'=',puntos_maquina


# DEFINAMOS LAS VARIABLES QUE VAMOS A NECESITAR
computer_option = random.choice(options)
# Ponemos la opcion del usuario con el metodo lower para que independientemente si el usuario pone la letra en mayuscula o minusculo o convinado el programa lo ponga en minuscula tal cual como lo tiene en su base de datos o listas internas
user_option = user_option.lower()

# Empecemos por definir el empate, ya que es lo más simple
if user_option == computer_option:
    print('Empatados :|\n JUEGA DE NUEVO ')

# Definamos PROBABILIDADES


    if not user_option in options:
        print('esa opcion no es valida')
        continue

    if user_option == 'papel' and computer_option == 'piedra':
        print('Maquina saca PIEDRA')
        print('PAPEL gana a PIEDRA\n User WINS =D ')
        puntos_usuario += 1
        puntos_maquina = 0
        print(marcador)

    if user_option == 'tijera' and computer_option == 'papel':
        print('Maquina saca PAPEL')
        print('TIJERA gana a PAPEL\n User WINS')

    if user_option == 'piedra' and computer_option == 'tijera':
        print('Maquina saca TIJERA')
        print('PIEDRA gana a TIJERA\n User WINS')






# # else:
#     print()
# if user_option == 'piedra' and computer_option == 'papel':
#     print('Maquina saca papel')
#     print('PAPEL gana a PIEDRA\n Maquina WINS =D')
# elif user_option == 'tijera' and computer_option == 'papel':
#     print('Maquina saca PAPEL')
#     print('TIJERA gana a PAPEL\n User WINS =D')

            


   





# elif user_option == 'tijera':
#     print('Maquina saca PIEDRA')
#     print('Piedra gana a tijera\n computer WINS')

