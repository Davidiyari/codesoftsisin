# Zonas Horarias
# Definir 5 ciudades del mundo y checar su diferencia en la zona horaria
# Calcular la hora de las 5 ciudades a base de la hora especificada por el usuario
# Cabe considerar que la hora sera representada en un sistema de 12 horas

ciudades_mundo = ["dublin", "londres", "tokio", "los_angeles", "nueva_york", "nueva_deli"]
horas_mundo = [6, 7, 15, -2, 2, 11.3]

hora_mexico = int(input("Ingresa el valor de la hora que quieres consultar (0-24): "))

if 0 <= hora_mexico <= 24:
    print("La hora en las siguientes ciudades seria: ")
    for i, hora in enumerate(horas_mundo):
        if hora_mexico == 0 or hora_mexico == 24:
            hora_final = hora
            formato = "AM" if hora_final <= 12 else "PM"
            hora_final = hora_final if hora_final <= 12 else hora_final - 12
        else:
            hora_final = (hora_mexico + hora) % 24
            formato = "AM" if hora_final < 12 else "PM"
            hora_final = hora_final if hora_final <= 12 else hora_final - 12

        print(ciudades_mundo[i], abs(hora_final), formato)
else:
    print("La hora ingresada no es valida")