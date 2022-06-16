from time import sleep
def maior(*valores):
    iterador = 0
    maior = 0
    print('Os valores digitados foram :')
    for número in valores:
        sleep(0.7)
        print(número, end=' ', flush = True)
        if iterador == 0:
            maior = número
        elif número > maior:
            maior = número
        iterador += 1
        sleep(0.3)
    sleep(0.7)
    print()
    print(f'Dos {iterador} valores, o maior é {maior}')
    
    

maior(1,2,3,7)
maior(1,2,45,5,3,21,23,54,4545,54,3234,65754,23456)