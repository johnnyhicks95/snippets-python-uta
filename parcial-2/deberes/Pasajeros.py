# crear una clase padre que describa un pasajero
# el pasajero igresa el pasaporte o cedula si es nacional
# las clases hijas deben heradar caracteristicas y metodos necesarios
# se debe verificar si el numero de cedula es correcto

#_modulos importados
import math


# clase Padre: Pasajero
class Pasajero():
    def __init__(self, nombrePasajero,tipoPasaje):
        # super().__init__()
        self._nombrePasajero = nombrePasajero
        self._tipoPasaje = tipoPasaje

    def descripcion(self):
        print('Nombre: ', self._nombrePasajero, 'tipo Pasaje:',self._tipoPasaje)

class Nacional(Pasajero):
    def __init__(self, codigo, ciudadResidencia , nombrePasajero, tipoPasaje):
        super().__init__(nombrePasajero, tipoPasaje)
        self._codigo = codigo
        self._ciudadResidencia = ciudadResidencia
        self._digitosLista = []
        self._sumaPares = 0
        self._sumaImpares = 0
        self._modulo = 0
        self._valido = "no valido"    # cuando sea verdadero es poque la cedula es valida

    # sobrrescribo la descipcion del padre
    def descripcion(self):
    # HEREDO EL METODO
        # primero ejecutara el metodo del padre, luego este (hijo)
        super().descripcion()
        print('Ciudad de residencia: ', self._ciudadResidencia, ' Validez de cedula: ', self._valido )
    
    # verificacion
    def validarCedula(self):
        print('Validando cedula ...')
        # self._codigo
            # Metodos
        def calcularImpares(self):
            listaDigitos = []
            for i in self.numCedula:
                listaDigitos.append(i) # los agrego a lista de constructor
            listaDigitos.pop()  # quito el ultimo elemento

            print(listaDigitos)

            impares = []    # lsita auxiliar para lmacenar los impares

            for i in range(0,10, 2):
                impares.append(listaDigitos[i] )
            
            print("Lista impares:",impares)
            # multiplicar por 2 cada digito
            for impar in impares:
                if int(impar) * 2 < 9:
                    self._sumaImpares += int(impar) * 2
                else:
                    # si la multiplicacion da mayor que 9 , a eso se resta 9 y se guarda a lasuma general
                    self._sumaImpares +=(int(impar) * 2) -9
            return self._sumaImpares


        def calcularPares(self):
            listaDigitos = []
            for i in self.numCedula:
                listaDigitos.append(i) # los agrego a lista de constructor
            listaDigitos.pop()  # quito el ultimo elemento
            pares = []    # lsita auxiliar para lmacenar los impares

            for i in range(1,9,2):
                pares.append(listaDigitos[i])
            
            print("Lista pares:",pares)
            # sumo los elementos 
            for digito in pares:
                self._sumaPares += int(digito)
            # print(self._sumaPares)   # la suma de los digitos
            return self._sumaPares

        def obtenerModulo(self):
            self._modulo = (self._sumaImpares + self._sumaPares)% 10
            return self._modulo 

        def comprobarVerificador(self):
            if self._modulo == 0:
                # si es cero . no se modifica y queda como num verificador
                print("El digito verificador es: ", self._modulo)
                # cambio el valor de 
                self._valido = 'la cedula esta verificada'
            else:
                # encuentro la decena arriba mas cerca y resto con la suma anterior
                self._modulo = (math.ceil(self._modulo/10) * 10) - self._modulo
                return self._modulo

class Internacional(Pasajero):
    def __init__(self,codigoPasaporte, paisRes,  nombrePasajero, tipoPasaje):
        super().__init__(nombrePasajero, tipoPasaje)
        self._codigoPasaporte = codigoPasaporte
        self._paisRes = paisRes
    
    # sobreescribo el metodo de padre
    def descripcion(self):
        # primero ejecutara el metodo del padre, luego este (hijo)
        super().descripcion()
        print('\t** Ciudadano internacional  **')
        print('Codigo de pasaporte: ', self._codigoPasaporte, ' Pais de residencia: ', self._paisRes )


# ingreso de datos
nombre = input('Ingrese el nombre del pasajero:')
print(''' 
        ** Tipos de pasaje **
    A: primera clase
    B: clase ejecutiva
    C: clase economica
 ''')
pasaje = input('Ingrese el tipo del pasaje(A/B/C): ')
tipoDoc=input('Ingrese el tipo de documento"cedula/pasaporte": ')

 # condicion 
if tipoDoc == 'cedula':
    codigo = int(input('Ingrese el numero de cedula: '))
    ciudadRes = input('Ingrese su ciudad de residencia: ')
    # instancio la clase nacional
    ecuatoriano = Nacional(codigo,ciudadRes, nombre, pasaje)
    ecuatoriano.validarCedula()
    ecuatoriano.descripcion()

if tipodoc == 'pasaporte':
    codigo = int(input('Ingrese el numero de pasaporte: '))
    paisRes = input('Ingrese su pais de residencia: ')
    # instancio la clase internacional
    extranjero = Internacional(codigo, paisRes ,nombre, pasaje)
    extranjero.descripcion()

else:
    print('Documento no permitido, escriba que tipo desea ingresar')
    print('"cedula o pasaporte"')
 