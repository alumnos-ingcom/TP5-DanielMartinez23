################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def binario(numero):
    lista = []
    while numero >= 1:
        if numero % 2 != 0:
            numero = numero - 1
            lista.append(1)
        else:
            lista.append(0)
        numero = numero / 2
    binario = reversed(lista)
    return tuple(binario)   
    
def prueba():
    numero = 20
    print("este es el ejercicio 10")
    lista = binario(numero)
    print(lista)
           
if __name__ == "__main__":
    prueba()
