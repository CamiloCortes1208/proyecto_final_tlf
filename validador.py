import re


def validar_expresion(entrada):
    # Definir la expresión regular para el lenguaje deseado.
    # Por ejemplo, solo letras minúsculas y números en secuencias válidas.
    patron = r'^[a-z0-9]+$'  # Solo letras minúsculas y números.

    # Intentar hacer coincidir la entrada con el patrón del lenguaje
    if re.match(patron, entrada):
        return "La expresión es válida."
    else:
        return "La expresión no es válida en el lenguaje definido."


def validar_expresion2(expresion, cadena):
    # Definir la expresión regular para el lenguaje deseado.
    # Por ejemplo, solo letras minúsculas y números en secuencias válidas.

    # Intentar hacer coincidir la entrada con el patrón del lenguaje
    if re.match(expresion, cadena):
        return True
    else:
        return False

expresion_1 = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
cadena_1 = "ejemplo@dominio.com"  # Cadena válida

expresion_2 = r'^\d+$'
cadena_2 = "123456"  # Cadena válida
cadena_2_invalida = "123abc"  # Cadena inválida


expresion_3 = r'^[a-zA-Z]$'
cadena_3 = "a"  # Cadena válida

print(validar_expresion2(expresion_1, cadena_1))
print(validar_expresion2(expresion_2, cadena_2))
print(validar_expresion2(expresion_2, cadena_2_invalida))
print(validar_expresion2(expresion_3, cadena_3))
