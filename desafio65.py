maior=0
menor=0
soma=0
quantidade=0
opcao=1
opcao=int(input('Deseja começar?\n[1] - SIM   [2] - NÃO'))
while opcao == 1:    
    numero=int(input('Digite um número qualquer\n'))
    quantidade+=1
    if numero>maior:
        maior=numero
    if quantidade==1:
        menor=numero
    elif numero<menor:
        menor=numero
  
    soma+=numero
    opcao=int(input('Deseja continuar?\n[1] - SIM   [2] - NÃO'))
if soma:
    media=soma/quantidade
    print(f'A media foi {media}')
    print(f'O maior é {maior}\nO menor é {menor}')