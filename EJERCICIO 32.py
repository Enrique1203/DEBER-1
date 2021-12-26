def PromEdad(suma, conteo):
    promedio = suma / conteo
    print("\nEl promedio de edad de mayores de 18 años es:", promedio)


salir = "S"
cont_mas18 = 0
sum_mas18 = 0
while salir != "N":
    edad = int(input("Ingrese la edad: "))
    if edad >= 18:
        cont_mas18 += 1
        sum_mas18 += edad
    salir = input("Desea ingresar otro dato (S/N): ").upper()

PromEdad(sum_mas18, cont_mas18)