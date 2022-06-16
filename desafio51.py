primeiroTermo=int(input("Digite o primeiro termo da PA\n"))
razao=int(input("Dgiite a razão da PA\n"))
item=primeiroTermo-razao
for PA in range(0,10):
    print(item+razao,end=' ')
    item+=razao
