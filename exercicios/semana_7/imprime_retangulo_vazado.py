largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
l = 0
a = 0

while a < altura:
    while l < largura:
        if (a == 0) or (a == altura - 1) or (l == 0) or (l == largura - 1):
            print('#', end = '')
        else:
            print(' ', end = '')
        l += 1
    a += 1
    print('')
    l = 0