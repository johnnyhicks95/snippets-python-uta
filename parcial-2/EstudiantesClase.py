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
        

# pedir nombre y calificaciones
nombreEstud = input("Ingrese el nombre del estudiante: ").title()
dniEstud = input("Ingrese el DNI del estudiante: ")
nota1Est = float(input("Ingrese la nota 1: "))
nota2Est = float(input("Ingrese la nota 2: "))
nota3Est = float(input("Ingrese la nota 3: "))

# instancia estudiantes
estudiante1 = Estudiante(nombreEstud, dniEstud, nota1Est, nota2Est,nota3Est)
estudiante1.setDatosDict()
# print("Datos ",list(estudiante1.getDatos()))
# print("Notas:", list(estudiante1.getCalificaciones()))

# enviar datos al dicccionario
# estudiantesListado[nombreEstud] = {}
print(estudiantesListado)