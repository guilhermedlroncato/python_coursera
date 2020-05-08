def busca(lista, elemento):
    tamanho = len(lista)
    index_achado = 0
    for i in range(tamanho):
        if lista[i] == elemento:
            index_achado = i

    if index_achado == 0:
        return False
    else:
        return index_achado            

lista = [1,2,3,4,5,6,7]
print(busca(lista, 99))