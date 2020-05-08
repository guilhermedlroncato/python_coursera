def soma_lista(lista):
    n = 0
    if lista:
        n = lista[0]
        if len(lista) > 1:
            return n + soma_lista(lista[1:])
        else:
            return n


        