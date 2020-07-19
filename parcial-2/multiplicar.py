limiteMltpl = 5 + 1
cuantasTablas = int(input("Ingrese cuantas tablas quiere generar: "))

for i in range(1, cuantasTablas+1):
    for j in range(1, limiteMltpl):
        resultado = j * i
        print("{} x {} = {}".format(i, j, resultado))
    print()