import datetime
ano_atual=datetime.date.today().year
ano=int(input('Qual o ano do seu nascimento ? '))
idade=ano_atual-ano
if idade<18:
    print('Você tem {}anos, seu alistamento será em {}.'.format(idade,ano+18))
elif idade==18:
    print('Você fez ou fará 18 anos em {},seu alistamento será neste ano'.format(ano_atual))
else:
    print('A data do seu alistamento já passou.\nDeveria ter sido feito em {}.'.format(ano+18))