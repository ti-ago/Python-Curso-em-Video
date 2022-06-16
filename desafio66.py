soma=0
contador=0
while True:
    numero=int(input('Digite um número - sair 999 '))
    if numero==999:
        break
    soma+=numero
    contador+=1
print(f'A soma dos {contador} números foi de {soma}')
