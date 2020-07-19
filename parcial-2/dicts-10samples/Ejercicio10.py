# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente 
# será su NIF, y el valor será otro diccionario con los datos 
# del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente 
# tendrá el valor True si se trata de un cliente preferente. El programa debe
#  preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, 
#  (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, 
#  (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida
#   el programa tendrá que hacer lo siguiente:

# 1.Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# 2.Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 3.Preguntar por el NIF del cliente y mostrar sus datos.
# 4.Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 5.Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# 6.Terminar el programa.

clients = {}
option = ''
while option != '6':
    if option == '1':
        nif = input('Introduce NIF del cliente: ')
        name = input('Introduce el nombre del cliente: ')
        address = input('Introduce la dirección del cliente: ')
        phone = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        client = {'nombre':name, 'dirección':address, 'teléfono':phone, 'email':email, 'preferente':vip=='S'}
        clients[nif] = client
    if option == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clients:
            del clients[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if option == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clients:
            print('NIF:', nif)
            for key, value in clients[nif].items():
                print(key.title() + ':', value)
        else:
            print('No existe el cliente con el nif', nif)
    if option == '4':
        print('Lista de clientes')
        for key, value in clients.items():
            print(key, value['nombre'])
    if option == '5':
        print('Lista de clientes preferentes')
        for key, value in clients.items():
            if value['preferente']:
                print(key, value['nombre'])
    option = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')

# output:
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 1
# Introduce NIF del cliente:  11111111A
# Introduce el nombre del cliente:  Pepito Pérez
# Introduce la dirección del cliente:  Madrid
# Introduce el teléfono del cliente:  666555444
# Introduce el correo electrónico del cliente:  pepito@gmail.com
# ¿Es un cliente preferente (S/N)?  S
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 1
# Introduce NIF del cliente:  22222222B
# Introduce el nombre del cliente:  Paquito Fernández
# Introduce la dirección del cliente:  Barcelona
# Introduce el teléfono del cliente:  666333222
# Introduce el correo electrónico del cliente:  paquito@gmail.com
# ¿Es un cliente preferente (S/N)?  N
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 4
# Lista de clientes
# 11111111A Pepito Pérez
# 22222222B Paquito Fernández
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 5
# Lista de clientes preferentes
# 11111111A Pepito Pérez
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 3
# Introduce NIF del cliente:  222
# No existe el cliente con el nif 222
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 3
# Introduce NIF del cliente:  22222222A
# No existe el cliente con el nif 22222222A
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 22222222B
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 3
# Introduce NIF del cliente:  22222222B
# NIF: 22222222B
# Nombre: Paquito Fernández
# Dirección: Barcelona
# Teléfono: 666333222
# Email: paquito@gmail.com
# Preferente: False
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 2
# Introduce NIF del cliente:  22
# No existe el cliente con el nif 22
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar
# Elige una opción: 2
# Introduce NIF del cliente:  22222222B
# Menú de opciones
# (1) Añadir cliente
# (2) Eliminar cliente
# (3) Mostrar cliente
# (4) Listar clientes
# (5) Listar clientes preferentes
# (6) Terminar