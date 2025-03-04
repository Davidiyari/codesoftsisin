 
#-------------------------------------------------------------------------#
#Escribe un programa que calcule el numero factorial de una cantidad especificada por el usuario
numero = int(input("Ingresa un número: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es {factorial}")
#-------------------------------------------------------------------------#
#Escribir un programa que muestre la suma de los digitos de un numero especificado por el usuario
numero = int(input("Ingresa un número: "))
suma = sum(int(digito) for digito in str(numero))

print(f"La suma de los dígitos de {numero} es {suma}
#-------------------------------------------------------------------------#
#Escribir un programa que escriba el siguiente formato hasta un numero definido por el usuario
#Ejemplo
#1
#12
#123
#1234
#12345
#123456
#******
#*****
#****
#***
#**
#*
 
numero = int(input("Ingresa un número: "))

# Imprimir la secuencia ascendente
for i in range(1, numero + 1):
    print("".join(str(x) for x in range(1, i + 1)))

# Imprimir la secuencia descendente de asteriscos
for i in range(numero, 0, -1):
    print("*" * i)




#-------------------------------------------------------------------------#
#Escribir un programa que acepte 10 numeros separados por comas y calcular su promedio
numeros = input("Ingresa 10 números separados por comas: ")
lista_numeros = [int(num) for num in numeros.split(",")]

if len(lista_numeros) == 10:
    promedio = sum(lista_numeros) / 10
print(f"El promedio de los números ingresados es {promedio}")
else:
print("Por favor, ingresa exactamente 10 números.")

# Escribir un programa que escriba todos los números primos que se encuentren entre dos números escritos por el usuario

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

inicio = int(input("Ingresa el número de inicio: "))
fin = int(input("Ingresa el número de fin: "))

print(f"Los números primos entre {inicio} y {fin} son:")
for num in range(inicio, fin + 1):
    if es_primo(num):
        print(num)