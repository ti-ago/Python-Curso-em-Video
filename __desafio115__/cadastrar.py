try:
    from __desafio115__ import título
except:
    import título
def cadastrar():
    título.titulo('NOVO CADASTRO')
    título.titulo()
    try:
       arq=open('/home/tiago/Codding/python/Python-Curso-em-Video/__desafio115__/Cadastrados.txt','a')
    except:
        arq=open('/home/tiago/Codding/python/Python-Curso-em-Video/__desafio115__/Cadastrados.txt','w')

    nome = str(input('Digite o nome completo da pessoa: ')).upper()
    while True:
        idade = str(input('Digite a idade da pessoa: '))
        if idade.isnumeric():
            idade = int(idade)
            break
        else:
            print('Idade inválida, tente novamente: ')

    linha = str(f'{nome:<50}{idade:<3}anos\n')
    arq.write(linha)
    arq.close()
    print(f'Registro de {nome.split()[0]} foi adicionado corretamente ')