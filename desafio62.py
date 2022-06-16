termoPA=int(input('Digite o primeiro termo da PA\n'))
razaoPA=int(input('Digite a razão da PA\n'))
contador=1
while contador <= 10:
    print(termoPA,end=' ')
    termoPA+=razaoPA
    contador+=1

opcao=int(input('Deseja exibir mais 10 termos?\n[1]-SIM   [0]-NÃO\n'))
while opcao == 1:    
    limite=contador+10
    while contador < limite:
        print(termoPA,end=' ')
        termoPA+=razaoPA
        contador+=1
    opcao=int(input('Deseja exibir mais 10 termos?\n[1]-SIM   [0]-NÃO\n'))
print('encerrando...')