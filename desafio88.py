from random import randint
lista=[]
quantidade=int(input('Quantos jogos você deseja criar? '))
for jogos in range (0,quantidade):
    palpite=[]
    dezenas=0
    while dezenas < 6:
        sorteado=randint(1,60)
        if sorteado not in palpite:
            palpite.append(sorteado)
            dezenas+=1
    palpite.sort()
    lista.append(palpite)
    palpite.clear

for item, jogo in enumerate(lista):
    print(17*'--')
    print(f'Jogo n°{item+1}:',end='')
    for dezena in jogo:
        print('[{:2}]'.format(dezena),end='')
    print()
    print(17*'--')
 