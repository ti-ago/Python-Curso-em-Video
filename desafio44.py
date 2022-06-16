preço = float(input("Qual o preço do produto ? "))
pag = int(input('''Qual a forma de pagamento ?
Escolha uma das opções abaixo:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão '''))

if pag==1:
    print("Será aplicado um desconto de 10% ao produto.\nO preço será de R${:.2f}.".format(preço*0.9))
elif pag==2:
    print("Será aplicado um desconto de 5% ao produto.\nO preço será de R${:.2f}.".format(preço*0.95))
elif pag==3:
    print("O preço cobrado será de R${:.2f}".format(preço))
elif pag==4:
    print(" O preço cobrado será de R${:.2f}".format(preço*1.2))
else:
    print("Opção inválida, tente novamente ")

