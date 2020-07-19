# Construye un programa que al recibir como datos tres variables reales que representen
# los lados de un probable triangulo, determine si esos lados corresponden
# a un triangulo. En caso de serlo, ademas de escribir el area correspondiente compruebe
# si el mismo es equilatero, esosceles o escaleno.
# Consideraciones:
# Si se cumple la propiedad de que la suma de dos lados del triangulo es mayor que el tercero
# es un triangulo

# El area se obtiene aplicando la siguiente formula
# Area = raiz(S * (S-A) * (S-B )* (S- C) )

# import math

a = float(input("Ingrese el primer lado: "))
b = float(input("Ingrese el primer segundo lado: "))
c = float(input("Ingrese el primer tercer lado: "))

# a+b>c
#  a+b>c
#  b+c>a
if (a+b)>c and (a+c)>b and (b+c)>a:
    print("\tSe forma un triangulo")

    s= (a+b+c)/2    # para hallar el area

    area = (s * (s-a) * (s-b) * (s-c)) ** (1/2) # hallo la raiz

    print("El area del triangulo es", area)

    # equilatero: 3 lados iguales: a=b a=c
    if ( a==b ==c):
        print("Se trata de un triangulo equilatero")
        
    # isosceles: 2 lados iguales a=b o a=c o b=c
    elif ( a==b or a==c or b==c ):
        print("Es un triangulo isosceles")
    else:
        print("Es un triangulo escaleno")

    # escaleno = no tiene lados iguales

else:
    print("\tNo se forma un triangulo")
