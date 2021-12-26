numero = int(input("Por favor, ingrese un numero: "))
user_input = abs(numero)

count = 0
while numero > 0:
    numero //= 10
    count += 1

print("El numero de digitos es: {} ".format(count))

