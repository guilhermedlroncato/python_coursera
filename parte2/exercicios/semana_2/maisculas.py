def maiusculas(frase):
    letras_maiusculas = ''

    for letras in frase:
        if ord(letras) in range(65,90):
            letras_maiusculas += letras

    return letras_maiusculas.strip()     

print(maiusculas('Programamos em python 2?'))
