# importaciones librerias
import math

datosFigura=[]  # lista almacena : figura, datos: medidas
PI = math.pi

# una clase
class FigurasGeometricas:
    # declaro constantes

    # crear un constructor
    def __init__(self, dimension, datoEntrada):
        # super().__init__()
        # datoEntrada, dimension
        self.dimension = dimension
        self.datoEntrada= datoEntrada

    #metodos de clase
    def enviarDatos(self):
        pass

# metodos de archivo
def registrarFigura():
    print("Menu tipo de figura")
    control = True

    while control:
        print("""
        1. Cubo
        2. Tetraedro
        3. Pirámide cuadrada
        4. Hiperesfera
        5. Regresar        
        """)
        opcion=input()
        # opciones del menu 2
        if opcion == "1":
            print("  Datos Cubo ")  
            #calculo:volumen, superficie, espacio
            # input: datoEntrada, dimension
            dimension = 6
            datoEntrada=int(input("Ingrese la medida de la arista:"))

            figura = FigurasGeometricas(dimension, datoEntrada)
            datosFigura.append(figura)

        elif opcion == "2":
            print("  Datos Tetraedro ")  
            #calculo:volumen, superficie, espacio
            # input: datoEntrada, dimension
            dimension = 4
            datoEntrada=int(input("Ingrese la medida de la arista:"))

            figura = FigurasGeometricas(dimension, datoEntrada)
            datosFigura.append(figura)

        elif opcion == "3":
            print("  Datos Piramide cuadrada ")  
            #calculo:volumen, superficie, espacio
            # input: datoEntrada, dimension
            dimension = 5
            datoEntrada=int(input("Ingrese la medida de la arista:"))

            figura = FigurasGeometricas(dimension, datoEntrada)
            datosFigura.append(figura)

        elif opcion == "4":
            print("  Datos Hiperesfera ")  
            #calculo: hiper volumen, hiper area
            # input: radio, pi(es constante)
            dimension = 1
            radio = float(input("Ingrese el valor del radio"))

            figura = FigurasGeometricas(dimension, radio)
            datosFigura.append(figura)
        elif opcion == "5":
            print("De vuelta al menu principal")
            print("")
            control = False
        else:
            print("Comando desconocido, intente de nuevo")
            print("")

def calcularVolumen():
    print("Cálculo de volumen")
    for figura in datosFigura:
        if figura.dimension == 6:
            volumen = figura.datoEntrada**3
            print("El volumen del cubo es: {}".format(volumen))
        if figura.dimension==4:
            volumen = ( (pow(2, 1/2)/12) * pow(figura.datoEntrada, 3) )
            print("El volumen del tetraedro es: {}".format(volumen))
        if figura.dimension==5:
            volumen = ((pow(2, 1/2)/12) * figura.datoEntrada**3 )
            print("El volumen de la piramide cuadrada es: {}".format(volumen))

def calcularSuperficie():
    print("Calculos de superficie")
    for figura in datosFigura:
        if figura.dimension == 6:
            superficie = (6 * (figura.datoEntrada**2))
            print("La superficie del cubo es: {}".format(superficie))
        if figura.dimension==4:
            superficie = ( (pow(3, 1/2)) * pow(figura.datoEntrada, 2) )
            print("La superficie del tetraedro es: {}".format(superficie))
        if figura.dimension==5:
            superficie = ( ( 1+ pow(3, 1/2)) * (pow(figura.datoEntrada,2))  )
            print("La superficie de la piramide cuadrada es: {}".format(superficie))

def calcularEspacio():
    print("Calculo de espacio")
    for figura in datosFigura:
        if figura.dimension == 6:
            espacio = ( pow(figura.datoEntrada, figura.dimension)  )
            print("El espacio del cubo es: {}".format(espacio))

        if figura.dimension==4:
            espacio = ( pow(figura.datoEntrada, figura.dimension)  )
            print("El espacio del tetraedro es: {}".format(espacio))

        if figura.dimension==5:
            espacio = ( pow(figura.datoEntrada, figura.dimension)  )
            print("El espacio de la piramide cuadrada es: {}".format(espacio))

def calcularHiperVolumen():
    for figura in datosFigura:
        if figura.dimension ==1:
            print("Calculo de hiper volumen")
            hiperVolumen= ((pow(figura.datoEntrada,4)) * (pow(PI,2)/2) )
            print("El resultado es: {}".format(hiperVolumen))

def calcularHiperArea():
    for figura in datosFigura:
        if figura.dimension ==1:
            print("Calculo de hiper area")
            hiperArea= ( (2 * (pow(PI,2)*pow(figura.datoEntrada,3))) )
            print("El resultado es: {}".format(hiperArea))

def salir():
    print("Cerrando programa!")
    print("Adiós!")
    exit()

# menu principal
def main():
    while True:
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Tipo de figura ")
        print("2.- Cálculo de volumen")
        print("3.- Cálculo de la superficie")
        print("4.- Cáculo del espacio (solo para el cubo y el tetaedro)")
        print("5.- Cálculo del Hiper-Volumen (Solo para la Hiperesfera)")
        print("6.- Cálculo del Hiper área (Solo para la Hiperesfera)")
        print("7.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            registrarFigura()
        elif opcion == 2:
            calcularVolumen()
        elif opcion == 3:
            calcularSuperficie()
        elif opcion == 4:
            calcularEspacio()
        elif opcion == 5:
            calcularHiperVolumen()
        elif opcion == 6:
            calcularHiperArea()
        elif opcion == 7:
            salir()

if __name__ == '__main__':
    main();