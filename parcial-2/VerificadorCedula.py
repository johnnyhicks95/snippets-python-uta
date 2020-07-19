# crear una clase persona y validar su numero de cedula con el algoritmo
# POO - 011 de julio 2020

import math

    # constructor
    # son 10 digitos
    # los primeros 9 según las posiciones donde se encuentren :
    #       Impares:
    #           - cada digito se multiplica por 2 y se suman todos los digitos .
    #           -  si la suma total es mayor a 9 se resta 9
    #       PAres:  
    #           -  se suman los digitos en posiciones pares
    #           -  se suman los Eimpares con los Epares
    # Obtener el modulo(10) de las dos sumas (29 , mod(10) = 9
    #       - si el modulo es cero, ese es el numero verificador
    #       - si no, de 10 se resta el modulo ( 10 - 6 = 4, 3 es el numero verificador)
    # 
class Persona:

    def __init__(self, nombre="John", apellido="Doe", numCedula="1804981890", digitosLista=[], 
    sumaPares=0, sumaImpares=0, modulo=0):
        # super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.numCedula = numCedula
        self.digitosLista = digitosLista
        self.sumaPares = sumaPares
        self.sumaImpares = sumaImpares
        self.modulo = modulo
    # Metodos
    def calcularImpares(self):
        listaDigitos = []
        for i in self.numCedula:
            listaDigitos.append(i) # los agrego a lista de constructor
        listaDigitos.pop()  # quito el ultimo elemento

        print(listaDigitos)

        impares = []    # lsita auxiliar para lmacenar los impares

        for i in range(0,10, 2):
            impares.append(listaDigitos[i] )
        
        print("Lista impares:",impares)
        # multiplicar por 2 cada digito
        for impar in impares:
            if int(impar) * 2 < 9:
                self.sumaImpares += int(impar) * 2
            else:
                # si la multiplicacion da mayor que 9 , a eso se resta 9 y se guarda a lasuma general
                self.sumaImpares +=(int(impar) * 2) -9
        return self.sumaImpares


    def calcularPares(self):
        listaDigitos = []
        for i in self.numCedula:
            listaDigitos.append(i) # los agrego a lista de constructor
        listaDigitos.pop()  # quito el ultimo elemento
        pares = []    # lsita auxiliar para lmacenar los impares

        for i in range(1,9,2):
            pares.append(listaDigitos[i])
         
        print("Lista pares:",pares)
        # sumo los elementos 
        for digito in pares:
            self.sumaPares += int(digito)
        # print(self.sumaPares)   # la suma de los digitos
        return self.sumaPares

    def obtenerModulo(self):
        self.modulo = (self.sumaImpares + self.sumaPares)% 10
        return self.modulo 

    def comprobarVerificador(self):
        pass
        if self.modulo == 0:
            # si es cero . no se modifica y queda como num verificador
            print("El digito verificador es: ", self.modulo)
        else:
            # encuentro la decena arriba mas cerca y resto con la suma anterior
            self.modulo = (math.ceil(self.modulo/10) * 10) - self.modulo
            return self.modulo
    
    # funcion principal
    def main(self):
        # deben ser 10 digitos
        longCed = len(self.numCedula)
        valido = False  # comprueba si es (True) valida o no(False)

        if longCed != 10:
            print("Compruebe e ingrese que sean 10 dígitos")
        else: 
            print("Proceso de verificacion de validez ")
            print()
            self.apellido=input("Ingrese su nombre:")
            print("Bienvenido senio:", self.apellido)
            # no reconoce los mteodos par aejecutarlos desde una sola funcion
            # calcularImpares()
            # calcularPares()
            # obtenerModulo()
            # comprobarVerificador()

# tests
testPersona1 = Persona()
# print(testPersona1.numCedula)
# print(testPersona1.main())
print()
print("La suma de los impares",testPersona1.calcularImpares())
print("La suma de los pares",testPersona1.calcularPares())
print()
print("El modulo de las sumas",testPersona1.obtenerModulo())
print(testPersona1.comprobarVerificador())
# print(testPersona1.main())
