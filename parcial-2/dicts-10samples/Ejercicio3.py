# Escribir un programa que guarde en un diccionario los precios de las frutas 
# de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por
#  pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el
#  diccionario debe mostrar un mensaje informando de ello.

#       Fruta	Precio
#       Plátano	1.35
#       Manzana	0.80
#       Pera	0.85
#       Naranja	0.70

fruits = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruit = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruit in fruits:
    print(kg, 'kilos de', fruit, 'valen', fruits[fruit]*kg )
else: 
    print("Lo siento, la fruta", fruit, "no está disponible.")

# output:
# ¿Qué fruta quieres?  pera
# ¿Cuántos kilos?  3.5
# 3.5 kilos de Pera valen 2.975