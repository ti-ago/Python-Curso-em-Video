def escreva(texto = ''):
    texto = str(input('Digite algo :'))
    caracteres = len(texto)+2
    print('~'*caracteres)
    print(f'{texto:^{caracteres}}')
    print('~'* caracteres)
    

escreva()