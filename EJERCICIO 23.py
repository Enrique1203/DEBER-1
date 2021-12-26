n = int(input("Ingresar un numero: "))
if n > 99 and n <1000:
    a = n // 100
    b = n % 10
    if a==b:
        print("El numero",n,"es un numero capicua")
    else:
        print("El numero ingresado",n,"no es un numero capicua")