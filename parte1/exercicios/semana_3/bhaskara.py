import math

a = float(input('Valor a: '))
b = float(input('Valor b: '))
c = float(input('Valor c: '))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print('esta equação não possui raízes reais')
if delta == 0:
    raiz1 = (-b + math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    print('a raiz desta equação é', raiz1)
if delta > 0:
    raiz1 = (-b + math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    raiz2 = (-b - math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    if raiz1 > raiz2:
        print('as raízes da equação são',raiz2,'e',raiz1)
    else:
        print('as raízes da equação são',raiz1,'e',raiz2)

