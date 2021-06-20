################
# Daniel Martinez -  DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_capicua(numero):
    
    if numero >= 0:
        return str(numero) == str(numero)[::-1]
    else:
        return False

def prueba():
    print("Este es el ejercicio 14")
    numero = input("ingrese un numero para ver si es capicua o no: ")
    num = int(numero)
    capicua = es_capicua(num)
    if capicua == True:
        print("el numero ingresado es capicua")
    else:
        print("el numero ingresado no es capicua")

if __name__ == "__main__":
    prueba()

