from datetime import date

hoy = date(2014, 1, 1)
otra_fecha = date(2014, 4, 8)

delta = otra_fecha-hoy

print(delta)
print(delta.days)