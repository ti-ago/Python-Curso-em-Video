from random import shuffle
t1 = str(input('Qual o primeiro item da lista ? '))
t2 = str(input('Qual o segundo ? '))
t3 = str(input('Qual o terceiro ? '))
t4 = str(input('Qual o quarto ? '))
t5 = str(input('Qual o quinto ? '))

list = [t1,t2,t3,t4,t5]

shuffle(list)

print('A sequência será {}'.format(list))

shuffle(list)
print(list)