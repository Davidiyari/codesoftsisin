 
#-------------------------------------------------------------------------#
#Crear una tuple con 3 elementos: 10, "Hola" y 3.14
from sympy.physics.units import length


tupla1=(10,"Hola",3.14)
print(tupla1)

#-------------------------------------------------------------------------#
#La tupla(1,2,3,4,5), accede y escribe el tercer element
tupla2 = (1,2,3,4,5)
print(tupla2[2])

#-------------------------------------------------------------------------#
#Concatena las tuplas y almacena el resultado en una tupla Nueva
tupla_final=tupla1+tupla2
print(tupla_final)

#-------------------------------------------------------------------------#
#Desempaqueta la tupla en tres variables y escribe sus valores
tupla3 = ('a','b','c')
var1,var2,var3 = tupla3
print(var1,var2,var3)

#-------------------------------------------------------------------------#
#verifica si el elemento 7 existe en la tupla (1,3,5,7,9)

tupla4 = (1,3,5,7,9)
existe=7 in tupla4
print(existe)

#-------------------------------------------------------------------------#
#crea una tupla (0,1,2,3,4,5) y escribe los elementos del indice 2 a 4 con slice
tupla5 = (0,1,2,3,4,5)
resultado=tupla5[2:5]
print(resultado)

#-------------------------------------------------------------------------#
#encuentra la longitude de una tupla (10,20,30,40,50)
tupla6 =  (10,20,30,40,50)
length=len(tupla6)
print(length)

#-------------------------------------------------------------------------#
#crea una tupla y repitela 3 veces
tupla7=(1,2,3)
resultado=tupla7*3
print(resultado)

#-------------------------------------------------------------------------#
#convierte la lista[1,2,3] a tupla
lista=[1,2,3]
tupla8=tuple(lista)
print(tupla8)

#-------------------------------------------------------------------------#
 
#Encuentra los valores minimo y maximo de la tupla(5,12,3,8,15)
tupla9=(5,12,3,8,15)
valor_minimo=min(tupla9)
valor_maximo=max(tupla9)
print('Minimo: ',valor_minimo,' Maximo: ', valor_maximo) 



