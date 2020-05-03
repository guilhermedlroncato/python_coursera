def dimensoes(matriz):
    linhas = 0
    colunas = 0
    i = 0

    for i in matriz:
        linhas += 1
        colunas = len(i)
              
    print(f'{linhas}X{colunas}')

minha_matriz = [[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1], [2, 3, 6, 7]]
dimensoes(minha_matriz)