while True:
    numero=int(input('Digite o número que você deseja ver a tabuada '))
    if numero <0:
        break
    multiplicador=1
    while True:
        print('{} x {} = {}'.format(numero, multiplicador, numero*multiplicador))
        multiplicador+=1
        if multiplicador>10:
            break
    