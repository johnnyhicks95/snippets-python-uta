# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
# sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse
#  el contenido del diccionario.

person = {}
more = 'Si'
while more=='Si':
    key = input('¿Qué dato quieres introducir? ')
    value = input(key + ': ')
    person[key] = value
    print(person)
    more = input('¿Quieres añadir más información (Si/No)? ')

# output:
# ¿Qué dato quieres introducir?  Nombre
# Nombre:  Alfredo Sánchez
# {'Nombre': 'Alfredo Sánchez'}
# ¿Quieres añadir más información (Si/No)?  Si
# ¿Qué dato quieres introducir?  Dirección
# Dirección:  Madrid
# {'Nombre': 'Alfredo Sánchez', 'Dirección': 'Madrid'}
# ¿Quieres añadir más información (Si/No)?  Si
# ¿Qué dato quieres introducir?  email
# email:  asalber@ceu.es
# {'Nombre': 'Alfredo Sánchez', 'Dirección': 'Madrid', 'email': 'asalber@ceu.es'}
# ¿Quieres añadir más información (Si/No)?  No