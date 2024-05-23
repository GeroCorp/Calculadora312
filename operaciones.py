def suma(a: int, b: int)->int:
    """Calcula la suma de dos numeros

    Args:
        a (int): Primer numero
        b (int): Segundo numero

    Returns:
        int: Retorna el resultado de la suma
    """
    return str(a+b)

def resta(a: int, b: int)->int:
    """Calcula la resta de dos numeros

    Args:
        a (int): Primer numero
        b (int): Segundo numero

    Returns:
        int: Retorna el resultado de la resta
    """
    return str(a-b)

def division(a: int, b: int)->float:
    """Calcula la division de dos numeros

    Args:
        a (int): Primer numero
        b (int): Segundo numero

    Returns:
        int: Retorna el resulatado de la division
    """
    if b==0:
        return "No es posible dividir por cero"
    return str(a/b)

def multiplicacion (a: int,b: int)->int:
    """Calcula la multiplicacion de dos numeros

    Args:
        a (int): Primer numero
        b (int): Segundo numero

    Returns:
        int: Retorna el resultado de la multiplicacion
    """
    
    return str(a*b)

def factorial (a: int,b: int):
    """Calcula el factorial de los numeros ingresados

    Args:
        a (int): Numero a
        b (int): Numero b
    """
    factorialA = 1
    for i in range(2,a + 1):
        factorialA *= i

    factorialB = 1
    for i in range(2,b + 1):
        factorialB *= i
    
    print ("El factorial de {0} es: {2} y El factorial de {1} es: {3}".format(a, b, factorialA, factorialB))
    pass