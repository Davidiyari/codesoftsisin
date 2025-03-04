
# 1. Porcentaje del alumno
porcentaje = float(input("Ingresa el porcentaje del alumno:"))
if porcentaje > 90:
    grado = 'A'
elif porcentaje > 80 and porcentaje <=90:
    grado = 'B'
elif porcentaje >= 60 and porcentaje <= 80:
    grado = 'C'
else:
    grado = 'D'
print(f"El grado del alumno es: {grado}")

# 2. Impuesto de bicicleta
precio = float(input("Ingresa el precio de la bicicleta: "))
if precio > 100000:
    impuesto = precio * 0.15
elif 50000 < precio <= 100000:
    impuesto = precio * 0.10
else:
    impuesto = precio * 0.05
print(f"El impuesto que debes pagar es: {impuesto:.2f}")

# 3. Anio bisiesto
año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto:")
else:
    print(f"El año {año} no es bisiesto.")

# 4. Dia de la semana
numero = int(input("Ingresa un número del 1 al 7: "))
semana = ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
print("El día correspondiente es : +",semana[numero-1])

# 5. Cuantos dias tiene cada mes
numero = int(input("Ingresa un número del 1 al 12: "))
mes = ["Enero 31","Febrero 28","Marzo 31","Abril 30","Mayo 31","Junio 30","Julio 31","Agosto 31","Septiembre 30","Octubre 31","Noviembre 30","Diciembre 31"]
if (numero >=1 and numero <=12):
    print("El mes "+str(numero)+" Es "+mes[numero-1])
else:
    print("El numero "+str(numero) +" no es valido")