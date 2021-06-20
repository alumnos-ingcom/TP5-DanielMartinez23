################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def tribonacci(n):
    num1 = 1
    num2 = 1
    num3 = 1
    sucecion =[]
    for i in range(n):
        total = num1 + num2 + num3
        num1 = num2
        num2 = num3
        num3 = total
        sucecion.append(total - num1 - num2)
    return sucecion

def num_n(mensaje):
    ingreso = 0
    while ingreso <= 2:
        ingreso = input(mensaje + "#")
        ingreso = int(ingreso)
        if ingreso <= 2:
            print("el numero ingresado tiene que ser mayor a 2")
    return ingreso
    
    
def prueba():
    print("este es el ejercicio 3")
    numero = num_n("ingrese el numero n(tiene que ser mayor a 2)")
    total = Fibonacci(numero)
    print(f"el n-esimo termino de la secuencia Fibonacci es: {total}")

if __name__ == "__main__":
    prueba()

