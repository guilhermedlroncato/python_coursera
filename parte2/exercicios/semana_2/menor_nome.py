def menor_nome(nomes):
    tam_menor = ''
    nome_menor = ''
    cont = 0
    for nome in nomes:
        if cont == 0:
            nome_menor = nome.strip()
        if len(nome.strip()) < len(tam_menor.strip()):
            nome_menor = nome.strip()
        tam_menor = nome.strip()
        cont += 1
            
    return nome_menor.capitalize().strip()

print(menor_nome(['zé', ' lu', 'fê']))