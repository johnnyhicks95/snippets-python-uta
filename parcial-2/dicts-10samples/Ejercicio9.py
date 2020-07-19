# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el 
# número de factura y el valor el coste de la factura. El programa debe preguntar al 
# usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y su 
# coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará 
# por el número de factura y se eliminará del diccionario. Después de cada operación 
# el programa debe mostrar por pantalla la cantidad cobrada hasta el momento
#  y la cantidad pendiente de cobro.

invoices = {}
collected = 0
remains = 0
more = ''
while more != 'T':
    if more == 'A':
        key = input('Introduce el número de la factura: ')
        cost = float(input('Introduce el coste de la factura: '))
        invoices[key] = cost
        remains += cost
    if more == 'P':
        key = input('Introduce el número de la factura a pagar: ')
        cost = invoices.pop(key, 0)
        collected += cost
        remains -= cost
    print('Recaudado:', collected)
    print('Pendiente de cobro: ', remains)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')

# output:
# Recaudado: 0
# Pendiente de cobro:  0
# ¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  A
# Introduce el número de la factura:  1
# Introduce el coste de la factura:  150
# Recaudado: 0
# Pendiente de cobro:  150.0
# ¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  A
# Introduce el número de la factura:  2
# Introduce el coste de la factura:  300
# Recaudado: 0
# Pendiente de cobro:  450.0
# ¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  P
# Introduce el número de la factura a pagar:  2
# Recaudado: 300.0
# Pendiente de cobro:  150.0
# ¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  A
# Introduce el número de la factura:  3
# Introduce el coste de la factura:  85
# Recaudado: 300.0
# Pendiente de cobro:  235.0
# ¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  P
# Introduce el número de la factura a pagar:  1
# Recaudado: 450.0
# Pendiente de cobro:  85.0
# ¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  T