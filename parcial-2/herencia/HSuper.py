class Persona():
    def __init__(self, nombre, edad, lugarResidencia):
        # super().__init__()
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia

    def descripcion(self):
        print('Nombre: ', self.nombre, 'Edad:',self.edad, ' Residencia:', self.lugarResidencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        # super().__init__('Antonio', 55, 'Colombia')
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        # HEREDO EL METODO
        # primero ejecutara el metodo del padre, luego este (hijo)
        super().descripcion()
        print('Salario: ', self.salario, ' Antiguedad: ', self.antiguedad )
    

# ***********
Antonio = Persona('Antonio', 55, 'Colombia')
# Antonio.descripcion()
print()
Antonio = Empleado(1500, 30, 'Manuel', 28, 'Peru')
Antonio.descripcion()

print(isinstance(Manuel, Empleado))  # compruebo que es un objeto