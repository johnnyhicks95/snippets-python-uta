class Jugador:
    def __init__(self,cedula,nombres,estatura):
        self.cedula = cedula   #publico
        self._nombres = nombres #protected
        self.__estatura = estatura  #private

    #def __str__(self):
    #    return '{} ({})'.format(self._nombres, self.__estatura)

    def get_estatura(self):
        #print (self.__estatura)
        return self.__estatura

    def get_nombres(self):
        #print (self.__estatura)
        return self.__nombres

    def nombres(self):
        #print (self.__estatura)
        return self.__nombres    



    def impresionEstatura(self): 
        if self.__nombres=='Messi':
           self.set_estatura('2.05') 

        print (self.get_estatura())  

    def set_estatura(self,estatura):
        self.__estatura = estatura



class Equipo:
    jugadores = []
    def __init__(self,jugadores=[]):
        self.jugadores = jugadores

    def agregarJugador(self,j):
        self.jugadores.append(j)

    def mostrarJugadores(self):
        for j in self.jugadores:
            print ((j.nombres()))


j = Jugador('18000001','Messi','1.70')
#j.set_estatura('2.05')
j.impresionEstatura()
#print (j)
e = Equipo([j])
#e.mostrarJugadores()
e.agregarJugador(Jugador('18000002','Ronaldo','1.80'))
e.mostrarJugadores()


