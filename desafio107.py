from utilidadesCeV import moeda

valor = float(input('Digite um valor :'))
aumento = float(input('Percentual de aumento :'))
reducao = float (input('Percentual de redução :'))

print(f'O valor {valor} aumentado em {aumento} % é :{moeda.aumentar(valor, aumento)}')
print(f'O valor {valor} reduzido em {reducao}% é :{moeda.diminuir(valor, reducao)}')
print(f'O dobro do valor {valor} é igual a :{moeda.dobro(valor)}')
print(f'A metade do valor {valor} é igual a :{moeda.metade(valor)}')