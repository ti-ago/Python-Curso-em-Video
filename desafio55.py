maior=0
menor=0
for pessoa in range(0,5):
    peso=float(input("Digite o peso da pessoa "))
    if peso > maior:
        maior=peso
    if peso < menor or pessoa==0:
        menor=peso
print("O maior peso lido foi {} e o menor peso lido foi {}.".format(maior,menor))
