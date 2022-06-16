palavras=('TELA','AMOR','LAPISEIRA','BANANA','CAVACO','BIBLIA','MATRIARCA','CELULAR','CARRO','ESCAPE','TECLADO','VENTO','MONTANHA','AGUIA','PROFESSOR')
vogais=('A','E','I','O','U')
for palavra in palavras:
    print(f'NA PALAVRA {palavra} temos: ',end="")
    for letra in palavra:
        if letra in vogais:
            print(letra,end=" ")
    print('\n')