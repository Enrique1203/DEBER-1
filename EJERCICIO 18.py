peso_lib=float(input("Ingrese su peso (libras): "))
est_cm=int(input("Ingrese su estatura (cm): "))

peso_kg=peso_lib*0.453592
est_mt=est_cm/100
imc=peso_kg/(est_mt**2)

if imc < 16:
    clasi="Criterio de ingreso"
elif imc>=16 and imc<17:
    clasi="Infra peso"
elif imc>=17 and imc<=18.4:
    clasi="Bajo peso"
elif imc>=18.5 and imc<25:
    clasi="Peso normal"
elif imc>=25 and imc<30:
    clasi="Sobrepeso"
elif imc>=30 and imc<40:
    clasi="Obesidad pre-mórbida"
elif imc>=40 and imc<=45:
    clasi="Obesidad mórbida"
elif imc>45:
    clasi="Obesidas híper-mórbida"

print("Usted pesa",round(peso_kg,2),"Kg y su estatura es de",est_mt,"mt.")
print("Su IMC es de",round(imc,2),"por lo que su categoria es:",clasi)