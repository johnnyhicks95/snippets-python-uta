# fecha 22 de julio 2020
# taller sobre simlar sistema de calificaciones  a estudiantes
# per o usando las clases que sea nnecesarias e instanciado objetos

# el diccionario principal tendra dos campos o keys
# dictPrincipal {
# minimo 5 asignaturas
#   "cedula": '123456',
#   calificaciones : {
#   "matematicas" : 8,
#   "calculo" : 9,
#   "fisica" : 7,
#   "ciencias" : 8,
#   "politica" : 9,
#   }
# }
#
#

# variables o elementos globales
dictPrincipal = {}	# este diccionario obtiene la cedula y las asignaturas con las notas
# almacena la asignatura y su nota
dictNotas = {}	
# almacena los objetos
dictEstudiantes = {}


class Estudiante:
	# constructor
	def __init__(self, nombre="John Doe", dni=111111, calificacion=0, asignaturas={}):
		# super().__init__()
		self._nombre = nombre
		self._dni = dni
		self._calificacion = calificacion
		self._asignaturas = asignaturas
	# cambia los datos del estudiante

	def setDatosEst(self, nombre, dni):
		self._nombre = nombre
		self._dni = dni
	# que retorne el nombre y dni

	def getDniEst(self):
		return self._dni
	def getNombreEst(self):
		return self._nombre
	def getCalificacion(self):
		return self._calificacion
	def getAsignaturas(self):
		return self._asignaturas

	def setCalificaciones(self):
		for asignatura, nota in dictNotas.items():
			nota = self._calificacion
			# dictNotas[asignatura] = {
			# 		nota = self._calificacion
			# }

	# fin clase Estudiante

# while repitiendo pedir asignaturas
def ingresarCalificaciones(): 
	# control para ingreso de calificaciones
	contadorAsign = 1
	siguiente = 'si'
	while siguiente == 'si':
		while contadorAsign <= 5:  # 5 asignaturas
			# print("...............")
			clave = input("¿Qué asignatura quieres introducir?: ").title()
			nota = input( clave + ' su nota es: ')
			dictNotas[clave] = nota
			print(dictNotas)
			# incremento el contador de asignaturas
			contadorAsign += 1
			print("...............")
			# print("")
		# control para seguir\parar
		siguiente = input('¿Quieres añadir más asignaturas (Si/No)?: ')

# pruebo la funcion este asignando las asignaturas y calificaciones: CHECKED
# ingresarCalificaciones()
# print('Notas ingresadas: ',dictNotas)

# funcion ingresar estudiante
def ingresarEstudiantes():
	i= '1'  # numero que se agregara al final de la clave 
	estudiante = {}
	siguiente = 'si'

	nombreEst = input('¿Qué nombre quieres introducir?: ').title()
	dni = int(input(nombreEst + ', ingrese DNI: '))
	# instancio la clase
	nuevoEst = Estudiante(nombreEst, dni)
	# llamo el dni y mando al dict prinipal
	nuevoDni = str(nuevoEst.getDniEst())
	dictPrincipal['cedula'+i] = nuevoDni	# este envia datos a la impresion de resultados
	dictPrincipal[nuevoDni] = nuevoEst	# aqui envio al dict todo el objeto
	print()

ingresarEstudiantes()
print('Diccionario estudiantes -> ',dictPrincipal)

# promedio de calificaciones
def promedioCalificaciones():
	sumaNotas= 0
	promedio = 0
	cantNotas = 5
	# pedir de quien quiere obtener el promedio
	dniBusqueda = input('Ingrese el DNI de quien buscar el promedio: ')
	for dniBusqueda, numero in dictPrincipal.items():
		for clave, valor in dictEstudiantes.items():
			sumanotas += valor 
			promedio = sumaNotas / 5
			print(dniBusqueda, 'tiene', promedio)
	# if nombre == 

# estudiante con el puntaje mas alto
def getPuntajeAlto():
	pass

# reporte con perdidos, nota menor a 6
def getPerdidos():
	pass