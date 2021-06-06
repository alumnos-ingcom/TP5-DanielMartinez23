################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def cad(mensaje):
    ingreso = input(mensaje + "#")
    return ingreso
    
def cambio_min_may(cadena):
    cambio = cadena.swapcase()
    return cambio

def prueba():
    cadena = cad("ingrese un texto")
    cambio = cambio_min_may(cadena)
    print(cadena)
    print(cambio)
           
if __name__ == "__main__":
    prueba()
