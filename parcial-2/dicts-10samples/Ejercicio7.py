# Escribir un programa que cree un diccionario simulando una cesta de la compra.
#  El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista 
# de la compra y el coste total, con el siguiente formato

#       Lista de la compra	 
#       Artículo 1	Precio
#       Artículo 2	Precio
#       Artículo 3	Precio
#       …	…
#       Total	Coste

basket = {}
more = 'Si'
while more == 'Si':
    item = input('Introduce un artículo: ')
    price = float(input('Introduce el precio de ' + item + ': '))
    basket[item] = price
    more = input('¿Quieres añadir artículos a la lista (Si/No)? ')
cost = 0
print('Lista de la compra')
for item, price in basket.items():
    print(item, '\t', price)
    cost += price
print('Coste total: ', cost)

# output:
# Introduce un artículo:  Ordenador
# Introduce el precio de Ordenador:  450.5
# ¿Quieres añadir artículos a la lista (Si/No)?  Si
# Introduce un artículo:  Tablet
# Introduce el precio de Tablet:  230
# ¿Quieres añadir artículos a la lista (Si/No)?  Si
# Introduce un artículo:  Teléfono
# Introduce el precio de Teléfono:  121.2
# ¿Quieres añadir artículos a la lista (Si/No)?  No
# Lista de la compra
# Ordenador 	 450.5
# Tablet 	 230.0
# Teléfono 	 121.2
# Coste total:  801.7