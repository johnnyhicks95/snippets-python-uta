
numeroInicio = int(input("Desde que digito quiere empezar:"))
numeroCuantos = int(input("Cuantos números mas de la serie:"))
print('*********Serie*********')
inicio = 0
print(inicio)
siguiente=1
print(siguiente)
unidades=['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
decenas=['cero','diez','veinte','treinta','cuarenta','cincuenta','sesenta','setenta','ochonte','noventa']
contador=2

limite = True
while limite:
    if siguiente<numeroInicio:
        serie  = inicio + siguiente
        print(serie)
        inicio = siguiente
        siguiente = serie
        contador+=1
    else:
        if numeroCuantos>0:
            serie  = inicio + siguiente
            print(serie)
            inicio = siguiente
            siguiente = serie
            contador+=1
            numeroCuantos-=1
        else:
            limite = False
serieFibonacci = serie
#------------------------------------------------------------------------------------------
print('*********Factorial*********')
#Factorial
def factorail(n):
    if n==0 or n==1:
        resultado=1
    elif n>1:
        resultado = n*factorail(n-1) 
    return resultado   

for comienzaFac in range(contador):
    fac=factorail(comienzaFac)
    print (fac) 

#------------------------------------------------------------------------------------------
print('*********Posicion*********')
#Posición
def palabrasPosicion(numero):
    if numero<10:
        return unidades[numero]
    decena, unidad = divmod(numero,10)
    if numero>=10:
        valorFinal = decenas[decena] 
        if unidad > 0:
            valorFinal = (valorFinal + " y " + unidades[unidad])
        return valorFinal       

for comienzaPosi in range(contador):
    posicion=palabrasPosicion(comienzaPosi)
    print (posicion)

#---------------------------------------------------------------------------------------------
#Diccionario
diccionario= {}
diccionario['serie original'] = serieFibonacci
diccionario['factorial'] = fac
diccionario['posición'] ='Posición..' + posicion
print(diccionario)
 



