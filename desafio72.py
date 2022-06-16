contagem=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

numero=int(input('Digite um número entre 0 e 20\n'))
while numero < 0 or numero >20:
    numero=int(input('Valor digitado fora do permitido, digite novamente\n'))
print('Você digitou o número {}'.format(contagem[numero]))