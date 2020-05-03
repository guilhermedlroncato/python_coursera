n = int(input('Digite um número inteiro: '))
i = 0
adjacente = 0

if n < 0:
    print('O numero precisa ser positivo')
else:
    while i < len(str(n)):
        if i > 0:
            if str(n)[i] == str(n)[i - 1]:
                adjacente += 1    
        i += 1

if adjacente > 0:
    print('sim')
else:
    print('não')