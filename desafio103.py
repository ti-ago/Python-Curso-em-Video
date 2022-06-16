def ficha(nome='', gols=''):
    nome = input('Nome do Jogador : ')
    nome.strip()
    if not nome:
        nome = '<desconhecido>'
    gols = input('Número de gols: ')
    if not gols.isnumeric():
        gols = '0'
    gols = int(gols)
    print('O jogador {} fez {} gol(s).'.format(nome, gols))


ficha()
