sum_edad=0
sum_esta=0
sum_peso=0
sum_e18a25=0
sum_may36=0
sum_pesoe18y35=0
cont_peso18y35=0
conteo_total=0
edad=1

while edad != 0:
    edad=int(input("Ingrese la edad (para terminar ingrese 0): "))
    if edad<18:
        if edad==0:
            print("Termino ingreso de datos")
        else:
            print("Edad no valida")
            continue
    else:
        peso=float(input("Ingrese el peso: "))
        estatura=float(input("Ingrese la estatura: "))
        conteo_total+=1
        sum_edad+=edad
        sum_peso+=peso
        sum_esta+=estatura
        if edad<=25:
            sum_e18a25+=1
        elif edad>36:
            sum_may36+=1
        if edad<=35:
            sum_pesoe18y35+=peso
            cont_peso18y35+=1

print("\nEl total de datos ingresados:",conteo_total)
print("La edad promedio es:",sum_edad/conteo_total)
print("El peso promedio es:",sum_peso/conteo_total)
print("La estatura promedio es:",sum_esta/conteo_total)
print("Cantidad de personas entre 18 y 25 años es:",sum_e18a25)
print("Cantidad de personas mayores de 36 años es:",sum_may36)
print("El promedio de peso de las personas de edad entre 18 y 35 años es:",sum_pesoe18y35/cont_peso18y35)