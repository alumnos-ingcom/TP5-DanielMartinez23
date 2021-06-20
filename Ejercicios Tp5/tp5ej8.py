################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def factoriales():
    temporal = 1
    lista = []
    lista.append(1)
    for i in range(1, 10):
        temporal = temporal * i
        lista.append(temporal) 
    return lista

def factoriones(lista):
    lista_a = []
    for i, valor in enumerate(lista):
        lista_a.append(i)
    return lista_a
    
def prueba():
    print("este es el ejercicio 8")
    lista = factoriales()
    lista_factoriones = factoriones(lista)
    print(lista_factoriones)
    print(lista)    
           
if __name__ == "__main__":
    prueba()
