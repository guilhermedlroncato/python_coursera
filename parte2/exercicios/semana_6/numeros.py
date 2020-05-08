def busca_binaria(lista, elemento, min=0, max=None):
    cont =  0

    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        cont += 1
        print('entrou')
        return busca_binaria(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        cont += 1
        print('entrou')
        return busca_binaria(lista, elemento, meio + 1, max)
    else:
        return meio, cont

a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]
print(busca_binaria(a, 99))