largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
l = 0
a = 0

while a < altura:
    while l < largura:
        print('#', end = '')
        l += 1
    a += 1
    print('')
    l = 0

