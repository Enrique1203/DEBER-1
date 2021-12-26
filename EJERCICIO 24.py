n = int(input("Ingrese un numero: "))
def evaluar_primo(n):
    contador = 0
    resultado = True
    for i in range(1,n+1):
        if (n%i==0):
            contador+=1
        if (contador>2):
            resultado = False
            break
    return  resultado
if (evaluar_primo(n)==True):
    print("El numero ingresado es primo")
else:
    print("El numero ingresado no es primo")
