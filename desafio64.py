soma=0
quantidade=0
numero=int(input('Digite um número qualquer, pra sair digite 999\n'))
while numero != 999:
    quantidade+=1
    soma+=numero
    numero=int(input('Digite um número qualquer, pra sair digite 999\n'))
print(f'Foram digitados {quantidade} numeros\nA soma total foi {soma}')