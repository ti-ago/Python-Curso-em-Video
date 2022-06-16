n = int(input('Digite um número inteiro qualquer, por gentileza ? '))
base = int(input('''Agora, escolha uma base para realizarmos a conversão 
do número que vc escolheu anteriormente, sendo:
[1] para converter para BINÁRIO     (base 2)
[2] para converter para OCTAL       (base 8)
[3] para converter para HEXADECIMAL (base 16)
Sua escolha:'''))
if base == 1:
    print('O número {} convertido para BINÁRIO é {:b}.'.format(n,n))
elif base == 2:
    print('O número {} convertido para OCTAL é {:o}.'.format(n,n))
elif base == 3:
    print('O número {} convertido para HEXADECIMAL e {:X}.'.fomat(n,n))
else:
    print('Sua opção é inválida, tente novamente!')

