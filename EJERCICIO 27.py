mayor=0
menor=0
numero=1

while numero != 0:
    numero=int(input("Ingrese un numero (para finalizar ingrese 0): "))
    if numero!=0:
        if numero>mayor:
            mayor=numero
        if menor==0:
            menor=numero
        elif menor>numero:
            menor=numero
    else:
        print("Terminado la secuencia...")
print("El numero mayor ingresado fue:",mayor)
print("El numero menor ingresado fue:",menor)