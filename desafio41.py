import datetime
ano = int(input('Informe seu ano de nascimento '))
idade = datetime.date.today().year-ano
if idade == 9 or idade < 9:
    print('O competidor estará na classe MIRIM ')
elif idade == 14 or idade < 14:
    print('O competidor estará na clasee INFANTIL ')
elif idade == 19 or idade < 19:
    print('O competidor estará na classe JUNIOR ')
elif idade == 20:
    print('O competidor estará na classe SENIOR ')
else:
    print('O competidor estará na classe MASTER')
