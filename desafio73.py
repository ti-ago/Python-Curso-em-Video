classificacao2021=('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Red Bull Bragantino','Fluminense','América-MG','Atlético-GO','Santos','Ceará','Internacional','São Paulo','Athletico-PR','Cuiabá','Juventude','Grêmio','Bahia','Sport','Chapecoense')
print('MENU')
print('[1] - Exibir os 5 primeiros colocados')
print('[2] - Exibir os 4 últimos colocados')
print('[3] - Exibir os times em ordem alfabética')
print('[4] - Exibir a posição da Chapecoense')
print('[5] - Encerrar')
opcao=0
while True:
    opcao=int(input('Escolha uma opção: '))
    if opcao==1:
        print(classificacao2021[:5])
    elif opcao==2:
        print(classificacao2021[-4:])
    elif opcao==3:
        print(sorted(classificacao2021))
    elif opcao==4:
        print(classificacao2021.index('Chapecoense')+1)
    elif opcao==5:
        break
    else:
        continue
print('Encerrando...')
