# Parte 3

#Clase
class Auto:
    marca = ""
    modelo = 2006
    placa = ""

taxi = Auto()
print(taxi.modelo)

# Parte 2
# class Persona:
#     doctor = 'Victor'
# print(Persona.doctor)

class JugadoresA:
    j1 = 'Messi'
    j2 = 'C. Ronaldo'

# print(JugadoresA.j2)

class JugadoresB:
    j3 = 'Marcelo'
    j1 = 'Falcao'

# print(JugadoresB.j3)


class nombre:
    pass

victor = nombre()
maria = nombre()

# objeto.atributo= valor
victor.edad= 30
victor.sexo = 'masculino'
victor.pais = 'Bolivia'

maria.edad=25
maria.sexo='femenino'
maria.pais='Colombia'

print(victor.edad)
print(maria.edad)
