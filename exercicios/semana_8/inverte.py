i = 1
lista = []

while i != 0:
    i = int(input('Digite um número: '))
    lista.append(i)

tamanho = len(lista)
index = 1

while index <= tamanho:  
    if lista[tamanho - index] > 0:
        print(lista[tamanho - index])
    index += 1