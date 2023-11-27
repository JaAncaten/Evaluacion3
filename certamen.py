import os

os.system('cls')
Tipo = []
Patente = []
Marca = []
Precio = []
multas = []
fRegristroV = []
nDueño = []

menu = """ 
    1.- Grabar
    2.- Buscar
    3.- Imprimir Certificados
    4.- salir
    opcion: """
 

def Grabar():
    print("Grabando datos")
    aT = input("""ingrese el tipo de vehiculo: 
                (AUTO, CAMIONEATA , SUV) """)
    while True:
        aP = int(input("Ingresa la petente: "))
        try:
            if aP >= 2 or aP <= 15:
             if aPP > 5000000:
                break
            else:
                print("a ocurrido un error")
        except:
            print("")
            

    
    aM = input("Ingreza la marca del vehiculo: ")
    aPP = input("Ingresa el precio: ") 
    aMu = int(input("monto  y fechas: "))   
    aFr = input("Fecha de rgistro Vehiculo: ")
    aN = input("Ingresa el nombre dueño: ")
    Tipo.append(aT)
    Patente.append(aP)
    Marca.append(aM)
    Precio.append(aPP)
    multas.append(aMu)
    fRegristroV.append(aFr)
    nDueño.append(aN)
    

def Buscar():
    print("Buscar Vehiculo")
    print(f"patentes: {Patente}")
    aPatente = int(input("Ingrese la patente del vehiculo: "))
    if not aPatente in Patente:
        print("patente no encontrada")
    else:
       indice = Patente.index(aPatente)
       print(f"Patente : {Patente[indice]}")
       print(f"Tipo : {aPatente[indice]}")
       print(f"marca : {Marca[indice]}")
       print(f"Multas : {multas[indice]}")

 
   
    
   

      




    

def imprimir():
     print("")
     



while True:
    os.system("cls")
    try:
        opcion = int(input(menu))
        if opcion == 4:
             break
        elif opcion == 1:
            Grabar
        elif opcion == 2:
            Buscar
        elif opcion == 3:
           imprimir
        else:
            print("a ocurrido un error")
    except:
        print("a ocurrido una error")