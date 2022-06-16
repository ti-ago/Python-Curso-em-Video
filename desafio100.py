def sorteia(quantidade=0,inicio=0,final=0):

    ''' Sorteia uma quantidade de valores especificada pelo usuário em uma lista crescente de números sequenciais com início e fim também especificados pelo usuário, sendo:  sorteia(quantidade de números sorteados, início do campo de sorteio, fim do campo de sorteio'''

    from random import choice

    global listaSorteados

    números=list()
    listaSorteados=list()
    for contador in range(inicio,final+1):
        números.append((contador))
    
    for c in range(1,quantidade+1):
        sorteado = choice(números)
        listaSorteados.append((sorteado))
        números.remove(sorteado)
    (listaSorteados.sort())

    
    print(f'Os {quantidade} números sorteados de {inicio} a {final} foram :')
    for n in listaSorteados:
        print(n, end=' ')
    print()
   
def somaPar(lista = None):
    lista = listaSorteados
    soma = 0
    for item in lista:
        if int(item) % 2 == 0:
            soma += int(item)
    print(f'A soma entre os números pares desta sequência foi : {soma}')
    
      
(sorteia(3,1,10))
(somaPar())



