diccionario={
    'nombre':"Juan",
    'edad':33,
    "hincha":True,
    'comida':['yogurt','hamburger','alpiste']
}
print(diccionario)

#nombres={}
#for nombre in range(1,5,1):
#    nombres['nombre']=input("Digita nombre: ")+
#print(nombres)

#recorrer
for llave,valor in diccionario.values('nombre'):
    print(llave)
    print(valor)