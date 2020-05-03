def dimensoes(matriz):
    linhas = 0
    colunas = 0
    i = 0

    for i in matriz:
        linhas += 1
        colunas = len(i)
              
    return [linhas,colunas]

def soma_matrizes(m1, m2):
    d_m1 = dimensoes(m1)
    d_m2 = dimensoes(m2)
    i = 0
    j = 0
    m3 = []

    if d_m1 == d_m2:
        while i < d_m1[0]:
            m3.append([])
            while j < d_m1[1]:
                m3[i].append(m1[i][j] + m2[i][j])
                j += 1
            j = 0
            i += 1
        return m3
    else:
        return False

m1 = [[1], [4]]
m2 = [[2], [5]]

soma_matrizes(m1,m2)



