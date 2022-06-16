pessoa=dict()
cadastros=list()
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('idade: '))
    pessoa['sexo'] = str(input('sexo M/F: ').upper())
    while True:    
        if pessoa['sexo'] not in 'MmFf':
            print('Digitar M ou F')
            pessoa['sexo'] = str(input('sexo M/F: ').upper())
        break
    
    cadastros.append(pessoa.copy())
    opt=str(input('Continuar S/N: '))
    if opt in 'Ss' :
        continue
    if opt in 'Nn' :
        break

#quantidade pessoas cadastradas
print(f'Foram cadastradas {len(cadastros)} pessoas.')

#media das idades
soma=0
for cadastrado in cadastros:
    soma += cadastrado['idade']
media = soma/len(cadastros)
print('A média de idade é de {:2.1f} anos.'.format(media))

# mulheres
print('São mulheres as seguintes pessoas: ')
for cadastrado in cadastros: 
    if cadastrado['sexo'] in 'Ff':
        print(cadastrado['nome'], end=' ')
print('\n')
        

# pessoas acima da média
print(f'São as pessoas acima da média de {media:2.1f} anos: ')
for cadastrado in cadastros:
    if cadastrado['idade'] > media:
        print(cadastrado['nome'], end=' ')
print('\n')
