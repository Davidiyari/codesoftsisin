#Erick Otoniel Soto Hdez.
#Practica 9.
#26/02/25
#2do "J"



#!/usr/bin/env python
# coding: utf-8

# In[2]:


for i in range(10):
    print(i)


# In[14]:


for i in range(1,20,2):
    print(i)


# In[34]:


lista1=[0,1,2,3,4,5,6,7,8,9]
lista1.sort(reverse=True)
print (lista1)


# In[53]:


numero=input("Ingresa el numero que deseas multiplicar")
print(numero, "x1",numero*1)
print(numero, "x2",numero*2)
print(numero, "x3",numero*3)
print(numero, "x4",numero*4)
print(numero, "x5",numero*5)
print(numero, "x6",numero*6)
print(numero, "x7",numero*7)
print(numero, "x8",numero*8)
print(numero, "x9",numero*9)
print(numero, "x10",numero*10)


# In[63]:


numero=int (input("Ingresa el numero que deseas multiplicar"))
for i in range(1,11):
    print(i ," x ",numero, " = ",i * numero)


# In[79]:


numero1="1234567890"
contador=1
numero=input("Ingresa el numero")
numero2=list(numero)
for numero3 in numero2:
    contador = int (numero3)*contador
    print("Producto ",contador)

