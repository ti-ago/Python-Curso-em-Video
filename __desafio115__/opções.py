try:
    from __desafio115__ import título
except:
    import título

def mostraMenu(opções = list()):
    título.titulo()
    for i in range(0,len(opções)):
        print(f'\033[0;32m{i + 1}\033[m - \033[0;34m{opções[i]}\033[m')
    título.titulo()
        
    escolha = 0
    while True:
        try:
            escolha = int(input('\033[0;33mSua opção: \033[m'))
        except:
            print('\033[0;31mOpção inválida\033[m')
            continue
        if escolha not in range(1,len(opções)+1):
            print('\033[0;31mOpção inválida\033[m')
            continue
        else:
            break
    
    return escolha
       
