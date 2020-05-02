import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos(as_a):
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
            
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', str(sentenca))

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def retira_pontuacao(texto):
    return texto.replace(',','').replace('.','')

def tot_palavras(texto):
    return len(texto)

def total_palvras_texto(texto):
    return texto.split()

def calcula_media_palavras(texto):
    qtd_palavras = total_palvras_texto(texto)
    total_palavras = tot_palavras(qtd_palavras)
    tamanho_palavras = 0
    for i in qtd_palavras:
        tamanho_palavras += len(i)
    return tamanho_palavras / total_palavras

def calcula_media_sentenca(texto):
    sentencas = separa_sentencas(texto)
    total_caracter = len(texto) - len(sentencas)
    return total_caracter / len(sentencas)

def calcula_media_frase(texto):
    frases = len(separa_frases(separa_sentencas(texto)))
    total_caracter = len(texto) - frases
    return total_caracter / frases

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    cont = 0
    dif = 0
    for i in as_a:
        dif += abs(i - as_b[cont])
        cont += 1
       
    return dif/6    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = []
    texto_sem_pontacao = retira_pontuacao(texto)
    lista_palavras = total_palvras_texto(texto_sem_pontacao)
        
    ##### inicio calculo média #####
    media = calcula_media_palavras(texto_sem_pontacao)
    assinatura.append(media)    
    ##### fim calculo média #####
    
    ##### inicio relação type-token #####
    type_token = n_palavras_diferentes(lista_palavras) / tot_palavras(lista_palavras)
    assinatura.append(type_token)
    ##### fim relação type-token #####

    ##### inicio relação hapax-legomana #####
    hapax_legomana = n_palavras_unicas(lista_palavras) / tot_palavras(lista_palavras)
    assinatura.append(hapax_legomana)
    ##### fim relação hapax-legomana #####

    ##### inicio tamanho medio sentenças #####
    media_sentencas = calcula_media_sentenca(texto)
    assinatura.append(media_sentencas)
    ##### fim tamanho medio sentenças #####

    ##### inicio complexidade sentenças #####
    complexidade_sentencas = len(separa_frases(separa_sentencas(texto))) / len(separa_sentencas(texto))
    assinatura.append(complexidade_sentencas)
    ##### fim complexidade sentenças #####

    ##### inicio tamanho medio frases #####
    media_frases = calcula_media_frase(texto)
    assinatura.append(media_frases)
    ##### fim tamanho medio frases #####

    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridade = []
    for i in textos:
        assinatura_autor = calcula_assinatura(i)
        similaridade.append(compara_assinatura(ass_cp, assinatura_autor))
    
    n_min = min(similaridade)
    n_pos = similaridade.index(n_min) + 1
    
    return n_pos

assinatura_contaminado = le_assinatura()
print('\n')
textos = le_textos(assinatura_contaminado)
print(f'O autor do texto {avalia_textos(textos, assinatura_contaminado)} está infectado com COH-PIAH')
