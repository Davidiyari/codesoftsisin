#Archivo para alumnos
with open('alumnos.txt', 'r') as fichero:
    for linea in fichero:
        print(linea, end='')

lista= ["Garcia Hernandez Sofia Gabriela\n",
        "Sanchez Lopez Mateo Julian\n",
        "Martinez Rodriguez Luciana Valeria\n",
        "Gomez Gonzalez Alejandro Daniel\n",
        "Torres Ramirez Valeria Sofia\n",
        "Diaz Morales Sebastian Julian\n",
        "Reyes Sanchez Gabriela Luciana\n",
        "Hernandez Garcia Carlos Eduardo\n",
        "Lopez Martinez Daniela Valeria\n",
        "Ramirez Torres Julian Alejandro\n"]
with open("datos_guardados.txt", 'w') as fichero:
    fichero.writelines(lista)

with open('alumnos.txt', 'r') as fichero:
    for linea in fichero:
        print(linea, end='')