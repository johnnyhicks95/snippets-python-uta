# Usando decoradores crear funcion que pida al usuario cuantas tablas de multiplicar quiere
# y que las muestre

limiteMltpl = 12 # mas 1 porque el range siempre tiene el rango n-1
cuantasTablas = int(input("Ingrese cuantas tablas quiere generar: "))

# decorador
def decorador(funcParam):
    def funcionDecorar(*args):
        # antes de la funcion
        print("Generando tabla de multiplicar...")
        print()
        funcParam(limiteMltpl, cuantasTablas)
        print("Proceso terminado...")
    #returno lla funcion
    return funcionDecorar

# agrego el decorador a la funcion multiplicar
@decorador
# bloque de codigo con la funcion multiplicar
def multiplicar(limiteMtpl, cuantasTablas):
    for i in range(1, cuantasTablas+1): # recorre la cantidad de tablas pedidas por el usuario
        print("Siguiente tabla ->", i," :")
        for j in range(1, limiteMltpl+1):  # recorre hsta que numero multiplicar
            resultado = j * i
            print("{} x {} = {}".format(i, j, resultado))
        print()
# ejecuto multiplicar enviando los parametros
multiplicar(limiteMltpl, cuantasTablas)