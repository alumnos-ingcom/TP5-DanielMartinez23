################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def cadena(mensaje):
    ingreso = input(mensaje + "#")
    return ingreso
    
def cambio_minuscula_mayuscula(cadena):
    cambio = cadena.swapcase()
    return cambio

def prueba():
    cad = cadena("ingrese un texto")
    cambio = cambio_minuscula_mayuscula(cadena)
    print(cad)
    print(cambio)
           
if __name__ == "__main__":
    prueba()
