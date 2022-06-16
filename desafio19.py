from random import choice
a = (input('Digite o primeiro nome '))
b = (input('Digite o segundo '))
c = (input('Digite o terceiro '))
d = (input('Digite o quarto '))
e = (input('Digite o quinto '))
f = (input('Digite o sexto '))
g = (input('Digite o sétimo '))
h = (input('Digite o oitavo '))
i = (input('Digite o nono '))
j = (input('Digite o décimo '))

lista = [a,b,c,d,e,f,g,h,i,j]

sorteado = choice(lista)

print('O aluno sorteado foi {}'.format(sorteado))
