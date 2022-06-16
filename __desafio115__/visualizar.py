try:
    from __desafio115__ import título
except:
    import título
def visualizar():
    título.titulo('PESSOAS CADASTRADAS')
    título.titulo()
    try:
        arq = open('/home/tiago/Codding/python/Python-Curso-em-Video/__desafio115__/Cadastrados.txt','r')
        print(arq.read())
        arq.close()
    except:
        print('Nenhuma pessoa cadastrada')