# 18 - julio - 2020
# construir un programa que :
# pida los datos de una asignatura
# pida los datos de un estudiante
# pida las notas del estudiante
# el codigo: una clase, se debe instanciar multiples objetos de manera dinamica
#  las variables deben declararse privadas, usar funciones decoradoras

# modelo del dict completo
# {
#   "asignatura1": {
#      "nombre": "Encantamientos",
#      "estudiantes": {
#          "pedro": {
#                "nota1": 8
#                "nota2": 8
#                "nota3": 10
#          },
#          "john": {
#                "nota1": 8
#                "nota2": 8
#                "nota3": 8
#       },
#
#   "asignatura2": {
#       "nombre": Pociones",
#       "estudiantes" : {
#            "mario" : {}
#                "nota1": 10
#           }
#       }
#   }

# constantes globales
NOMBRE_ASIGNATURA = "asignatura"
# dccionario asignaturas
dictAsignaturas = { }

# decorador
def saludar(funcParam):
    def funcDecorar(*args):
        print("")
        print("\tBienvenido")
        print("\tModulo 'Ingreso de asignaturas y estudiantes'")
        print()
        # inserto la funcion que necesito
        funcParam()
        print("")
        print("fin decorador. adios!")
        print("")
    return funcDecorar

# clases
class Asignatura:
    def __init__(self, nombreAsignatura):
        # super().__init__()
        self._nombreAsignatura = nombreAsignatura
        self._estudiantesListado = { }  # la clase estudiantes y su funcion

    def getAsignatura(self):
        return self._nombreAsignatura
    def setAsignatura(self, asignatura):
        self._nombreAsignatura = asignatura

    # funcion para insertar los datos signatura a un diccionario
    # es un decorador
    def setAsignaturas(self):
        # inicializador para el bucle
        siguiente = 'si'

        while siguiente == 'si':
            # contador para iterador
            i = 1
            # un nombre(clave) unico para el diccionario
            nombreAsignID = NOMBRE_ASIGNATURA + str(i)

            # ejecutar el ingreso de estudiantes
            crearEstudiante()

            # inserto el numero de asginatura al dict, con un valor de dict interno
            dictAsignaturas[nombreAsignID] = { 
                "nombre" : self._nombreAsignatura,
                # enlazo la lista estudiantes a la asignatura
                "estudiantes": self._estudiantesListado    
            }

            # pregunta para continuar o seguir insertando asignaturas
            print("")
            siguiente = input("¿Quieres añadir más asignaturas (si/no)? ").lower()
            # incremento el contador para el siguiente ID asignatura
            i+=1
    def setEstudiantes(self, estList):
        self._estudiantesListado = estList
    def getEstudiantes(self):
        return self._estudiantesListado

# ESTUDIANTES 
# clase de estudiantes y respectivas calificaciones
# dict estudiantes

estudiantesListado = {}

# preguntar el nombre del estudiante
# preguntar las 3 notas
# DECORADOR ?
# preguntar si quiere ingresar otro estudiante
# DECORADOR ?
# preguntar si quiere ingresar otra materia
class Estudiante:
    def __init__(self, nombre, dni, nota1, nota2, nota3):
        # super().__init__()
        self._nombre = nombre
        self._dni = dni
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3
    def setDatos(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni
    def setCalificaciones(self, nota1, nota2, nota3):
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3

    def getDatos(self):
        return self._nombre, self._dni
    def getCalificaciones(self):
        return self._nota1, self._nota2, self._nota3
    
    # funcion para ingresar datos al diccionario
    def setDatosDict(self):
        estudiantesListado[self._nombre] = {
            "nota-1" : self._nota1,
            "nota-2" : self._nota2,
            "nota-3" : self._nota3,
        }
# funcion para la clase Estudiante        
def crearEstudiante():
    # inicializador para el bucle
    siguiente = 'si'

    while siguiente == 'si':
        # pedir nombre y calificaciones
        print("")
        nombreEstud = input("Ingrese el nombre del estudiante: ").title()
        dniEstud = input("Ingrese el DNI del estudiante: ")
        nota1Est = float(input("Ingrese la nota 1: "))
        nota2Est = float(input("Ingrese la nota 2: "))
        nota3Est = float(input("Ingrese la nota 3: "))
        # instancia estudiantes
        estudiante1 = Estudiante(nombreEstud, dniEstud, nota1Est, nota2Est,nota3Est)
        estudiante1.setDatosDict()

        # pregunta para continuar o seguir insertando asignaturas
        print("")
        siguiente = input("¿Quieres añadir más estudiantes (si/no)? ").lower()
    return estudiantesListado

# inserto un decorador a la funcion PRINCIPAL
@saludar
# una funcion con ciclo para ingresar asignaturas
def main():
    # valor(value) del nombre asignatura con la primera letra en mayusc
    nombAsign = input("Ingrese el nombre de la asignatura: ").title()

    # instancio el objeto? : verificar si es necesario una clase*
    nombre = Asignatura(nombAsign)
    # ejecuto el metodo para enviar datos al dict
    nombre.setAsignaturas() # se ejecuta crear asignaturas y estudiantes**
    nombre.setEstudiantes(estudiantesListado)   # mando la lista externa a la variable interna de clase ASignatura
    print("")
    print("Imprimiendo la lista estudiantes desde el objeto")
    print(nombre.getEstudiantes())

# ejecuto la funcion
main()

# imprimo el diccionario con lo datos,
print("imprimiendo fuera del metodo")
# Warning: imprimiendo desde el objeto parece que no se imprime? pero los elemtos si estan
print(dictAsignaturas)
print("Imprimiendo listado estudiantes fuera de main")
print(estudiantesListado)

