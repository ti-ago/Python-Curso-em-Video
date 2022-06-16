def fatorial(num,show=False):
    fat=1
    for i in range (num,0,-1):
        fat=i*fat
        if show:
            if i>1:
                print(f'{i}',end=' x ')
            else:
                print(f'{i} = {fat}')
    if not show:            
        print(f'{num}! = {fat}')


userNum=int(input('Digite um número :'))
fatorial(userNum)