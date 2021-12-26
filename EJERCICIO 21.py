compra = float(input("Ingrese el valor total de la compra: "))

if compra <=1000:
    print("El total a pagar es: ",compra)
else:
    compra >1000
    compra -= (compra * 0.20)
    print("El valor final a pagar es: ",compra)
