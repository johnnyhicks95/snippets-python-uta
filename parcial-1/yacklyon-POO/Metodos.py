#Clase 5
# class nombreDeClase
#     def nombreDelMetodo(self):
# self.nombreDeVariable= algoritmo

class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3
s = Matematica()
s.suma()
print(s.n1 + s.n2)

# metodo constructor
class Ropa:
    def __init__(self):
        # super().__init__()
        self.marca = 'versace'
        self.talla = 'm'
        self.color = 'rojo'

camisa = Ropa()
print(camisa.talla)
print(camisa.marca)

class Calculadora:
    def __init__(self, n1, n2):
        # super().__init__()
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2
operacion = Calculadora(2, 3)
print(operacion.producto)
print(operacion.suma)