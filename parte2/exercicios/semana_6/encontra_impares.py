def encontra_impares(lista):
    lista_impar = []
    if len(lista) < 1:
        return lista
    
    if lista[0] % 2 != 0:
        lista_impar.append(lista[0])
        lista_impar = lista_impar + encontra_impares(lista[1:])
    else:
        lista_impar = lista_impar + encontra_impares(lista[1:])
    
    return lista_impar

lista = [1,2,3,4,5,6,7,8,9]
print(encontra_impares(lista))