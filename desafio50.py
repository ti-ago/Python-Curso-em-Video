soma=0
for item in range(0,6):
    numero=float(input("Digite um número qualquer\n"))
    if numero%2==0:
        soma+=numero
print(f"A soma dos números pares foi {soma}")