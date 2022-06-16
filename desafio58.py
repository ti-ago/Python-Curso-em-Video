from random import randint
tentativas=1
numero = randint(0,10)
aposta = int(input('Tente adivinhar o número, entre 0 e 10\n'))
while aposta != numero:
    aposta = int(input('Você errou, tente novamente\n'))
    tentativas+=1
print('Parabéns você acertou em {} tentativa(s)'.format(tentativas))
