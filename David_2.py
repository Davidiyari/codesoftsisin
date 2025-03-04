#calcular en base a un valor dado por el usuario 
#su equivalencia en las diferentes divisas definidas

#china
yuan=2.81
#japon
jen=0.13
#Estados Unidos
dólar=20.54
#unión europea
euro=21.29
#Reino Unido
libra=25.56

peso = input("ingresa la cantidad a convertir")
peso=int(peso)
print("son %.2f yuanes" %(peso/yuan))
print("son %.2f jenes" %(peso/jen))
print("son %.2f dolares" %(peso/dólar))
print("son %.2f euros" %(peso/euro))
print("son %.2f libras" %(peso/libra))