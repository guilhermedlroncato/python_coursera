def remove_repetidos(lista):
    index = 0
    lista = sorted(lista)
    lista_sem_duplicidade = []

    for i in lista:
        if i not in lista[:index]:
           lista_sem_duplicidade.append(i)
        index += 1

    return lista_sem_duplicidade

print(remove_repetidos([1,2,3,4,3,2,10,2,9]))

