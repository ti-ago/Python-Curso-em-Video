aluno=dict()
aluno['nome'] = str(input('Informe o nome do aluno: '))
aluno['media'] = float(input(f'Qual foi a média de {aluno["nome"]}: '))
if aluno['media'] < 6:
    aluno['situacao'] = 'reprovado'
else:
    aluno['situacao'] = 'aprovado'
print(f'A situação de {aluno["nome"]} é {aluno["situacao"]}')

print(aluno)
