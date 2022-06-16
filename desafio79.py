print('Iniciando...')
print('Para sair, tecle ENTER, sem informar valor algum')
print('-='*70)
lista=[]
while True:
    numero=input("Digite um valor: ")
    if numero:
        if int(numero) not in lista:
            lista.append(int(numero))
        else:
            print('Valor já digitado, tente novamente...')
            continue
    else:
        print('Calculando...')
        break
print('-='*70)
print(sorted(lista))