n = 1
while n > 0:
    n = int(input('Digite um numero: '))
    i = 1
    fat = 1
    total = 0
    while i < n:
        fat = n * (n - i)
        if i == 1:
            total += fat        
        elif (n - 1) > 0:
            total = total * (n - i)
        i = i + 1
    if i == 1:
        total = 1
    print(f'O fatorial do numero {n} é {total}')