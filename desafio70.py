contador=0
valorTotal=0
maioresDe1000=0
menorValor=0
maisBarato=''
while True:
    nome=str(input('Produto: '))
    preco=float(input('preço: R$'))
    if contador==0:
        maisBarato=nome
        menorValor=preco
    if preco > 1000:
        maioresDe1000+=1
    if preco<menorValor:
        maisBarato=nome
        menorValor=preco
    contador+=1
    valorTotal+=preco
    opcao=str(input('Quer continuar? [S/N] ')).upper()
    if opcao=='N':
        break
print(20*'-',' FIM DO PROGRAMA ',20*'-')
print(f'O total da compra foi R${valorTotal:.2f}')
print(f'Temos {maioresDe1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisBarato} que custa R${menorValor:.2f}')