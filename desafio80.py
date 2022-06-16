lista=[]
for contador in range(0,5):
    numero=int(input('Digite um valor : '))
    if contador==0:
        lista.append(numero)
        print(f'número {numero} inserido na posição 0')
    else:
        for itens in range(0,len(lista)):
            if numero <= lista[itens]:
                lista.insert(itens, numero)
                print(f'número {numero} inserido na posição {itens}')
                break
            elif numero > lista[-1]:
                lista.append(numero)
                print(f'número {numero} inserido no fim da lista')
                break
                
print(lista)
