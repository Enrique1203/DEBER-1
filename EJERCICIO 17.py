print("Ingresa los datos de la hora de entrada")
hora_ent = int(input("Ingrese la hora: "))
min_ent = int(input("Ingrese los minutos: "))
tip_ent = input("Ingrese A para indicar Mañana o P si es Tarde/Nocche: ").upper()
print("\nIngresa los datos de la hora de salida")
hora_sal = int(input("Ingrese la hora: "))
min_sal = int(input("Ingrese los minutos: "))
tip_sal = input("Ingrese A para indicar Mañana o P si es Tarde/Noche: ").upper()

if tip_ent == tip_sal:
    if hora_ent > hora_sal or (hora_ent == hora_sal and min_ent > min_sal):
        horas = 24 - (hora_ent - hora_sal + 1)
    elif hora_ent == hora_sal and min_ent < min_sal:
        horas = -1
    else:
        horas = hora_sal - hora_ent - 1
else:
    if tip_ent == "A":
        horas = (hora_sal + 12) - hora_ent - 1
    else:
        horas = (24 - (hora_ent + 12)) + hora_sal - 1
if min_ent > min_sal:
    minutos = 60 - (min_ent - min_sal)
elif min_ent == min_sal:
    minutos = 0
    horas += 1
else:
    minutos = min_sal - min_ent
    horas += 1

if minutos >= 30:
    pgmin = 2.5
else:
    pgmin = 0
total_pag = horas * 4 + pgmin

print("Tiempo en estacionamiento:", horas, "horas,", minutos, "minutos.")
print("Total a pagar Bs.", total_pag)