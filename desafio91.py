from operator import itemgetter
from random import randint
from time import sleep
jogo=dict()
print(f'{"Valores Sorteados":-^70}')
for j in range (1,5):
    jogo [f'jogador{j}'] = randint(1,6)
for k, v in jogo.items():
    #sleep(0.7)
    print(f' O {k} tirou {v} no dado')

ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{" RANKING DOS JOGADORES ":=^50}')
for posicao, item in enumerate(ranking):
    print(f'{posicao+1}°  {item[0]} com {item[1]}')