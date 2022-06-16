primo=1
numero=int(input("Digite um número inteiro qualquer "))
for divisores in range (2,numero):
    if numero%divisores==0:
        print("Este número não é primo")
        primo=0
        break
if primo:
    print("Este número é primo")
