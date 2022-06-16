a=int(input('Digite um valor: '))
b=int(input('Digite um valor: '))
c=int(input('Digite um valor: '))
d=int(input('Digite um valor: '))
tupla=(a,b,c,d)
print(f'O número 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro 3 está na {tupla.index(3)+1}° posição.')
else:
    print('O número 3 não foi encontrado em nenhuma posição')
print('Os números pares digitados foram: ',end='')
for numero in tupla:
    if numero%2==0:
        print(numero,end=' ')
print('\n')