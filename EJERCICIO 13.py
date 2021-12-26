numero = int(input("Ingrese un numero de 5 digitos: "))
if numero>=0:

    if str(numero) ==str(numero)[::-1]:
        print("%i Si es un numero capicua." % numero)
    else:
        print("%i No es un numero capicua." % numero)
