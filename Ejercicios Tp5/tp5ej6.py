################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def balance(cadena):
    contador_a = 0
    contador_b = 0
    condicion = False
    for i in cadena:
        if i == '[' or i == '(' or i == '{':
            contador_a = contador_a + 1
        elif i == ']' or i == ')' or i == '}':
            contador_b = contador_b + 1
    if contador_a == contador_b and contador_a != 0 and contador_b != 0:
        condicion = True
    return condicion


def prueba():
    print("este es el ejercicio 1")
    cadena = input("ingrese una cadena con parentesis")
    condicion = balance(cadena)
    if condicion == True:
        print("la cadena está balanceada")
    elif condicion == False:
        print("la cadena no está balanceada")
    elif condicion == 0:
        print("no ha ingresado ningun parentesis")

if __name__ == "__main__":
    prueba()

