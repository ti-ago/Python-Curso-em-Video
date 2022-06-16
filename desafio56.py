mulheresNovas=0
somaIdades=0
maisVelho=''
idadeMaisVelho=0
for pessoa in range(0,4):
    nome=str(input("Digite o primeiro nome da pessoa\n"))
    idade=int(input("Digite a idade da pessoa\n"))
    sexo=int(input("Gênero:\nSe feminino [0]\nSe masculino [1]"))
    somaIdades+=idade
    if sexo and idade > idadeMaisVelho:
        maisVelho=nome
        idadeMaisVelho=idade
    if not sexo and idade < 20:
        mulheresNovas+=1
media=somaIdades/(pessoa+1)
print(f"A média de idade do grupo é de {media}")
print(f"O homem mais velho se chama {maisVelho}")
print(f"Existem {mulheresNovas} mulheres menores de 20 anos no grupo")