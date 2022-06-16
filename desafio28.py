from random import randint
n = randint(0,5)
c = int(input('Qual é o número da sua aposta ?\n'))
if n==c:
    print('Parabéns, você acertou!')
else:
    print('Você perdeu, tente novamente')