################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def lista_factoriones():
    
    lista_factoriones = []
    lim = 1499999
    for i in range(lim):
        if i == factoriones(i):
            lista_factoriones.append(i)
    return lista_factoriones

def factoriones(numero):
    
    factorial = 1
    suma = 0
    for j in str(numero):
        k = int(j)
        for i in range(k):
            factorial = factorial * (i + 1)
        suma = suma + factorial
        factorial = 1
    return suma

def prueba():
    
    print("Este es el ejercicio 9")
    print("Lista de todos los factoriones menores a 1.499.999: ")
    factoriales = lista_factoriones()
    print(f"{factoriales}")

if __name__ == "__main__":
    prueba()

