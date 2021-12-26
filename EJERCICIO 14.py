horas = int(input("Escriba la cantidad de horas: "))
minutos = int(input("Escriba la cantidad de minutos: "))
segundos = int(input("Escribir la cantidad de segundos: "))

segundos += horas*60 * 60
segundos += minutos * 60

print("La cantidad de segundos es igual: {}".format(segundos))
