def leiadinheiro():
    while True:
        valor = str(input('Digite um valor :'))
        valor = valor.strip().replace(',','.')
        if valor.isnumeric():
                break
        if '.' in valor[-3:]:
            teste = valor.replace('.','',1)
            if teste.isnumeric():
                break
        print(f'\33[0;31m<<< Dado incorreto >>> "{valor}" é inválido\33[m')
    return float(valor)
