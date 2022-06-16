from math import trunc
num = float(input('Digite um número qualquer com vírgula e a porção inteira dele será mostrada a seguir \n'))
print('O número digitado foi {}, sua parte inteira é {} e sua parte fracionada é {:.3f}'.format(num, trunc (num),(num-(trunc(num)))))#investigar isso, o resultado apresenta mais numeros do que deveria
