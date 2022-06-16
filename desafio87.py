linha0=[]
linha1=[]
linha2=[]
matriz=[linha0,linha1,linha2]
soma=0
pares=0
for linha in range(0,3):
    for indice in range(0,3):
        numero=int(input(f'Digite um valor para [{linha},{indice}]: '))
        if numero %2 == 0:
            pares+=numero
        matriz[linha].append(numero)
        if indice == 2:
            soma+=matriz[linha][2]
        
for linha in matriz:
    print('')
    for item in linha:
        print(f'[{item:^5}]',end='')
print('\n')
        
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {max(linha1)}')
