# adaptado do desafio107, usa o mesmo módulo do 107
from utilidadesCeV import moeda

valor = float(input('Digite um valor :'))
aumento = float(input('Percentual de aumento :'))
reducao = float(input('Percentual de redução :'))

print(
    f'O valor {moeda.moeda(valor,True)} aumentado em {aumento} % é :\t{moeda.aumentar(valor, aumento, True)}')
print(
    f'O valor {moeda.moeda(valor)} reduzido em {reducao}% é :\t\t{moeda.diminuir(valor, reducao, True)}')
print(f'O dobro do valor {moeda.moeda(valor, True)} é igual a :\t\t{moeda.dobro(valor,True)}')
print(
    f'A metade do valor {moeda.moeda(valor, True)} é igual a :\t\t{moeda.metade(valor,True)}')
