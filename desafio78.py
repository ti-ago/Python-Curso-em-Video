lista=[]
maioresLista=[]
menoresLista=[]

for contador in range(0,5):
    numero=int(input(f'Digite um valor para posição {contador}: '))
    lista.append(numero)

maximo=max(lista)
minimo=min(lista)

while maximo in lista:
    maioresLista.append(lista.index(maximo))
    lista.remove(maximo)
while minimo in lista:
    menoresLista.append(lista.index(minimo))
    lista.remove(minimo)

print(f'\nO maior valor digitado foi {maximo} nas posições ',end='')
for item in maioresLista:
    print(item, end='... ')

if maximo==minimo:
    print(f'\nO menor valor digitado foi {minimo} nas posições ',end='')
    for item in maioresLista:
        print(item, end='... ')
    print('\n')

else:
    print(f'\nO menor valor digitado foi {minimo} nas posições ',end='')
    for item in menoresLista:
        print(item, end='... ')
    print('\n')


