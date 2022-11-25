

# SETTER, GUETTERS 
# Sirven para poder leer y modificar elementos que se encuentran encapsulados, es decir que vamos a poder leer y modificar los elementos desde afuera de la clase


class cuenta():
    def __init__(self, pro, sal, mon):
        self._propietario = pro
        self._saldo = sal
        self._moneda = mon


# Gatters (Metodos GET) OBTENER VALORES
    def get_saldo(self):
        return self._saldo

    def get_propietario(self):
        return self._propietario

    def get_moneda(self):
        return self._moneda

    # Setters (Metodos SET) MODIFICAR VALORES
    def set_moneda(self,moneda):
        self._moneda = moneda


    # Acá estamos obteniendo (get) los valores encapsulados de la class cuenta
cuenta1 = cuenta("oscar garcia", 15000, "soles")
print(cuenta1.get_saldo())
print(cuenta1.get_propietario())
print(cuenta1.get_moneda())

    # Acá estamos modificando un valor (set), por ejemplo le deciamos que nos mostrara la moneda en la que estaba en al cuenta que eran soles, pues ahora con el metodo set cambiamos a dólarese imprimimos
cuenta1.set_moneda("Dolares")
print(cuenta1.get_moneda())