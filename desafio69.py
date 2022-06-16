maiores=0
homens=0
mulheres=0

while True:
    while True:
        idade=int(input('Digite a idade da pessoa\n'))
        if idade < 0:
            continue

        else:
            break
    while True:
        sexo=str(input('Informe o sexo [M/F]\n')).upper()
        if sexo != 'M' and sexo != 'F':
            print('Opção inválida, tente novamente')
            continue
        else:
            break
    if idade>18:
        maiores+=1
    if sexo=='M':
        homens+=1
    elif sexo=='F' and idade<20:
        mulheres+=1
    continuar=str(input('Deseja continuar? [S/N]\n')).upper()
    if continuar=='S':
        continue
    elif continuar=='N':
        break
print(f'{maiores} maiore(s) de 18 anos\n{homens} homens\n{mulheres} mulheres menores de 20 anos')
