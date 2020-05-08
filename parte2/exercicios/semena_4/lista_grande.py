from random import randint

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(randint(0,n) * i)

    return lista

print(lista_grande(200))