#Archivo para alumnos
with open('alumnos.txt', 'r') as fichero:
    for linea in fichero:
        print(linea, end='')

lista= ["Sanchez Ortiz Lizbeth Estefania\n",
        "Bayardo Fregoso Carlos Eduardo \n",
        "Gomez Fernandez Jose Roberto\n",
        "Mejia Lopez Angel Gadiel\n",
        "Parra Almado Emmanuel Alejandro\n",
        "Montaño Hernandez Yamile Isabela\n",
        "Robles Gomez Efren Alexander\n",
        "Gutierrez Gomez Gerardo Jesus\n",
        "Garcia Guzman Andrea Guadalupe\n",
        "Romero Zaragoza Cristofer Alexander\n"]
with open("datos_guardados.txt", 'w') as fichero:
    fichero.writelines(lista)

with open('alumnos.txt', 'r') as fichero:
    for linea in fichero:
        print(linea, end='')