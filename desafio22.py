nome = str(input('Digite seu nome completo '))
print('Escrito todo em maiúsculas \n{}'.format(nome.upper()))
print('Escrito todo em minúsculas \n{}'.format(nome.lower()))
print('O nome de {} tem {} letras no total '.format((nome.split()[0]),(len(nome.replace(' ','')))))
print('O primeiro nome tem {} letras '.format(len(nome.split()[0])))