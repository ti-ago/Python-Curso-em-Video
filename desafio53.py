fraseReversa=''
frase=str(input("Digite uma frase qualquer sem acentos ou caracteres especiais, somente letras\n")).upper().replace(' ','')
for letraReversa in range(len(frase)-1,-1,-1):
    fraseReversa+=frase[letraReversa]
if frase == fraseReversa:
    print("É palíndromo ")
else:
    print("Não é palíndromo ")
