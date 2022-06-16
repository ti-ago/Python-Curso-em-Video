from __desafio115__ import título
from __desafio115__ import opções
from __desafio115__ import visualizar
from __desafio115__ import cadastrar

while True:
    título.titulo('MENU PRINCIPAL')
    escolha = opções.mostraMenu(('Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'))
    if escolha == 1:
        visualizar.visualizar()
    elif escolha == 2:
        cadastrar.cadastrar()
    elif escolha == 3:
        print('Encerrando...')
        break
    else:
        print('Opção inválida, tente novamente')
