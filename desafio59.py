
valor1=float(input('Informe um valor\n'))
valor2=float(input('Informe outro valor\n'))
while valor1 and valor2:
    opcao=int(input('\n\n[1] - somar\n[2] - multiplicar\n[3] - maior\n[4] - novos números\n[5] - sair do programa\n'))
      
    if opcao == 1:
        print(f'\nA soma dos valores é {valor1+valor2}')
    if opcao == 2:
        print(f'\nA multiplicação dos valores é {valor1*valor2}')
    if opcao == 3:
        if valor1==valor2:
            print('\nOs valores são iguais')
        else:
            if valor1>valor2:
                print(f'\nO maior é {valor1}')
            else:
                print(f'\nO maior é {valor2}') 
    if opcao == 4:
        valor1=float(input('Informe um valor\n'))
        valor2=float(input('Informe outro valor\n'))
    if opcao == 5:
        break
print('Encerrando...')