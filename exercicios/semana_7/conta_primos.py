def n_primos(n):
    i = 1
    x = 2
    qtd = 0
    restozero = 0

    if n >= 2:
        while x <= n:
            while (i <= x):
                if x % i == 0:
                    restozero += 1
                i += 1
            if restozero == 2:
                qtd += 1
            x += 1
            i = 1
            restozero = 0
    else:
        print('O inteiro precisa ser maior que 2')

    return qtd

n_primos(121)
