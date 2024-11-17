import re


def validar_expresion_regular(expresion, cadena):
    # Se verifica si coincide la cadena con la expresión regular dada
    if re.match(expresion, cadena):
        return True
    else:
        return False
