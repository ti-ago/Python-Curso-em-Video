lista=[]
print('Para sair tecle ENTER somente')
while True:
    numero=input('Digite um valor:')
    if numero:
        lista.append(int(numero))
    else:
        print('Saindo....')
        break
pares=[]
impares=[]
for item in lista:
    if item % 2==0:
        pares.append(item)
    else:
        impares.append(item)

print('Lista inicial',lista)
print('Lista de números pares',pares)
print('Lista de números ímpares',impares)

