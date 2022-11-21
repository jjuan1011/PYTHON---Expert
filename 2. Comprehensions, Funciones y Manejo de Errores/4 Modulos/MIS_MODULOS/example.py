

#  MODULARIZAR

# Un problema que tendríamos acá es que al importar la librería main nos va a ejecutar lo que hay en dicha librería pero en este archivo example.py para evitar una doble ejecución debemos importar main desde este archivo pero guardar la ejecución de la funcipon por ejemplo o lo que qeurramos ejecutar desde acá en una función que en este caso llamamos run ahora para ejecutar una determinada cosa que haya en main debemos hacer referencia al main.LaCosaQueVamosAEjecutar

'''
import main

print(main.data)

'''

import main

print(main.data)
main.run()