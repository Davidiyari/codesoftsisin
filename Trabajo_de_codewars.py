#Listas code
a = [3, 7, 11, 13, 17]  
b = [3, 13] 

# Aqui esta la clase
class Lista:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def filtrar(self):  # Aqui filtramos las 2 listas 
        resultado = []  
        for x in self.a:  
            if x not in self.b: 
                resultado.append(x)  
        return resultado 


mi_lista = Lista(a, b)  
print(mi_lista.filtrar())