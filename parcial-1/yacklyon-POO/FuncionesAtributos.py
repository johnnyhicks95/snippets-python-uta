
class Persona:
    edad = 27
    nombre = 'victor'
    pais = "brazil"

doctor = Persona()
print("la edad es:",doctor.edad)
print('la edad es:', getattr(doctor, 'edad'))

# va a devolver un boolean indica si existe o no un atributo
print("el doctor tiene una edad?", hash(doctor, 'edad'))    #True

#
print("Antes era ",doctor.nombre)
#cambio el valor de nombre
setattr(doctor, 'nombre', 'hector') #hector
#elimino un valor por el nombre de clase y el atributo
delattr(Persona, 'pais')
print(doctor.pais)  #object has no attribute