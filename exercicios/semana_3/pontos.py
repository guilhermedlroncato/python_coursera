import math

x1 = float(input('Valor de x1: '))
y1 = float(input('Valor de y1: '))
x2 = float(input('Valor de x2: '))
y2 = float(input('Valor de y2: '))

delta = ((x2 - x1) ** 2) + ((y2 - y1 ** 2))

if delta >= 0:
    distancia = math.sqrt(delta)
    if distancia > 10:
        print('longe')
    else:
        print('perto')
else:
    print('perto')

