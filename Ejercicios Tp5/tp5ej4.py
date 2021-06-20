################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def numero_n(mensaje):
    ingreso = input(mensaje + "#")
    try:
        entero = int(ingreso)
    except ValueError:
        print("el numero ingresado no es un numero entero")
    return entero
    
def numumero_perfecto(num):
    condicion = False
    for i in range(num):
        if 2**(i-1)*((2**i) - 1) == num:
            condicion = True
    return condicion

def prueba():
    numero = num_n("ingrese un numero")
    condicion = num_perfecto(numero)
    if condicion == True:
        print("el numero ingresado es un numero perfecto!")
    elif condicion == False:
        print("el numero ingresado no es un numero perfecto")
        
    
if __name__ == "__main__":
    prueba()
