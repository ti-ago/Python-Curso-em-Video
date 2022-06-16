def aumentar(numero, aumento=0, format=False):
    res = numero * (aumento/100+1)
    if format is True:
        return moeda(res, format)
    else:
        return res


def diminuir(numero, reducao=0, format=False):
    res = numero * (1 - reducao/100)
    if format is True:
        return moeda(res, format)
    else:
        return res


def dobro(numero, format=False):
    res = numero * 2
    if format is True:
        return moeda(res, format)
    else:
        return res


def metade(numero, format=False):
    res = numero / 2
    if format is True:
        return moeda(res, format)
    else:
        return res


def moeda(valor, format=False):
    if format is True:
        res = f"R${f'{valor:.2f}':>8}".replace('.', ',')
        return res
    else:
        return valor

def resumo(numero, aumento, reducao):
    print('-'*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('-'*30)
    print(f"{'Preço analisado:':<20}{moeda(numero, True):>10}")
    print(f"{'Dobro do preço:':<20}{dobro(numero, True):>10}")
    print(f"{f'{aumento:.0f}% de aumento:':<20}{aumentar(numero, aumento, True):>10}")
    print(f"{f'{reducao:.0f}% de redução:':<20}{diminuir(numero, reducao, True):>10}")
    print('-'*30)
