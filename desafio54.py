from datetime import date
anoAtual=date.today().year
maiores=0
for pessoa in range (0,7):
    anoNascimento=int(input("Informe o ano de nascimento da pessoa "))
    if anoAtual-anoNascimento>=18:
        maiores+=1
print("Foram informadas {} pessoas maiores de idade e {} menores.".format(maiores,pessoa-maiores+1))