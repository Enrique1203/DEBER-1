def MillasAKilometros(cd_origen,cd_destino,milla):
    km=milla*1.60935
    print("Entre la",cd_origen,"y la",cd_destino,"hay",km,"Km.\n")

def SolicitaInfo():
    for i in range(4):
        cd_org=input("Ingrese la ciudad origen: ")
        cd_des=input("Ingrese la ciudad destino: ")
        distancia=float(input("Ingrese la distancia en millas: "))
        MillasAKilometros(cd_org,cd_des,distancia)

SolicitaInfo()