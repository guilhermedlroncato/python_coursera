def main():
    menu = 'Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '
    escolha = int(input(menu))
    if escolha != 1 and escolha != 2:
        print('Opção invalida!')
        main()
    else:
        if escolha == 1:
            print('\nVocê escolheu partida isolada!\n')
            partida()
            print('\nPlacar: Você 0 X 1 Computador')
        if escolha == 2:
            print('\nVocê escolheu campeonato!\n')
            print('**** Rodada 1 ****\n')
            partida()
            print('\n**** Rodada 2 ****\n')
            partida()
            print('\n**** Rodada 3 ****\n')
            partida()
            print('\nPlacar: Você 0 X 3 Computador')

def usuario_escolhe_jogada(n,m):
    opcao = False
    while opcao != True:
        retira = int(input('\nQuantas peças você vai tirar? '))
        if (retira <= n) and (retira <= m) and (retira > 0):
            opcao = True
        else:
            print('Oops! Jogada inválida! Tente de novo.')

    print(f'Voce tirou {retira} peças.\n')
    print(f'Agora resta apenas {n - retira} peça no tabuleiro.')
    return retira

def computador_escolhe_jogada(n,m):
    multiplo = m + 1
    valor_escolha = 0
    x = 1
    
    while x <= m:
        if (n - x) % multiplo == 0:
            valor_escolha = x
        x += 1
    
    if valor_escolha <= n:
        retira = valor_escolha
    else:
        retira = n                
    print(f'O computador tirou {retira} peça.')
    if (n - retira) == 0:
        print('Fim do jogo! O computador ganhou!')
    else:
        print(f'Agora resta apenas {n - retira} peça no tabuleiro.')
    return retira

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    prox_jogador = ''

    if n % (m + 1) == 0:
        print('\nVocê começa!\n')
        n = n - usuario_escolhe_jogada(n,m)
        prox_jogador = 'computador'
    else:
        print('\nComputador começa!\n')
        n = n - computador_escolhe_jogada(n,m)
        prox_jogador = 'voce'

    while n > 0:
        if prox_jogador == 'computador':
            n = n - computador_escolhe_jogada(n,m)
            prox_jogador = 'voce'
        else:
            n = n - usuario_escolhe_jogada(n,m)
            prox_jogador = 'computador'    

main()