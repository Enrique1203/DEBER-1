def CalSalSem(horas, tarifa):
    sal_sem=horas*tarifa
    return sal_sem

def CalHorExt(horas,tarifa):
    extras=horas*(tarifa+(tarifa*.35))
    return extras

def Calculo():
    for i in range(5):
        horas_trb=int(input(f"Empleado {i+1} Ingrese las horas laboradas: "))
        tarifa=float(input(f"Empleado {i+1} Ingrese la tarifa por hora: "))
        if horas_trb<=40:
            print("Empleado",i+1,"Salario semanal:",CalSalSem(horas_trb,tarifa))
            print("No hubo horas extras")
        else:
            extra=horas_trb-40
            print("Empleado",i+1,"Salario semandal:",CalSalSem(40,tarifa))
            print(extra,"horas extra:",CalHorExt(extra,tarifa))

Calculo()