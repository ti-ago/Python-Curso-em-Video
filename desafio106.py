def carregaCores():
    global branco, verde, vermelho, amarelo, azul, fimCor
    branco = '\33[7;37;40m'
    verde = '\33[0;30;42m'
    vermelho = '\33[0;30;41m'
    amarelo = '\33[0;30;43m'
    azul = '\33[0;30;44m'
    fimCor = '\33[m'

def cores(cor=''):
    print(cor,end='')
    
def textoColorido(texto,titulo=True,colorir=''):
    if titulo:
        caracteres = len(texto)+10
        cores(colorir)
        print(caracteres*'~')
        print(f'{texto:^{caracteres}}')
        print(caracteres*'~')
        cores(fimCor)
        
    else:
        cores(colorir)
        print(texto)
        cores(fimCor)


def ajuda(comando=''):
    carregaCores()
    while True:
        textoColorido('SISTEMA DE AJUDA PYTHON', True, verde)
        comando = str(input('Função ou comando - FIM [sair] >>> '))
        if comando.upper() == 'FIM':
            break
        else:
            textoColorido(f"Acessando manual do comando '{comando}'", True, azul)
            cores(branco)
            help(comando)
            cores(fimCor)


ajuda()
