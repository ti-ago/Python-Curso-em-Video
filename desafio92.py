from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento (AAAA): '))
if len(str(nascimento)) < 4:
    nascimento = int(input('Ano de nascimento (AAAA): '))
cadastro['idade'] = date.today().year - nascimento
cadastro['ctps'] = int(input('n° CTPS (digite 0 se não possuir): '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação (AAAA): '))
    if len(str(nascimento)) < 4:
        cadastro['contratacao'] = int(input('Ano de contratação (AAAA): '))
    cadastro['tpa'] = 35 - (date.today().year - cadastro['contratacao'])
    cadastro['salario'] = float(input('Salário mensal: '))
else:
    cadastro['ctps'] = str('NÃO POSSUI')

print(30*'=-')

for item, dados in cadastro.items():
    print(f'{item} tem o valor {dados}')
