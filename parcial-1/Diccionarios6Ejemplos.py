# Python - Nivel 20 - Reto 4 - Recorrer diccionarios. Métodos keys, values, items
#youtube
#los diccionarios son datos no ordenados por indice

# nivel 20 reto 1
telefonos = { 
    "Jose": 1234,
    "Maria": 3456
 } 
print(telefonos)

# para extraer el valor
print(telefonos["Maria"])

# buscando si contiene el valor
if "Julia" in telefonos:
    print(telefonos["Julia"])
else:
    print("Esa clave no existe")

telefonos["Jorge"] = 6543   # anadir un elemento
telefonos["Maria"] = 7890   # modifico el valor
del telefonos["Andres"]     # elimina el valor, si no contiene valor eliminara todos los valores



# nivel 20 reto 2 - agenda telefonica
telefonos = {
    "Jose": 1234,
    "Maria": 3456 ,
    "lucia": 7890,
    "Andres": 6543,
}
consultando = True

while consultando:
    print("Mis telefonos")
    print("-------------")
    print("1. consultar")
    print("2. Anadir")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Salir")
    print("---------")

    opcion = ""
    while opcion not in ("1","2","3","4","5"):
        opcion = input("-> ")
    if opcion == "1":
        nombre = input("Nombre: ")
        if nombre not in telefonos:
            print("Ese nombre no existe.")
        else:
            telf = telefonos[nombre]
            print(nombre, ":", telf)
    # opcion 2
    elif opcion == "2":
        nombre= input("Nombre: ")
        if nombre in telefonos:
            print("Ese nombre ya esta en la agenda")
        else:
            telf = int(input("telefono: "))
            telefonos[nombre] = telf
            print("El telefono se ha anadido correctamente")
    # opcion 3 modificar
    elif opcion == 3:
        nombre = input("Nombre: ")
        if nombre not in telefonos:
            print("Ese nombre no esta en la agenda. ")
        else:
            telf = int(input("Telefono: "))
            telefonos[nombre] = telf
            print("El telefono se ha modificado correctamente.")

    # opcion 4 borrar
    elif opcion == 4:
        nombre = input("Nombre:")
        if nombre not in telefonos:
            print("Ese nombre no esta en la agenda.")
        else:
            del telefonos[nombre]
            print("El telefono se ha borrado correctamente")
    
    # opcion salir
    elif opcion == "5":
        consultando = False
# Fin agenda


# Nivel 20 - Reto 3 -- Método get de los diccionarios
miAgenda = {
    "Alicia": 2222,
    "Roberto": 1111,
    "Lucia": 3333,
    "Andres": 5555
}
print(miAgenda.get("Jorge", "Esa clave no existe"))    # devuelveel valor, devuelve en caso no se encuentre

#comprobar las unidades que se encuentran enel inventario
inventario = {
    "Tornillos": 100,
    "Tuercas": 150,
    "Arandelas": 250
}
articulo = input("Articulo: ")
numero = inventario.get(articulo, 0)    # el valor, numero de unidades
print("{}: {}".format(articulo , numero))



# nivel 20 reto 4- Recorrer diccionarios. Métodos keys, values, items
miAgenda = {
    "Alicia": 2222,
    "Roberto": 1111,
    "Lucia": 3333,
    "Andres": 5555
}

for clave in miAgenda:  # como un map en js
    print(clave, ":", miAgenda[clave])  # recorro los elementos
#     Alicia: 2222,
#     Roberto: 1111,
#     Lucia: 3333,
#     Andres: 5555

# METODO keys: contiene solamente las claves
vistaClaves = miAgenda.keys()   # devuelvo en un a variable
vistaClaves = list(miAgenda.keys())   # lo puedo devolver como una lista
print(vistaClaves)
#dict_keys(['Alicia', 'Roberto', 'Lucia', 'Andres'])

for clave in vistaClaves:   # itero el objeti
    print(clave)
# Alicia
# Roberto
# Lucia
# Andres

# METODO VALUES
print(miAgenda.values())    # imprime solo los valores
if 1111 in miAgenda.values():
    print("Ese valor esta en el diccionario")

for valor in miAgenda.values(): # itero los valores
    print(valor)    
# 2222
# 1111
# 3333

# METODO ITEMS
print(miAgenda.items()) # mustra las parejas clave calor
for elemento in miAgenda.items():   # itero 
    print(elemento)
# ('Alicia', 2222)
# ('Roberto', 111)
# ('Lucia', 3333)
    print(elemento[0], elemento[1]) # formateo un poco
# Alicia 2222
# Roberto 111
# Lucia 3333
    # itero ambos
for clave, valor in miAgenda.items():
    print(clave, ":", valor)



