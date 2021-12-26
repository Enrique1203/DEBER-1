numero1 = float(input("Ingresar el primero numero: "))
numero2 = float(input("Ingresar el segundo numero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
modulo = numero1%numero2
if numero2 == 0:
    print("La suma es:",suma,"\n La resta es:",resta,"\n La multiplicacion es:",multiplicacion,"\n El modulo es:",modulo,"\n Division: No se puede dividir entre cero")
else:
    division = numero1/numero2
    print("La suma es:",suma,"\n La resta es:",resta, "\n La multiplicacion es:",multiplicacion,"\n El modulo es:",modulo, "\n La division es:",division)


