
x = 1

while True:
    # el codigo que va a ejecutar una vez
    print (x)
    x = x+1

    #condiciona para cerrar el ciclo
    if x >= 5:
        break # cerrara el ciclo cuando llegue a True en la condicion

print("Fin while")


# version 2
import random
print("Adivina un numero entre 1 y 5")

while True:
    # blque de codigo
    num= int(input("Introduce un numero:"))
    magia = random.randint(1,5)

    if num == magia:
        print("Ganaste! ")

    else:
        print("Perdiste\n el numero es:")
        print(magia)
    # termina bloque de codigo

    #Inicia comrobacion
    turno = int(input("Juegas otra vez? (1 Si) (2 No)"))
    if turno != 1:  # mientras el input no sea 1, siempre ejecutara el bucle while
        break   # cierra el programa

print("hasta luego! kayakaman!")