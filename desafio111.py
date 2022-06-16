from utilidadesCeV import moeda
from utilidadesCeV import dado

valor = dado.leiadinheiro()
aumento = float(input('Percentual de aumento :'))
reducao = float(input('Percentual de redução :'))

moeda.resumo(valor, aumento, reducao)
