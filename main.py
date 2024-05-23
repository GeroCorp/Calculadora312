from email.policy import default
from os import system
from operaciones import *

def clean():
    """Limpia la consola
    """
    system("cls")
def pause():
    """Pausa la consola hasta tocar una tecla
    """
    system("pause")

def menu(a: int,b: int)->str:
    """Imprime un menu de opciones

    Args:
        a (int): Primer numero ingresado por usuario
        b (int): Segundo numero ingresado por el usuario

    Returns:
        str: Opcion seleccionada
    """
    clean()

    print("     Menu de opciones\n1- Calcular suma ({0}+{1})\n2- Calcular resta ({0}-{1})\n3- Calcular division ({0}/{1})\n4- Calcular multiplicacion ({0}x{1})\n5- Calcular factorial ({0}!)\n0- Salir".format(a,b))
    return input("Ingresar opcion: ")
def validarNumero (n: int,) ->None:
    """Valida que el valor ingresado sea un numero

    Args:
        n (int): Valor a validar
    """
    while not n.isdigit():
        print("Error. No se ha ingresado un numero")
        n = input("Ingresar numero: ")
    return int(n)
def ingresoDeNumero() ->None:
    """Le pide al usuario ingresar un numero
    """
    n = input ("Ingresar un numero: " )
    return validarNumero(n) 

n1 = ingresoDeNumero()
n2 = ingresoDeNumero()


while True:
    match menu(n1, n2):
        case "1":
            print("El resultado de {0} + {1} es: ".format(n1, n2)+suma(n1, n2))

        case "2":
            print("El resultado de {0} - {1} es: ".format(n1, n2)+resta(n1, n2))
            
        case "3":
            if n2 == 0: 
                print(division(n1, n2))
            else:
                print("El resultado de {0} / {1} es: ".format(n1, n2)+division(n1, n2))
            
        case "4":
            print("El resultado de {0} x {1} es: ".format(n1, n2)+multiplicacion(n1, n2))
            
        case "5":
            factorial(n1, n2)
            
        case "0":
            break

    pause()
