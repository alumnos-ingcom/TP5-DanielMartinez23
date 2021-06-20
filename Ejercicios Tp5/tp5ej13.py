################
# Daniel Martinez - DanielMartinez23
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

class no_hay_palabra(Exception):
    """Esta es la excepcion para las palabras que no pudieron ser ubicadas"""
    pass

def buscar_palabra(texto, palabra):
    
    ubicacion = 0
    letra = 0
    misma_letra = 0
    for i in range(len(texto)):
        if letra < len(palabra) and texto[i] == palabra[letra]:
            if letra == 0:
                ubicacion = i
                letra = letra + 1
                misma_letra = misma_letra + 1
            else:
                misma_letra = misma_letra + 1
                letra = letra + 1
        elif misma_letra == len(palabra) and texto[i] == ' ':
            return ubicacion
        else:
            ubicacion = 0
            letra = 0
            misma_letra = 0
    if misma_letra == len(palabra):
        return ubicacion
    raise no_hay_palabra('No se a encontrado esa palabra')
    
def prueba():
    
    print("Este es el ejercicio 13")
    texto = str(input("ingrese el texto a analizar: "))
    palabra = str(input("ingrese la palabra que desea buscar en el texto ingresado: "))
    ubicacion = buscar_palabra(texto, palabra)
    print(f"La palabra se encuentra ubicada en el caracter {ubicacion}.")

if __name__ == "__main__":
    prueba()

