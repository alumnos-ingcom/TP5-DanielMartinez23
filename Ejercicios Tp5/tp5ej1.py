################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def numero_par_impar():
    num = ingreso_entero("ingrese un numero entero")
    par = 0
    condicion =  False
    for i in range(num):
        par = par + 2
        if par == num:
            condicion = True
    return condicion
        

def ingreso_entero(mensaje):
    ingreso = input(mensaje + "#")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero


def prueba():
    print("este es el ejercicio 1")
    condicion = numero_par_impar()
    if condicion == True:
        print("el numero ingresado es un numero par")
    else:
        print("el numero ingresado es un numero impar")
    pass

if __name__ == "__main__":
    prueba()

