class Calculadora:
    # def __call__(self):  #Funcion A
    def impresionDecorador(self, parametroTipoFuncion, *args):   #Funcion B                               
        print("Ejecucion de calculadora")
        parametroTipoFuncion()
        return impresionDecorador()                   #Funcion C 
        
    @impresionDecorador
    def suma(self):   
        print(8+22)
    
    def resta(self):    
        print(8-22)
    
    def multiplicacion(self):
        print(8*22)

    def division(self):    
        print(8/22)



calculadora = Calculadora()
calculadora.suma()


