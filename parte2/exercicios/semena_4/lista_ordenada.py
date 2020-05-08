def ordenada(lista):
    tamanho = len(lista)
    posicao_minimo = 0
    lordenada = True
    for i in range(tamanho - 1):
        posicao_minimo = i
        for j in range(i + 1, tamanho):
            if lista[j] < lista[posicao_minimo]:
                lordenada = False

    return lordenada        

lista = [1,9,3,4,5,6,7,8]
print(ordenada(lista))
