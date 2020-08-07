class Vehiculos():
    def __init__(self, marca, modelo):
        # super().__init__()
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca: ',self.marca, '\nModelo: ', self.modelo, '\nEn marcha: ', self.enMarcha,
        '\nAcelerando: ', self.acelera, '\nFrenado: ', self.frena
        )

# heredo
class Moto(Vehiculos):
    pass
    # propiedades propias
    hCaballito = ''
    def caballito(self):
        self.hCaballito='Voy haciendo el caballito'

    # sobreescribo el metodo de la clase padre
    def estado(self):
        print('Marca: ',self.marca, '\nModelo: ', self.modelo, '\nEn marcha: ', self.enMarcha,
        '\nAcelerando: ', self.acelera, '\nFrenado: ', self.frena, '\nCaballito: ', self.hCaballito
        )
# otra clase hijo heredada
class Furgoneta(Vehiculos):
    pass

    def carga(self, cargar):
        self.cargado = cargar

        if(self.cargado):
            return 'La furgoneta esta cargada'
        else:
            return 'La furgoneta no esta cargada'
        
# otra clase padre
class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

# &********************************
#instancio
miMoto = Moto('Suzuki', 'XZR')
miMoto.caballito()  # ejecuto el metodo en el hijo
miMoto.estado() # recibo la nueva info sobreescrita del hijo
print('')

# la otra clase hija
miFurgoneta = Furgoneta('Renault', 'Kangoo')
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

# HERENCIA MULTIPLE
# de la clase padre VElectricos
class BicicletaElectrica(Vehiculos, VElectricos):
    pass

miBici=BicicletaElectrica('BMX', '123A')