n = int(input('Digite um número inteiro: '))
i = 1
pause = False
restozero = 0

if n < 0:
    print('O numero precisa ser positivo')
else:
    while (i <= n) and (pause == False):
        if n % i == 0:
            restozero += 1
        i += 1
if restozero == 2:
    print('primo')
else:
    print('não primo')