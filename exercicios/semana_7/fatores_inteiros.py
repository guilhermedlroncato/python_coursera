n = int(input('Digite um numero inteiro: '))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n / fator
    if multiplicidade > 0: 
        print('Fator = ',fator,'multiplicade = ',multiplicidade)
    fator += 1
    multiplicidade = 0
