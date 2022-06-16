def leiaInt(numero=''):
    while True:
        try:
            numero = int(input('Digite um número Inteiro: '))
        except:
            print('\033[1;31mDado inválido\033[m')
            continue
        else:
            return numero

def leiaFloat(numero=''):
    while True:
        try:
            numero = float(input('Digite um número Real: '))
        except:
            print('\033[1;31mDado inválido\033[m')
            continue
        else:
            return numero


print(leiaInt())
print(leiaFloat())