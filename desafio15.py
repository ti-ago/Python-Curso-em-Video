dias = int(input('O carro ficou alugado por quantos dias?\n '))
km = float(input('Quantos km o carro rodou durante o período?\n '))
valor = ((dias*60)+(km*0.15))
print('O valor total devido é de R${:.2f} reais'.format(valor))