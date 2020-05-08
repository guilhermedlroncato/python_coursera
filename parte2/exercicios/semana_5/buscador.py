class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1
    
    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio -1
                else:
                    primeiro = meio + 1
        return -1
lista = [1,2,3,4,5,6,7,8]
b = Buscador()
print(b.busca_binaria(lista, 88))