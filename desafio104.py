def leiaInt(numero=''):
    numero = str(input('Digite um número inteiro:'))
    if numero.isnumeric():
        print(f'Você digitou o número {numero}.')
    else:
        print('Dado inválido, digite número inteiro')

   
leiaInt()
