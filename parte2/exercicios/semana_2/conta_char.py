def conta_letras(frase, contar="vogais"):
    vogais = ['a','e','i','o','u']
    tot_vogal = 0
    tot_cons = 0
    for letra in frase:
        if letra != ' ':
            if letra.lower() in vogais:
                tot_vogal += 1
            else:
                tot_cons += 1
    
    if contar == 'vogais':
        return tot_vogal
    else:
        return tot_cons

print(conta_letras('programamos em python', 'consoantes'))