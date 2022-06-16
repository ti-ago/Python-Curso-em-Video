from math import floor
v = float(input('Qual é a velocidade do veículo ? \n'))
if floor(v)<=80:
    print('O veículo está dentro dos limites de velocidade')
else:
    print('O veículo está acima do limite permitido.\nA multa será de R${:.2f}.'.format((floor(v)-80)*7))