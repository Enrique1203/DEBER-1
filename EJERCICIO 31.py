conteo=0
suma=0
numero=1
while numero!=0:
    numero=int(input("Ingrese un numero positivo mayor a 1 (para terminar ingrese 0): "))
    if numero<=1:
        if numero==0:
            print("Terminando serie...")
        else:
            print("Numero no valido")
            continue
    else:
        suma+=numero
        conteo+=1
print("El promedio de",conteo,"numero(s) es:",suma/conteo)