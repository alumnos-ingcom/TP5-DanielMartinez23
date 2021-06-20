################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def construccion_lista():
    lista=[]
    for i in range(5):
        ingreso = input("ingrese un numero")
        entero = int(ingreso)
        lista.append(entero)
    return lista

def comparacion(primera_lista, segunda_lista):
    
    mismo_elemento = 0
    for i in primera_lista:
        for j in segunda_lista:
            if i == j:
                mismo_elemento = mismo_elemento + 1
    return mismo_elemento >= len(primera_lista)

def prueba():
    
    print("Este es el ejercicio 12")
    
    print("Ingrese 2 listas para comparar sus similitudes")
    print("Primer lista: ")
    primera_lista = construccion_lista()
    print("Segunda lista: ")
    segunda_lista = construccion_lista()
    busqueda = comparacion(primera_lista, segunda_lista)
    if busqueda == True:
        print("Las listas son similares")
    else:
        print("No tienen los mismos elementos")

if __name__ == "__main__":
    prueba()

