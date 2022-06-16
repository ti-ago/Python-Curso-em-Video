pares=list()
impares=list()
lista=[pares,impares]
for indice in range (0,7):
    numero=int(input(f'Digite o {indice+1}° número :'))
    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)
pares.sort()
impares.sort()

print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')