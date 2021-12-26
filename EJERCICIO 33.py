class Potencia:
    def __init__(self,base=0,exponente=0):
        self.base = base
        self.exponente = exponente
    def calcular(self):
        self.resultado = self.base ** self.exponente
    def mostrar(self):
        print("El resultado de la potencia es: {}".format(self.resultado))
objeto1 = Potencia(2,6)
objeto1.calcular()
objeto1.mostrar()