print("*****MENú*******")
print("1. Agregar 1 empanada")
print("2. Mostrar empanada")
print("3. Salir")
opcion= int(100)
#datos empanada
#sabor
#ingredientes (x3)
#Precio fabricacion
#Precio venta
empanada={}
ingredientes = []
while (opcion!=3):
    opcion=int(input("Digite una opcion: "))
    if(opcion==1):
        empanada['sabor']=input("Digita el sabor: ")
        for i in range(3):
            ingredientes.append(input("Digite un ingrediente: "))
        empanada["ingredientes"]=ingredientes
        empanada['valorf']= int(input("Valor fabricacion: "))
        empanada['valorv']= int(input("Precio venta"))
    elif(opcion==2):
        print(empanada)
    else:
        print("Digite valor valido")
else:
    print("Chao") 
