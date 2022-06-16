n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
n3 = int(input('Digite o terceiro número '))
#conta 1
if n1-n2<0:
    ma1 = n2
    me1 = n1
else:
    ma1 = n1
    me1 = n2
#conta 2
if n1-n3<0:
    ma2 = n3
    me2 = n1
else:
    ma2 = n1
    me2 = n3
#conta 3
if n2-n3<0:
    ma3 = n3
    me3 = n2
else:
    ma3 = n2
    me3 = n3
#conclusão de maior
if ma1==ma2:
    maior=n1
if ma1==ma3:
    maior=n2
if ma2==ma3:
    maior=n3
#conclusão de menor
if me1==me2:
    menor=n1
if me1==me3:
    menor=n2
if me2==me3:
    menor=n3
print('O maior é o número {}\nO menor é o número {}.'.format(maior,menor))
