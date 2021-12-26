while True:
    contraseña=int(input("Ingrese una contraseña de 10 digitos: "))
    if contraseña>999999999 and contraseña<=9999999999:
        print("La contraseña es segura")
        break
    elif contraseña<=999999999:
        print("La contraseña debe contener 10 digitos intentelo de nuevo...")
        continue
    else:
        print("Contiene mas de 10 digitos, intentelo de nuevo...")
        continue