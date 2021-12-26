def convertir(numbin):
    numbin=str(numbin)
    decimal=0
    exp=len(numbin)-1
    for i in numbin:
        decimal += (int(i)*2**(exp))
        exp=exp-1
    return decimal
entrada=input("Ingresar numero binario: ")
conv=convertir(entrada)
print(f"{entrada} su convercion es: {conv}")

