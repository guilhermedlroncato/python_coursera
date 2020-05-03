n = int(input('Digite o valor de n: '))

i = 1

pause = False

while not pause:
    if not i % 2 == 0:
        print(i)
        n -= 1
    if n == 0:
        pause = True
    i += 1

