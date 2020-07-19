# crear una nueva clase a partir de una o mas clases existentes

# class NombreSubClase(NombreClaseSuperior)
# class ClaseBase:
#    Cuerpo de la clase Base
# class DerivadoClase(ClaseBase):
#   Cuerpo de clase derivada
class pokemon:
    pass
    def __init__(self, nombre , tipo):
        # super().__init__()
        self.nombre = nombre
        self.tipo = tipo
    
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre, self.tipo)

# clase hijo
class pikachu(pokemon):
    def ataque(self, tipoAtaque):
        return '{} tipo de ataque: {}'.format( self.nombre, tipoAtaque )

class charmander(pokemon):
    def ataque(self, tipoAtaque):
        return '{} tipo de ataque {}'.format(self.nombre, tipoAtaque)

nuevoPokemon = pikachu('baby', 'electrico')
print(nuevoPokemon.descripcion())
print(nuevoPokemon.ataque('impacto trueno'))