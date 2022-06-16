produtos=('lápis',0.5,'celular',1299,'calculadora',110,'pendrive',35,'álcool gel',3.99,'dicionário',40,'repelente',52)
print(60*'-')
print('{:^60}'.format('LISTAGEM DE PREÇOS'))
print(60*'-')

for item in range(0,len(produtos)):
    if item%2==0:
        print('{:.<50}R${:>8.2f}'.format(produtos[item],produtos[item+1]))
print(60*'-')
for item in produtos[0::2]:
    print('{:.<50}R${:>8.2f}'.format(item,produtos[produtos.index(item)+1]))
print(60*'-')