

# MAP CON DICCIONARIOS

# En esta clase vamos a aplicar el map pero a la estructura de datos de tipo diccionario

items = [
{
    'prodcut': 'camisa',
    'price': 100
},
{
    'product': 'pantalones',
    'price': 200
},
{
    'product': 'zapatos',
    'price': 200
}
]

prices = list(map(lambda i: i['price'], items))
print(prices)

# Vamos a agregar un nuevo elemento a dicha lista, en este caso estamos agregando el atributo impuesto
def add_iva(item):
    item['iva'] = item['price'] * .19
    return item

new_items = list(map(add_iva, items))

print("new list")
print(new_items)
print("lista original")
print(items)

