elementos=int(input('Digite qualquer número inteiro\n'))
contador = 1
ultimo= 1
penultimo = 0
print(penultimo,ultimo,end=' ')
while contador <= elementos-2:
    resultado=ultimo+penultimo
    print(resultado,end=' ')
    penultimo=ultimo
    ultimo=resultado
    contador+=1