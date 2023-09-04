String = '0A234567890B234567890C234567890D23456789'


def separador_Digitos(lista):
    Lista = [lista[v: v + 10] for v in range(0, len(lista), 10)]
    return Lista


variavel = separador_Digitos(String)
print(variavel)
