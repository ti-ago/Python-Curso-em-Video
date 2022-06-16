def leiaInt(numero=''):
    while True:
        numero = str(input('Digite um número Inteiro:'))
        if numero.isnumeric():
            print(f'Você digitou o número {numero}.')
            break
        else:
            print('\033[0;31mDado inválido, digite número inteiro\033[m')
            continue

def leiaFloat(numero=''):
    while True:
        numero = str(input('Digite um numero Real :'))
        numero = numero.strip().replace(',','.')
        if numero.isnumeric():
                print(f'Você digitou o número {numero}.')
                break
        if '.' in numero:
            teste = numero.replace('.','',1)
            if teste.isnumeric():
                print(f'Você digitou o número {numero}.')
                break
        print(f'\33[0;31m<<< Dado incorreto >>> "{numero}" é inválido\33[m')
    return float(numero)

   
leiaInt()
leiaFloat()