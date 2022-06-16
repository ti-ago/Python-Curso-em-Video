from random import choice
me = int(input('''Vamos Jogar Jokenpô, você conhece?
Escolha uma das três opções abaixo
[1] Pedra
[2] Papel
[3] Tesoura
'''))
pc = choice([1,2,3])
if me==1:
    eu='Pedra'
elif me==2:
    eu='Papel'
elif me==3:
    eu='Tesoura'

if pc==1:
    ele='Pedra'
elif pc==2:
    ele='Papel'
elif pc==3:
    ele='Tesoura'


print("Você escolheu {} e o seu computador escolheu {}, portanto!".format(eu,ele))
if me==pc:
    print("Empatou")
elif me==1 and pc==2 or me==2 and pc==3 or me==3 and pc==1:
    print("Você perdeu")
elif me==1 and pc==3 or me==2 and pc==1 or me==3 and pc==2:
    print("Você venceu")
