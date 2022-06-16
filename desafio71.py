notas100=notas50=notas20=notas10=notas5=notas2=notas1=0
valor=int(input('Valor a ser sacado:\nR$'))
print(50*'=')
print(f"{'BANCO':^50}")
print(50*'=')
while valor:
    if valor>=100:
        notas100=valor//100
        valor=valor-notas100*100
        print(f'{notas100} Cédulas de R$100,00')
        continue
    else:
        if valor>=50:
            notas50=valor//50
            valor=valor-notas50*50
            print(f'{notas50} Cédulas de R$50,00')
            continue
        else:
            if valor>=20:
                notas20=valor//20
                valor=valor-notas20*20
                print(f'{notas20} Cédulas de R$20,00')
                continue
            else:
                if valor>=10:
                    notas10=valor//10
                    valor=valor-notas10*10
                    print(f'{notas10} Cédulas de R$10,00')
                    continue
                else:
                    if valor>=5:
                        notas5=valor//5
                        valor=valor-notas5*5
                        print(f'{notas5} Cédulas de R$5,00')
                        continue
                    else:
                        if valor>=2:
                            notas2=valor//2
                            valor=valor-notas2*2
                            print(f'{notas2} Cédulas de R$2,00')
                            continue
                        else:
                            notas1=valor
                            print(f'{notas1} Moedas de R$1,00')
                            break
print(50*'=')
print(f"{'Tenha um bom dia!':^50}")