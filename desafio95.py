todos_jogadores = list()


while True:
    
    menuPrincipal = int(input(f'{"DESEMPENHO DOS JOGADORES":-^40} '+'\n[1] - Cadastro de jogadores\n[2] - Visualizar dados dos jogadores\n[3] - Sair\n'+ '-' * 40 + '\nOpção escolhida :'))
    
    if menuPrincipal == 1:
        print(f'{"NOVO CADASTRO":-^40}')
        while True:
            
            jogador = dict()

            jogador['nome'] = str(input('Nome: '))
            jogador['qtd_partidas'] = int(input('Partidas jogadas: '))
            jogador['gols_por_partida']=list()
            jogador['total_gols'] = 0
            for c in range(1,jogador['qtd_partidas']+1):
                jogador['gols_por_partida'].append(int(input(f'Gols na partida {c}: ')))
                jogador['total_gols'] +=jogador['gols_por_partida'][c-1]
            todos_jogadores.append(jogador.copy())
            

            if str(input('Quer continuar? [S/N] : ')) in 'Ss':
                print(40 * '-')
                continue
            else:
                print(40 * '-')
                break
        continue
    if menuPrincipal == 2:
        print(f'{"EXIBIR DADOS":-^40}')
        if len(todos_jogadores) == 0:
            print('Não há dados a exibir')
            continue

        menuSecundario = int(input('-'*40 +'\n[1] - Escolher jogadores\n[2] - Exibir todos\n[3] - Sair\n'+'-'*40 + '\nOpção escolhida :'))
    
        if menuSecundario == 1:
            print(40 * '-')
            for c in range (0,len(todos_jogadores)):
                print(c+1,todos_jogadores[c]['nome'])
            print(40 * '-')
            escolha_exibir = list()
            while True:
                escolhido = str(input('Número do jogador [continuar - ENTER] / [sair - 0]: '))
                
                if not escolhido:
                    print('Saindo...')
                    break
                elif int(escolhido) == 0:
                    print('Saindo...')
                    break         
                                
                elif int(escolhido) in escolha_exibir:
                    print('Jogador já selecionado, tente novamente')
                    continue
                
                elif int(escolhido) > len(todos_jogadores):
                    print('Valor escolhido é inválido, escolha outro')
                    continue

                escolha_exibir.append(int(escolhido))
                
                if len(escolha_exibir) == len(todos_jogadores):
                    print('Você escolheu todos os jogadores')
                    break
            print()
            for item in escolha_exibir:
                for chave, valor in todos_jogadores[item-1].items():
                    print(f'{chave:.<40}{valor}')
                print()
        if menuSecundario == 2:
            print(40 * '-')
            for c in range(0,len(todos_jogadores)):
                for chave, valor in todos_jogadores[c].items():
                    print(f'{chave:.<40}{valor}')
                print()

    if menuPrincipal == 3:
        print('Encerrando Programa...')
        break
    