c = (float(input('Qual o valor do imóvel? ')))
s = (float(input('Qual a renda do comprador? ')))
m = (int(input('Qual a quantidade de parcelas? ')))
prest = c/m
max = s*0.3
if prest>max:
    print('O empréstimo foi negado')
else:
    print('O financiamento foi aprovado, o valor das {} mensalidades serão de R${:.2f}.'.format(m,prest))