# Nivel 20 - Reto 5 - Encontrar y listar valores de un diccionario
consultando = True
while consultando:
    print("Mis telefonos")
    print("-------------")
    print("1. Consultar por nombre")
    print("2. Consultar por telefono")
    print("3. Listar toda la agenda")
    print("5. Salir")
    print("---------")

    opcion = ""
    while opcion not in ("1","2","3","4"):
        opcion = input("-> ")

    # opcion 1
    if opcion == "1":
        nombre = input("Nombre: ")
        telf = telefonos.get(nombre, "Ese nombre no existe")
        print("{}: {}".format(nombre, telf))
    # opcion 2
    elif opcion == 2:
        telf = int(input("Telefono: "))
        if telf in telefonos.values():
            for nombre in telefonos:
                if telefonos[nombre] == telf:
                    print("{}: {}".format(telf, nombre))
        else:
            print("Ese telefono no esta en la agenda")
    # listar toda la agenda
    elif opcion == "3":
        for nombre, telf in telefonos.items():
            print("{}: {}".format(nombre, telf))

    elif opcion == "4":
        consultando = False


#  Nivel 20 - Reto 6 - Convertir listas a diccionario y diccionario a listas
# Convertir un diccionario en dos listas
pares = {"A": 1, "B":2, "C": 3, "D":4, "E": 5}

letras = []
numeros = []

for clave in pares:
    letras.append(clave)
    numeros.append(pares[clave])

print(letras)
print(numeros)
# usando items()
for clave, valor in pares.items():
    letras.append(clave)
    numeros.append(valor)

# usando funciones: keys y values
letras = list(pares.keys())
numeros = list(pares.values())

# -------------
# convertir dos listas en un diccionario
letras = ["A","B","C","D","E"]
numeros = [1,2,3,4,5]

pares = {}  # un diccionario vacio

for i in range (len(letras)):
    pares[letras[i]] = numeros[i]   # deben ser la misma cantidades de elementos
print(pares)

# mediante funcion zip
pares = dict(zip(letras, numeros))  #dict: crea un dicionario a partir de listas
print (pares) # imprime el diccionario clave valor



#----------------------
# Nivel 20 - Reto 7 - Contar las letras de un texto
# Contador de letras
frase = "Hoy ha salido el sol y hace un dia estupendo"

conteo = {}

for letra in frase.lower():
    if letra not in conteo:
        conteo[letra] = 1
    else:
        conteo[letra]+=1    # si encuentra la letra incrementa

for k, v in conteo.items():
    print("{}: {}".format(k ,v))    # cuenta una a uno las letrasy muestra


# -------------
# Nivel 20 - Reto 8 - Método setdefault de los diccionarios

materiales = {
    "cuadernos": 5,    
    "boligrafos": 7,    
    "reglas": 3,    
    "gomas": 4,    
}
articulo = input("Articulos: ")
unidades = materiales.get(articulo, 0)  # si no encuentra el articulo manda 0
print("Hay {} unidades de {}".format(unidades, articulo))

unidades = materiales.setdefault(articulo, 0)  # si no encuentra el articulo, lo crea con el valor del 
                                                # segundo argumento

# ----------------------
# Nivel 20 - Reto 10 - Método fromkeys
minerales = ["Pirita", "Topacio", "Cinabrio", "Obsidiana", "Manganita",
    "Alabastro", "Turquesa", "Galena"
]
coleccion = {}.fromkeys(minerales, 0)  # diccionario vacio= valor iterable, valor por defecto 

numeros = dict.fromkeys(range(100, 11), 50)    # crea un diccionario con keys del 100 al 110, con valor 50


# Diccionarios anidados
datos = {
    "familias": {
        "Cruise": {
            "Sofi": {"Grupo": "Azul"},
            "Lori": {"Grupo": "Rojo"}
        },

    },
    "Grupos": {
        'Azul': ['Sofi','Perita'],
        'Rojo': ['Lori']
    }
}

print(datos['familias']['Cruise'])
print(datos['familias']['Cruise']['Sofi'])  #{"Grupo": "Azul"},

#ingreso un dato: forma 1
nuevo = {"Grupo": "Verde"}
datos['familias']['Cruise']['Poppy'] = nuevo
print(datos['familias']['Cruise'])

#ingreso un dato: forma 2
otro={'Pip': {'Grupo': 'Azul'}}
datos['familias']['Cruise'].update(otro)
print(datos['familias']['Cruise'])

#ingreso un dato: forma 3
clave= 'Rupert'
valor= 'Rojo'
extra= {clave: valor}
datos['familias']['Cruise'].update(extra)
print(datos['familias']['Cruise'])