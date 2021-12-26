binario=input("Ingrese un numero binario: ")
rev=binario[0]=="1"
resultado=("par","impar")[rev]
print("El valor del bit de paridad en",binario,"es:",resultado)