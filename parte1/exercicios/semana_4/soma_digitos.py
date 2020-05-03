n = int(input('Digite um número inteiro: '))

i = 0
soma = 0

while i < int(len(str(n))):
   soma += int(str(n)[i])
   i += 1 

print(soma)

     