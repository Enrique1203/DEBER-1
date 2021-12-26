num = int(input("Escriba un numero"))
u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print("Unidades: {}".format(u))
print("Decenas: {}".format(d))
print("Centenas: {}".format(c))
print("Unidades de mil: {}".format(m))
