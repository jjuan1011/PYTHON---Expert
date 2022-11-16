

#  CICLO FOR

# Le decimos que nos recorra que nos itere un rango o una estructura

for element in range(1, 20):
    print(element)

# Es decir le damos una estructura o un rango, en este caso es una estrutura de tipo lista y le decimo a element que recorra los varoles en la variable my_list
my_list = [23, 45,67,89,43]
for element in my_list:
    print(element)

# Acá tenemos un diccioanrio y le decimos a un iterador que en el pasado 
product = {
    'name':'adidas',
    'price': 100,   
    'stock': 25 
}
# Como es un dicionario nos toca ponerle otra sintaxis ya que si lo imprimimos así no más solo nos va a imprimir las llaves y no los valores
for key, value in product.items():
    print(key, '=>', value)

# Iterar diccionarios que se encuentran dentro de una lista, en este caso al iterador lo llamamos i 

industry = [
    {
        'name': 'Microsoft',
        'age':1975
    },

    {
        'name': 'IBM',
        'age': 1911
    },

    {
        'name': 'Apple',
        'age': 1976
    }
]

for i in industry:
    print('name =>', industry['name'])
    