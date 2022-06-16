from time import sleep

def contador(início, fim, passo):
    
    if início < fim:
        passoInt = passo * 1
    elif início > fim:
        passoInt = passo * (-1)
    print('=-' * 20)
    print(f'Contagem de {início} até {fim} com passo {passo} :')

    for i in range(início, fim + int(passoInt/passo), passoInt):
        print(i, end = ' ' , flush = True)
        sleep(0.5)
    print('Fim')
    print()

contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem :')
i = int(input('Início :'))
f = int(input('Fim :'))
p = int(input('Passo :'))
contador(i,f,p)
