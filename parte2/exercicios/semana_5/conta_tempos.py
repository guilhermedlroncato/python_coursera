import random
import ordenacao_selecao_direta
import time

class ContaTempos:
    def lista_aleatoria(self,n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenadra(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_quase_ordenadra(n)
        lista2 = lista1[:]
        lista3 = lista1[:]

        o = ordenacao_selecao_direta.Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        #print(lista1)
        print(f'Bolha demorou ',depois - antes)

        antes = time.time()
        o.bolha_curta(lista2)
        depois = time.time()
        #print(lista1)
        print(f'Bolha Curta demorou ',depois - antes)

        antes = time.time()
        o.selecao_direta(lista3)
        depois = time.time()
        #print(lista2)
        print(f'Seleção Direta demorou ',depois - antes)

c = ContaTempos()
c.compara(300)

