def maior_primo(n):
    i = 1
    x = 1
    restozero = 0
    max_primo = 0

    if n < 0:
        print('O numero precisa ser positivo')
    else:
        while x <= n:
            restozero = 0
            i = 1
            while i <= x:
                if x % i == 0:
                    restozero += 1
                i += 1
            if restozero == 2:
                max_primo = x
            x += 1
    return max_primo