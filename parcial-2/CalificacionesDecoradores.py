# 18 - julio - 2020
# construir un programa que :
# pida los datos de una asignatura
# pida los datos de un estudiante
# pida las notas del estudiante
# el codigo: una clase, se debe instanciar multiples objetos de manera dinamica
#  las variables deben declararse privadas, usar funciones decoradoras


class Persona:
    def __init__(self, cedula, nombre, ciudad):
        # super().__init__()
        self.cedula = cedula
        self.nombre = nombre
        self.ciudad = ciudad

    def agregarPersona(self):
        pass
        # print(self.cedula)

personas = {}
i=1
while i <= 5:
    personas[i] = Persona(i, "juan", "Ambato")
    personas[i].agregarPersona()
    i+=1

print(personas)