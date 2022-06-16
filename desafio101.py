def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if 65 > idade > 17:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 15 < idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'

eleitor = int(input('Informe o ano do nascimento (AAAA) :'))
print(voto(eleitor))

