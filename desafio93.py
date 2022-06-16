nome = str(input('Nome do jogador: '))
qtd_partidas = int(input('Total de partidas: '))
gols=[]
total=0
for partidas in range (0,qtd_partidas):
    gols.append(int(input(f'Gols na {partidas+1}ª partida: ')))
for itens in gols:
    total+=itens

desempenho={'nome': nome, 'partidas': qtd_partidas, 'gols': gols, 'total': total}
print(desempenho)

print(f'O jogador {desempenho["nome"]} jogou {desempenho["partidas"]} jogos.')
for partida, item in enumerate(gols):
    print(f'    => Na partida {partida+1}, fez {item} gols.')
print(f'Foi um total de {desempenho["total"]}gols.')