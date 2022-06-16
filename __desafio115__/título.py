def titulo(texto=''):
    print(40*'-')
    if texto != '':
        print('\033[7;36;40m{:^40}\033[m'.format(texto))
        
