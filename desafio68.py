from random import randint
vitorias=0
while True:
    aposta=str(input('Par ou Ímpar? [P/I]\n')).upper()
    if aposta != 'P' and aposta!= 'I':
        print('Opção incorreta, tente novamente P ou I')
        continue
    numero=int(input('Escolha um número\n'))
    cpu=randint(1,10)
    print(f'O computador jogou {cpu} e você {numero}\nTotal {cpu+numero} que é ',end='')
    if (cpu+numero)%2==0:
        print('PAR')
    else:
        print('ÍMPAR')
    if aposta=='P':
        print('Você escolheu Par')
        if (cpu+numero)%2==0:
            print('***Você ganhou***\n')
            vitorias+=1
        else:
            print('---Você perdeu---\n')
            break
    else:
        print('Você escolheu Ímpar')
        if (cpu+numero)%2==1:
            print('***Você ganhou***\n')
            vitorias+=1
        else:
            print('---Você perdeu---\n')
            break
print('Você teve {} vitórias consecutivas.'.format(vitorias))
