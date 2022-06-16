linha0=[]
linha1=[]
linha2=[]
matriz=[linha0,linha1,linha2]

for linha in range(0,3):
    for indice in range(0,3):
        numero=int(input(f'Digite um valor para [{linha},{indice}]: '))
        matriz[linha].append(numero)

for linha in matriz:
    print('')
    for item in linha:
        print(f'[{item:^5}]',end='')
print('\n')
        
