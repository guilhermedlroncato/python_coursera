def ordena(lista):
    fim = len(lista)

    for i in range(fim - 1):
        posicao_do_minimo = i
        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
        
    return lista

lista = [2,4,3,5,6,7,8,99,102,344,5,54]
print(ordena(lista))