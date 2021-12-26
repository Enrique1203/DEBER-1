from math import sqrt
ab = float(input("Escriba el valor de la longitud del vertice AB: "))
bc = float(input("Escriba el valor de la longitud del vertice BC: "))
hipotenusa = sqrt(ab**2 + bc**2)
print("La longitud de la hipotenusa es: {}".format(hipotenusa))
