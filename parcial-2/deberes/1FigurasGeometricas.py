# sacar el area de al menos 4 figuras geometricas
# y calcular su area usando herencia

class Figura():
    def __init__(self, nombre, datoX=0, datoY=0):
        # super().__init__()
        pass
        self.nombre = nombre
        self.datoX = datoX
        self.datoY = datoY
        self.areaRes = 0

    def calcularArea(self):
        print('la figura: ',self.nombre)
        print('La base',self.datoX, ' ; de altura: ', self.datoY)

# una subclase
class Cuadrado(Figura):
    pass
    def calcularArea(self):
        super().calcularArea()
        # HEREDO EL METODO
        # primero ejecutara el metodo del padre, luego este (hijo)
        print('Area: ', self.datoX * self.datoX)

class Rectangulo(Figura):
    pass
    pass
    def calcularArea(self):
        super().calcularArea()
        # HEREDO EL METODO
        # primero ejecutara el metodo del padre, luego este (hijo)
        print('Area: ', self.datoX * self.datoY, 'metros')
class Triangulo(Figura):
    pass
    def calcularArea(self):
        super().calcularArea()
        # HEREDO EL METODO
        # primero ejecutara el metodo del padre, luego este (hijo)
        print('Area: ', (self.datoX * self.datoX)/2, 'metros')
class Paralelogramo(Figura):
    pass
    def calcularArea(self):
        super().calcularArea()
        # HEREDO EL METODO
        # primero ejecutara el metodo del padre, luego este (hijo)
        print('Area: ', (self.datoX * self.datoX), 'metros')

nombre = input('Ingrese el tipo de figura:')
base = int(input('Ingrese la base(en metros): '))
altura = int(input('Ingrese la altura(en metros): '))

testCuadrado = Cuadrado(nombre, base, altura,)
testCuadrado.calcularArea()

testTriangulo= Triangulo(nombre, base, altura)
testTriangulo.calcularArea() 
