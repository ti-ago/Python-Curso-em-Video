lista=[]
print('Para sair tecle ENTER somente')
while True:
    numero=input('Digite um valor:')
    if numero:
        lista.append(int(numero))
    else:
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores')
print('Esta é a lista em ordem descrescente ',end='')
print(lista)
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')

