frase = str(input('Digite uma frase qualquer '))
search = str(input('Digite a letra que você quer procurar na frase '))
prep = frase.upper()
print('A primeira letra "{}" na frase está na posição {} .' .format(search,(prep.find(search.upper())+1)))
print('A última letra "{}" na frase está na posição {}.'.format(search,(prep.rfind(search.upper())+1)))