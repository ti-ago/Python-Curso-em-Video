
numero=int(input('Informe um número para calcular o fatorial\n'))
numInicial=numero
fatorial=numero
while numero != 1:
    numero-=1
    fatorial*=numero
    
print('{}!={}'.format(numInicial,fatorial))