def area(largura=0 , comprimento=0):
    largura = float(input('Largura (m):'))
    comprimento = float(input('Comprimento (m):'))
    área_do_terreno = largura * comprimento
    print('A área do terreno é de :')
    print(str(área_do_terreno)+'m²')

area()

