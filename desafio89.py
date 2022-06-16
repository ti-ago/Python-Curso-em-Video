alunos=list()
notas1=list()
notas2=list()
medias=list()
dados=[alunos,notas1,notas2,medias]

while True:
#Entrada de dados dos alunos
    nome=str(input('Informe o nome do aluno: '))
    while True:
        nota1=float(input('Informe a primeira nota: '))
        if nota1<0 or nota1>10:
            continue
        else:
            break
    while True:
        nota2=float(input('Informe a segunda nota: '))
        if nota2<0 or nota2>10:
            continue
        else:
            break
    media=(nota1+nota2)/2
    
    
#Acrescenta os dados digitados nas listas respectivas
    alunos.append(nome.upper())
    notas1.append(nota1)
    notas2.append(nota2)
    medias.append(media)
#Validação de saída ou continuação do cadastro
    opcao=str(input('continuar [ENTER]\nsair [0]'))
    while opcao != '0' and opcao!='':
        opcao=str(input('continuar [ENTER]\nsair [0]'))
    print(76*'=')
    if not opcao:
        continue
    elif opcao=='0':
        break


print(29*'-'+'BOLETIM DOS ALUNOS'+29*'-')
print('N°',30*'=','ALUNO',30*'=','MÉDIA')
for item in range (0,len(alunos)):
    
    print(f'{item+1:<2}{alunos[item]:-^70}{medias[item]:>4}')

while True:
    print('MENU')
    print('Escolha sua opção')
    print('[1] - Ver notas de um aluno')
    print('[2] - Ver notas de todos os alunos')
    print('[3] - SAIR')

    menu=int(input('Opção: '))
#Validação da escolha 1
    if menu == 1:
        for aluno in alunos:
            print(aluno)
        escolhido=str(input('Digite o nome do aluno escolhido exatamente como exibido anteriormente: '))
        while escolhido not in alunos:
            escolhido=str(input('ERRO, digite corretamente o nome do aluno: '))
        indice=alunos.index(escolhido)

        print(f'As notas do aluno {escolhido} são {notas1[indice]} e {notas2[indice]}  com média {medias[indice]}')
#Validação da saída da opção escolhida
        retorno=str(input('Para sair [0]\nPara retornar [1]\n'))
        while retorno != '0' and retorno !='1':
            retorno=str(input('Para sair [0]\nPara retornar [1]\n'))
        if retorno == '1':
            continue
        elif retorno == '0':
            break
        

    elif menu == 2:
        
        for item in range (0,len(alunos)):
            print(f'As notas do aluno {alunos[item]:>10} são {notas1[item]:>4} e {notas2[item]:>4}  com média {medias[item]:>4}')
#Validação da saída da opção escolhida
        retorno=str(input('Para retornar [ENTER]\nPara sair [0]\n'))
        while retorno != '0' and retorno !='1':
            retorno=str(input('Para sair [0]\nPara retornar [1]\n'))
        if  retorno == '1':
            continue
        elif retorno == '0':
            break
    elif menu == 3:
        break
    else:
        print('Escolha a opção correta')
        continue
print('Encerrando...')
