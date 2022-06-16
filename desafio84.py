from ntpath import join


pessoas=list()
individuo=list()
maiorPeso=0
menorPeso=0
maisPesado=list()
maisLeve=list()
while True:
    nome=str(input('Informe o primeiro nome da pessoa: '))
    if nome:
        massa=int(input('Digite o peso: '))
        if maiorPeso==0:
            maiorPeso=massa
            menorPeso=massa
            maisPesado=[nome]
            maisLeve=[nome]
        else:
            if massa == maiorPeso:
                maisPesado.append(nome)
            if massa == menorPeso:
                maisLeve.append(nome)
            elif massa>maiorPeso:
                maiorPeso=massa
                maisPesado=[nome]
            elif massa<menorPeso:
                menorPeso=massa
                maisLeve=[nome]
            
        
        individuo.append(nome)
        individuo.append(massa)
        pessoas.append(individuo[:])
        individuo.clear()
    else:
        break
print(50*'=-')
print('Foram cadastradas {} pessoas'.format(len(pessoas)))
print(f'O maior peso cadastrado foi {maiorPeso}Kg referente a ',end='')
for pessoa in range(len(maisPesado)):
    if pessoa < (len(maisPesado)-2):
        print(maisPesado[pessoa],end=', ')
    elif pessoa == (len(maisPesado)-2):
        print(maisPesado[pessoa], end=' e ')
    else:
        print(maisPesado[pessoa])
print(f'\nO menor peso cadastrado foi {menorPeso}Kg referente a ',end='')
for pessoa in range(len(maisLeve)):
    if pessoa < (len(maisLeve)-2):
        print(maisLeve[pessoa],end=', ')
    elif pessoa == (len(maisLeve)-2):
        print(maisLeve[pessoa], end=' e ')
    else:
        print(maisLeve[pessoa])
print('\n')

