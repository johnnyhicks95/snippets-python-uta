# 08 de julio 2020
#  objetos dentro de objetos
# Clase Jugador
# Clase Equipo
# Clase Campeonato
# Clase Pais
# Teniendo en cuenta lo anterior, analicemos lo siguiente:

# Un jugador pertenece a un equipo
# Un equipo pertenece a un campeonato
# Un campeonato pertenece a un país
# **** usar solamente variables protegidas y privadas

class Jugador:
    pass
    def __init__(self):
        # super().__init__()
        self._cedula = 0000
        self._nombre = ""
        self._estatura = 0

    #metodos setters
    def setCedula(self, cedula):
        self._cedula = cedula

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEstatura(self, estatura):
        self._estatura = estatura

    # metodos getters
    def getCedula(self):
        return self._cedula

    def getNombre(self):
        return self._nombre

    def getEstatura(self):
        return self._estatura
    
    # mostrar los atributos
    def getJugador(self):
        print("\t* Datos jugador *")
        print("Nombre: ", self._nombre)
        print("Cedula: ", self._cedula)
        print("Estatura: ", self._estatura)

class Equipo:
    jugadores = [] # va a almacenar

    def __init__(self, jugadores=[]):
        # super().__init__()
        self._jugadores = jugadores
        self._nombreEquipo = ""

    def setNombreEquipo(self, nombre):
        self._nombreEquipo=nombre
    def getNombreEquipo(self):
        # print("Nombre del equipo:",self._nombreEquipo) # no descomentar, imprime otra vez si se ejecuta
        return self._nombreEquipo

    def setAgregarJugador(self, jugador):
        self.jugadores.append(jugador)

    def getMostrarEquipo(self):
        print("\t* Lista de jugadores *")
        for jugador in self.jugadores:
            print( "->",(jugador.getNombre()) )

class Campeonato:
    tablaCampeonatos = []

    def __init__(self, tablaCampeonatos=[]):
        # super().__init__()
        self._tablaCampeonatos = tablaCampeonatos
        self._nombreCampeonato=""
    
    def setNombreCampeonato(self, nombre):
        self._nombreCampeonato = nombre
    
    def getNombreCampeonato(self):
        # print("Nombre del campeonato:",self._nombreCampeonato)
        return self._nombreCampeonato
    
    def setAgregarEquipo(self, equipo):
        self.tablaCampeonatos.append(equipo)

    def getCampeonatos(self):
        print("Listado equipos en el campeonato")
        for equipo in self.tablaCampeonatos:
            print("=>",(equipo.getNombreEquipo()))


class Pais:
    listaCampeonatos = []

    def __init__(self, listaPaises=[]):
        # super().__init__()
        self._listaPaises = listaPaises
        self._nombrePais = ""
    
    def setNombrePais(self, nombre):
        self._nombrePais = nombre
    
    def getNombrePais(self):
        print("Nombre del pais:", self._nombrePais)
        return self._nombrePais

    def setAgregarCampeonato(self, campeonato):
        self.listaCampeonatos.append(campeonato)
    
    def getPaises(self):
        print("Campeonatos: ")
        for campeonato in self.listaCampeonatos:
            print("**:",campeonato.getNombreCampeonato())


# tests
# jugador 1: Bruno Borges
JugadorBorges = Jugador()
JugadorBorges.setCedula(7777)
JugadorBorges.setNombre("Bruno Borges")
JugadorBorges.setEstatura(1.79)
JugadorBorges.getJugador() # imprime datos del jugador 1

# equipo 1 : Manchester United
print()
ManchesterUnited = Equipo()
ManchesterUnited.setNombreEquipo("Manchester United")
ManchesterUnited.setAgregarJugador(JugadorBorges)
ManchesterUnited.getNombreEquipo()
ManchesterUnited.getMostrarEquipo()

# Campeonato: Premier League
print()
PremierLeague = Campeonato()
PremierLeague.setNombreCampeonato("Premier League")
PremierLeague.setAgregarEquipo(ManchesterUnited)
PremierLeague.getNombreCampeonato()
PremierLeague.getCampeonatos()

# Pais: Inglaterra
print()
Inglaterra = Pais()
Inglaterra.setNombrePais("Inglaterra")
Inglaterra.setAgregarCampeonato(PremierLeague)
Inglaterra.getNombrePais()
Inglaterra.getPaises()
