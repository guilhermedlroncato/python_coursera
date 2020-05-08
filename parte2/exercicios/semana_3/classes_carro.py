def main():
    carro1 = Carro(2020,'Ford','Vermelho',190)
    carro2 = Carro(2020,'Fiat','Vermelho',200)

    carro1.acelera(40)
    carro2.acelera(50)
    carro1.acelera(80)
    carro1.para()
    carro2.acelera(220)

class Carro:
    #construtor da classe o metodo __init__
    def __init__(self, ano, modelo, cor, velocidade_max): 
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.velocidade_max = velocidade_max
        self.velocidade = 0
    
    def imprime(self):
        if self.velocidade == 0:
            print("%s %s %d"%(self.modelo, self.cor, self.ano))
        elif self.velocidade < self.velocidade_max:
            print("%s %s indo a %d km/h"%(self.modelo, self.cor, self.velocidade))
        else:
            print("%s %s indo muito rapidoooo!!!"%(self.modelo, self.cor))
    
    def acelera(self, v):
        self.velocidade = v
        if self.velocidade > self.velocidade_max:
            self.velocidade = self.velocidade_max
        self.imprime()
    
    def para(self):
        self.velocidade = 0
        self.imprime()

main()




