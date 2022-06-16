termoPA=int(input('Digite o primeiro termo da PA\n'))
razaoPA=int(input('Digite a razão da PA\n'))
contador=1
while contador <= 10:
    print(termoPA,end=' ')
    termoPA+=razaoPA
    contador+=1
    