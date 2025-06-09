#Trabajo de codewars corregido
def dibujar_serpiente(cuerpo):
    
    direccion = 1  
    pos = 1         
    filas = []      

    # Pocisiones de cada letra 
    for b in cuerpo:
        fila = []
        if direccion == 1:
            for i in range(b):
                fila.append(pos + i)
            pos = pos + b - 1
        else:
            for i in range(b):
                fila.append(pos - i)
            pos = pos - b + 1
        filas.append(fila)
        direccion = -direccion

    #Pocisiones segun la anchura 
    minimo = min(x for fila in filas for x in fila)
    maximo = max(x for fila in filas for x in fila)
    ancho = maximo - minimo + 1

    dibujo = []
    n = len(filas)
    for i in range(n):
        linea = [" "] * ancho
        for j in range(len(filas[i])):

            if i == 0 and j == len(filas[i]) - 1:
                linea[filas[i][j] - minimo] = "H"
                
            elif i == n - 1 and j == len(filas[i]) - 1:
                linea[filas[i][j] - minimo] = "T"
            else:
                linea[filas[i][j] - minimo] = "X"
        dibujo.append("".join(linea))
    return dibujo

# Codigo principal
cuerpo = [1, 2, 3]
resultado = dibujar_serpiente(cuerpo)
for fila in resultado:
    print(fila)