fecha=input("Ingrese una fecha (ddmmaaaa):")
anio=int(fecha[4:])

if (anio%400) == 0:
    print("Es año bisiesto")
elif (anio%4) == 0:
    if (anio%100) != 0:
        print("Es año bisiesto")
    else:
        print("No es año bisiesto")
else:
    print("No es año bisiesto")