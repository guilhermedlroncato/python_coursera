def sao_multiplicaveis(m1, m2):
    colunas_primeira = len(m1[0])
    linhas_segunda = len(m2)

    if colunas_primeira == linhas_segunda:
        return True
    else:
        return False

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

sao_multiplicaveis(m1, m2)