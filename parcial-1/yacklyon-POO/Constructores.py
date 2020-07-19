# constructor: inicializa los valores iniciales
class Persona:
    def __init__(self, nombre , anio):
        # super().__init__()
        self.nombre= nombre
        self.anio = anio

    def descripcion(self):
        return '{} tiene {}'.format(self.nombre, self.anio)

    # metodo con atributo privado solo para ese metodo
    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre, frase)

doctor = Persona('Jose', 26)
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario("Hola que tal"))

# modificando atributos
class Email:
    def __init__(self):
        # super().__init__()
        self.enviado = False
    
    def enviarCorreo(self):
        self.enviado = True
miCorreo = Email()
print(miCorreo.enviado)
miCorreo.enviarCorreo()
print(miCorreo.enviado)