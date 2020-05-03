def imprime_matriz(matriz):
    linha = 0
    colunas = 0
    for linha in matriz:
        for colunas in linha:
            if colunas != linha[-1]:
                print(colunas, end = ' ')
            else:
                print(colunas, end = '')
        print('')

minha_matriz = [[1,2,3],[4,5,6]]
imprime_matriz(minha_matriz)