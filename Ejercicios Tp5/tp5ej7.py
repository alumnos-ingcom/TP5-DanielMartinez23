################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_real(mensaje):
    ingreso = input(mensaje + "#")
    try:
        entero = float(ingreso)
    except ValueError:
        print("No es un numero")
    return entero

def distancia(num1, num2):
    if num1 > num2:
        resultado = num1 - (num2)
    else:
        resultado = num2 - (num1)
    return resultado

def prueba():
    num1 = ingreso_real("ingrese un numero")
    num2 = ingreso_real("ingrese otro numero")
    dist = distancia(num1, num2)
    print(f"la distancia entre {num1} y {num2} es de: {dist}")
           
if __name__ == "__main__":
    prueba()
